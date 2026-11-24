// Package hermoso is the typed Go client for the Hermoso API (https://hermoso.ai/docs/sdks/).
//
// Everything in hermoso.gen.go is GENERATED from the /v1 OpenAPI document by tools/sdk-generate.mjs (oapi-codegen) and
// must not be edited. This file is the small hand-written layer on top: a client that reads your key, a cursor
// paginator, a job waiter and a one-line tool call. Every operation is a method on *ClientWithResponses, named after
// its operationId (GetCreditsWithResponse, CreatePostWithResponse, …).
package hermoso

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"iter"
	"net/http"
	"os"
	"strconv"
	"time"
)

// DefaultBaseURL is the Hermoso API.
const DefaultBaseURL = "https://app.hermoso.ai"

// APIError is an error answer from the API (`{"error": {"type", "code", "message", …}}`), returned by the helpers in
// this file. Body is nil when the answer was not the API's error shape.
type APIError struct {
	Status int
	Body   *Error
	Raw    []byte
}

func (e *APIError) Error() string {
	if e.Body != nil && e.Body.Error.Message != "" {
		return fmt.Sprintf("hermoso: %s (%s, HTTP %d)", e.Body.Error.Message, e.Body.Error.Code, e.Status)
	}
	return fmt.Sprintf("hermoso: API error (HTTP %d)", e.Status)
}

func apiError(status int, raw []byte) error {
	e := &APIError{Status: status, Raw: raw}
	var body Error
	if json.Unmarshal(raw, &body) == nil && body.Error.Code != "" {
		e.Body = &body
	}
	return e
}

// NewHermosoClient returns a client authenticated with your API key. An empty apiKey reads HERMOSO_API_KEY. Pass
// WithBrand to act on one brand of an account that holds several, and WithBaseURL or WithHTTPClient as needed:
//
//	client, err := hermoso.NewHermosoClient("", hermoso.WithBrand("brand_123"))
//	res, err := client.GetCreditsWithResponse(ctx, nil)
func NewHermosoClient(apiKey string, opts ...ClientOption) (*ClientWithResponses, error) {
	if apiKey == "" {
		apiKey = os.Getenv("HERMOSO_API_KEY")
	}
	if apiKey == "" {
		return nil, errors.New(`hermoso: no API key: pass one or set HERMOSO_API_KEY. Create one at https://app.hermoso.ai on the "API, MCP & CLI" tab, under "Terminal & API keys"`)
	}
	auth := WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
		req.Header.Set("Authorization", "Bearer "+apiKey)
		return nil
	})
	return NewClientWithResponses(DefaultBaseURL, append([]ClientOption{auth}, opts...)...)
}

// WithBrand acts on this brand (an id from ListBrands) instead of the one the key is pinned to. Sent as
// X-Hermoso-User; a per-call XHermosoUser parameter still wins.
func WithBrand(id string) ClientOption {
	return WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
		if req.Header.Get("X-Hermoso-User") == "" {
			req.Header.Set("X-Hermoso-User", id)
		}
		return nil
	})
}

// Ptr returns a pointer to v, for the optional fields of the generated parameter structs: Ptr("published").
func Ptr[T any](v T) *T { return &v }

// MediaURL is one media item for PostCreate.Media: a Hermoso-hosted URL (from a finished job or CreateMedia).
func MediaURL(url string) PostCreate_Media_Item {
	var item PostCreate_Media_Item
	_ = item.FromPostCreateMedia0(url)
	return item
}

// Paginate yields every item of a cursor-paginated list, calling page with the cursor of the previous page (nil for
// the first) until there is no next cursor. ListAllPosts, ListAllJobs, ListAllTools and ListAllConversionEvents are
// ready-made; use Paginate for any other list.
func Paginate[T any](ctx context.Context, page func(ctx context.Context, cursor *string) (items []T, next *string, err error)) iter.Seq2[T, error] {
	return func(yield func(T, error) bool) {
		var cursor *string
		for {
			items, next, err := page(ctx, cursor)
			if err != nil {
				var zero T
				yield(zero, err)
				return
			}
			for _, it := range items {
				if !yield(it, nil) {
					return
				}
			}
			if next == nil || *next == "" {
				return
			}
			cursor = next
		}
	}
}

func deref[T any](p *[]T) []T {
	if p == nil {
		return nil
	}
	return *p
}

func nextOf(hasMore *bool, next *string) *string {
	if hasMore != nil && !*hasMore {
		return nil
	}
	return next
}

// ListAllPosts yields every post matching params (its StartingAfter is managed for you):
//
//	for post, err := range client.ListAllPosts(ctx, hermoso.ListPostsParams{Status: hermoso.Ptr("published")}) { … }
func (c *ClientWithResponses) ListAllPosts(ctx context.Context, params ListPostsParams) iter.Seq2[Post, error] {
	return Paginate(ctx, func(ctx context.Context, cursor *string) ([]Post, *string, error) {
		params.StartingAfter = cursor
		res, err := c.ListPostsWithResponse(ctx, &params)
		if err != nil {
			return nil, nil, err
		}
		if res.JSON200 == nil {
			return nil, nil, apiError(res.StatusCode(), res.Body)
		}
		return deref(res.JSON200.Data), nextOf(res.JSON200.HasMore, res.JSON200.NextCursor), nil
	})
}

