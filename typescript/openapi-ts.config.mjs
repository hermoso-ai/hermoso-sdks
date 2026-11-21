// @hey-api/openapi-ts configuration. Run through tools/sdk-generate.mjs (which pins the generator version), never by hand.
export default {
  input: '../openapi.json',
  output: { path: 'src/gen', importFileExtension: '.js' },
  plugins: ['@hey-api/client-fetch', '@hey-api/typescript', '@hey-api/sdk'],
};
