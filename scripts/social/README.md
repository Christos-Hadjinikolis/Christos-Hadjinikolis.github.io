# Social Publishing

This directory is the repo-local publishing scaffold for syndicating blog posts and related updates.

## What Is Automated Here

- `X`: supported
- `LinkedIn`: supported
- `Medium`: not wired for direct publishing
- `Substack`: not wired for direct publishing

That split is deliberate.

## Why Medium And Substack Are Different

### Medium

Medium's official help states that it is **not issuing new integration tokens** and will **not allow new integrations**. Existing tokens continue to work, but this is not a good foundation for a new automated workflow.

Official source:
- https://help.medium.com/hc/en-us/articles/213480228-API-Importing

Practical recommendation:
- publish manually to Medium
- if you already have an old working integration token, treat it as legacy rather than a long-term dependency

### Substack

Substack's official help says it **does not have a public API** for this use case. The newer developer API is read-only profile lookup, not post publishing.

Official sources:
- https://support.substack.com/hc/en-us/articles/360038433912-Does-Substack-have-an-API
- https://support.substack.com/hc/en-us/articles/45099095296916-Substack-Developer-API

Practical recommendation:
- publish manually on Substack
- use RSS or import tools for archive migration and syndication workflows

## Why You Should Keep RSS

Keep `feed.xml`.

RSS is still useful because:
- it is effectively free to maintain in Jekyll
- Substack explicitly supports RSS-based import for posts
- Medium still supports RSS feeds for profiles and publications
- feed readers and automation tools still use it
- it gives you one neutral machine-readable distribution surface that is not tied to any platform API policy

Official sources:
- Substack publication RSS: https://support.substack.com/hc/en-us/articles/360038239391-Is-there-an-RSS-feed-for-my-publication
- Substack import posts: https://support.substack.com/hc/en-us/articles/360037830351-How-do-I-import-my-posts-from-another-platform-such-as-Mailchimp-WordPress-Medium-or-Ghost
- Medium RSS feeds: https://help.medium.com/hc/en-us/articles/214874118-Using-RSS-feeds-of-profiles-publications-and-topics

Recommendation:
- keep RSS
- consider removing the old FeedBurner-style promo blocks from legacy posts later, but keep the actual feed

## Local Secrets

Copy `.env.example` to `.env`:

```bash
cp .env .env
```

`.env` is gitignored.

## X Setup

Official sources:
- X API overview: https://docs.x.com/overview
- X API docs landing page: https://developer.x.com/en/docs/twitter-api
- v2 create-post migration reference: https://developer.x.com/en/docs/x-api/tweets/manage-tweets/migrate/manage-tweets-standard-to-twitter-api-v2

You need:
- an X developer app/project
- a user access token that can create posts

Set in `.env`:

```env
X_ACCESS_TOKEN=...
```

Publish:

```bash
make social-x ARGS='--text "New post: https://christos-hadjinikolis.github.io/2026/03/27/pyflink-pros-cons-in-2026.html"'
```

## LinkedIn Setup

Official sources:
- Getting access: https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access
- Posts API: https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api?view=li-lms-2025-08

The simplest path for personal posting is:
- create a LinkedIn app
- enable `Share on LinkedIn`
- use member OAuth (`w_member_social`)
- get a user access token
- set your person URN as the author

Set in `.env`:

```env
LINKEDIN_ACCESS_TOKEN=...
LINKEDIN_AUTHOR_URN=urn:li:person:...
LINKEDIN_VERSION=202508
```

Text-only post:

```bash
make social-linkedin ARGS='--text "New ML-Affairs post: https://christos-hadjinikolis.github.io/2026/03/27/when-flink-earns-its-complexity-over-kafka-streams.html"'
```

Article-style post with URL preview metadata supplied explicitly:

```bash
make social-linkedin ARGS='--text "New on ML-Affairs" --article-url "https://christos-hadjinikolis.github.io/2026/03/27/when-flink-earns-its-complexity-over-kafka-streams.html" --title "Kafka Streams vs Flink Is The Wrong Question" --description "When Flink earns its complexity over Kafka Streams."'
```

## Scripts

- `post_x.py`: create a post on X using a configured user access token
- `post_linkedin.py`: create a text or article post on LinkedIn

These scripts intentionally do not try to automate OAuth flows for you. They assume you already have tokens and want a clean, local, repo-owned publishing step.
