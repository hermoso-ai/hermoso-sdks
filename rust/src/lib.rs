//! The typed Rust client for the [Hermoso API](https://hermoso.ai/docs/api/).
//!
//! `apis` and `models` are GENERATED from the /v1 OpenAPI document by tools/sdk-generate.mjs and must not be edited.
//! This file and `helpers.rs` are the small hand-written layer on top: a client that reads your key, a cursor
//! paginator, a job waiter and a one-line tool call.
//!
//! ```no_run
//! use hermoso::Api; // the trait behind client.api.posts_api(), .credits_api(), …
//! # async fn run() -> Result<(), Box<dyn std::error::Error>> {
//! let client = hermoso::client()?; // reads HERMOSO_API_KEY
//! let credits = client.api.credits_api().get_credits(hermoso::apis::credits_api::GetCreditsParams::builder().build()).await?;
//! # Ok(()) }
//! ```
#![allow(unused_imports)]
#![allow(clippy::too_many_arguments)]

extern crate serde;
extern crate serde_json;
extern crate serde_repr;
extern crate url;

pub mod apis;
pub mod models;
mod helpers;
pub mod spec;

pub use apis::{Api, ApiClient};
pub use helpers::*;
