# frozen_string_literal: true

# The small hand-written layer over the generated client: a client that reads your key, a cursor paginator, a job
# waiter and a one-line tool call. Not generated; tools/sdk-generate.mjs copies it in from sdks/ruby/overlay.
require 'json'
require 'timeout'
require 'uri'

module Hermoso
  DEFAULT_BASE_URL = 'https://app.hermoso.ai'

  # An error answer from the API. +error+ is the parsed body (+error[:error][:code]+, +[:message]+) when there is one.
  class HermosoError < StandardError
    attr_reader :status, :error

    def initialize(status, error)
      @status = status
      @error = error
      detail = error.is_a?(Hash) ? error.dig(:error, :message) : nil
      super(detail || "Hermoso API error#{status ? " (HTTP #{status})" : ''}")
    end

    def self.from_api_error(e)
      body = begin
        JSON.parse(e.response_body.to_s, symbolize_names: true)
      rescue StandardError
        nil
      end
      new(e.code, body)
    end
  end

  # A client authenticated with your API key (default: the HERMOSO_API_KEY environment variable). +brand+ acts on that
  # brand (an id from list_brands) instead of the one the key is pinned to. Pass it to any generated API class:
  #
  #   client = Hermoso.client
  #   credits = Hermoso::CreditsApi.new(client).get_credits
  def self.client(api_key: nil, brand: nil, base_url: DEFAULT_BASE_URL, timeout: 90)
    key = api_key || ENV['HERMOSO_API_KEY']
    if key.nil? || key.empty?
      raise ArgumentError, 'No Hermoso API key: pass api_key: or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai ' \
                           'on the "API, MCP & CLI" tab, under "Terminal & API keys".'
    end
    uri = URI.parse(base_url)
    config = Configuration.new
    config.scheme = uri.scheme
    config.host = uri.port && uri.port != uri.default_port ? "#{uri.host}:#{uri.port}" : uri.host
    config.base_path = uri.path.to_s.sub(%r{/\z}, '')
    config.server_index = nil
    config.access_token = key
    config.timeout = timeout
    api_client = ApiClient.new(config)
    api_client.default_headers['X-Hermoso-User'] = brand if brand
    api_client
  end

  # Every item of a cursor-paginated list, following +next_cursor+ until +has_more+ is false. +api+ is a generated API
  # instance and +operation+ its list method; the rest are that method's options:
  #
  #   posts = Hermoso::PostsApi.new(client)
  #   Hermoso.paginate(posts, :list_posts, status: 'published').each { |post| puts post.id }
  #
  # list_conversion_events takes its cursor as +cursor+; every other list takes +starting_after+. That is detected.
  def self.paginate(api, operation, **opts)
    cursor_param = operation.to_sym == :list_conversion_events ? :cursor : :starting_after
    Enumerator.new do |out|
      cursor = nil
      loop do
        page = begin
          api.public_send(operation, cursor ? opts.merge(cursor_param => cursor) : opts)
        rescue ApiError => e
          raise HermosoError.from_api_error(e)
        end
        (page.data || []).each { |item| out << item }
        cursor = page.next_cursor
        break if cursor.nil? || cursor.empty? || (page.respond_to?(:has_more) && page.has_more == false)
      end
    end
  end

  # Polls a job (a render, a stitch, an upscale…) until it is "done" or "error" and returns it; the file is +job.url+.
  # Polling is free; calling the tool again would start (and bill) a second render.
  def self.wait_for_job(job_id, client:, interval: 5, timeout: 1200)
    jobs = JobsApi.new(client)
    deadline = Process.clock_gettime(Process::CLOCK_MONOTONIC) + timeout
    loop do
      job = begin
        jobs.get_job(job_id)
      rescue ApiError => e
        raise HermosoError.from_api_error(e)
      end
      return job if %w[done error].include?(job.status)
      if Process.clock_gettime(Process::CLOCK_MONOTONIC) > deadline
        raise Timeout::Error, "Job #{job_id} is still #{job.status}; it keeps running, call wait_for_job again."
      end

      sleep interval
    end
  end

  # Runs any Hermoso tool through POST /v1/tools/{name} and returns its result: a ToolResult, or a ToolJob handle when
  # it queued a render (pass +job_id+ to wait_for_job). ToolsApi#get_tool describes each tool's arguments.
  #
  #   plan = Hermoso.run_tool('plan_ad', { product: 'our cold brew, summer offer', format: 'video' }, client: client)
  def self.run_tool(name, args = {}, client:, wait: nil, idempotency_key: nil)
    opts = { debug_return_type: 'Object' }
    opts[:wait] = wait.to_s unless wait.nil?
    opts[:idempotency_key] = idempotency_key if idempotency_key
    data, status, = begin
      ToolsApi.new(client).call_tool_with_http_info(name, args, opts)
    rescue ApiError => e
      raise HermosoError.from_api_error(e)
    end
    status == 202 ? ToolJob.build_from_hash(data) : ToolResult.build_from_hash(data)
  end
end