// ListAllJobs yields every job matching params.
func (c *ClientWithResponses) ListAllJobs(ctx context.Context, params ListJobsParams) iter.Seq2[Job, error] {
	return Paginate(ctx, func(ctx context.Context, cursor *string) ([]Job, *string, error) {
		params.StartingAfter = cursor
		res, err := c.ListJobsWithResponse(ctx, &params)
		if err != nil {
			return nil, nil, err
		}
		if res.JSON200 == nil {
			return nil, nil, apiError(res.StatusCode(), res.Body)
		}
		return deref(res.JSON200.Data), nextOf(res.JSON200.HasMore, res.JSON200.NextCursor), nil
	})
}

// ListAllTools yields every tool matching params.
func (c *ClientWithResponses) ListAllTools(ctx context.Context, params ListToolsParams) iter.Seq2[Tool, error] {
	return Paginate(ctx, func(ctx context.Context, cursor *string) ([]Tool, *string, error) {
		params.StartingAfter = cursor
		res, err := c.ListToolsWithResponse(ctx, &params)
		if err != nil {
			return nil, nil, err
		}
		if res.JSON200 == nil {
			return nil, nil, apiError(res.StatusCode(), res.Body)
		}
		return deref(res.JSON200.Data), nextOf(res.JSON200.HasMore, res.JSON200.NextCursor), nil
	})
}

// ListAllConversionEvents yields every conversion event matching params (this list takes its cursor as `cursor`).
func (c *ClientWithResponses) ListAllConversionEvents(ctx context.Context, params ListConversionEventsParams) iter.Seq2[map[string]interface{}, error] {
	return Paginate(ctx, func(ctx context.Context, cursor *string) ([]map[string]interface{}, *string, error) {
		params.Cursor = cursor
		res, err := c.ListConversionEventsWithResponse(ctx, &params)
		if err != nil {
			return nil, nil, err
		}
		if res.JSON200 == nil {
			return nil, nil, apiError(res.StatusCode(), res.Body)
		}
		return deref(res.JSON200.Data), res.JSON200.NextCursor, nil
	})
}

// WaitOptions tunes WaitForJob. Zero values mean every 5 seconds, for up to 20 minutes.
type WaitOptions struct {
	Interval time.Duration
	Timeout  time.Duration
}

// WaitForJob polls a job (a render, a stitch, an upscale…) until it is "done" or "error" and returns it; a finished
// job's file is *job.Url. Polling is free; calling the tool again would start (and bill) a second render. ctx cancels
// the wait, never the job.
func (c *ClientWithResponses) WaitForJob(ctx context.Context, id string, opts *WaitOptions) (*Job, error) {
	interval, timeout := 5*time.Second, 20*time.Minute
	if opts != nil && opts.Interval > 0 {
		interval = opts.Interval
	}
	if opts != nil && opts.Timeout > 0 {
		timeout = opts.Timeout
	}
	deadline := time.Now().Add(timeout)
	for {
		res, err := c.GetJobWithResponse(ctx, id, nil)
		if err != nil {
			return nil, err
		}
		if res.JSON200 == nil {
			return nil, apiError(res.StatusCode(), res.Body)
		}
		job := res.JSON200
		status := ""
		if job.Status != nil {
			status = *job.Status
		}
		if status == "done" || status == "error" {
			return job, nil
		}
		if time.Now().After(deadline) {
			return job, fmt.Errorf("hermoso: job %s is still %s after %s; it keeps running, call WaitForJob again", id, status, timeout)
		}
		select {
		case <-ctx.Done():
			return job, ctx.Err()
		case <-time.After(interval):
		}
	}
}

// RunToolOptions tunes RunTool. Wait nil leaves the server default (a render is held up to 45 seconds); Ptr(0)
// answers at once with a job handle.
type RunToolOptions struct {
	Wait           *int
	IdempotencyKey string
}

// ToolOutcome is what a tool call answered: Result when the tool finished, Job when it queued a render (pass
// *Job.JobId to WaitForJob).
type ToolOutcome struct {
	Result *ToolResult
	Job    *ToolJob
}

// RunTool runs any Hermoso tool through POST /v1/tools/{name} with its arguments. GetToolWithResponse describes each
// tool's arguments.
//
//	out, err := client.RunTool(ctx, "plan_ad", map[string]any{"product": "our cold brew, summer offer"}, nil)
func (c *ClientWithResponses) RunTool(ctx context.Context, name string, args map[string]any, opts *RunToolOptions) (*ToolOutcome, error) {
	params := &CallToolParams{}
	if opts != nil {
		if opts.Wait != nil {
			params.Wait = Ptr(strconv.Itoa(*opts.Wait))
		}
		if opts.IdempotencyKey != "" {
			params.IdempotencyKey = Ptr(opts.IdempotencyKey)
		}
	}
	if args == nil {
		args = map[string]any{}
	}
	res, err := c.CallToolWithResponse(ctx, name, params, ToolCall(args))
	if err != nil {
		return nil, err
	}
	switch {
	case res.JSON202 != nil:
		return &ToolOutcome{Job: res.JSON202}, nil
	case res.JSON200 != nil:
		return &ToolOutcome{Result: res.JSON200}, nil
	}
	return nil, apiError(res.StatusCode(), res.Body)
}
