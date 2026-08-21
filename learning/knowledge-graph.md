# Knowledge graph

## why-python-backend

- status: introduced
- depends-on: none
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Identified the real tradeoff being accepted (describing types twice across Python and TypeScript) after a prompt.

## why-react-typescript-frontend

- status: introduced
- depends-on: why-python-backend
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Independently named two costs of a split stack — two processes to run, and CORS.

## why-fastapi

- status: introduced
- depends-on: why-python-backend
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Recognized the auto-docs page as a way to test endpoints before the frontend exists.

## why-postgres

- status: introduced
- depends-on: none
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Reasoned that copying Strava data locally beats re-fetching; reasons sharpened to rate limits, speed, colocation with lifting data, and ownership.

## why-raw-sql-over-orm

- status: introduced
- depends-on: why-postgres
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Chose raw SQL over SQLAlchemy deliberately, to learn SQL rather than have it hidden.

## secrets-and-dotenv

- status: introduced
- depends-on: gitignore
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Correctly stated that only the .env value changes between local and deployed, and that no code changes.

## overfetching-and-endpoint-design

- status: introduced
- depends-on: endpoints-and-routes
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Argued for a separate chart endpoint on the grounds that the chart needs fewer fields than the list.

## git-basics

- status: practicing
- depends-on: none
- introduced: 2026-08-21
- last-reviewed: 2026-08-21
- evidence: Correctly predicted `git status` would show everything as untracked right after `git init`; correctly reasoned that deleting `.git/` would leave working files untouched.

## commits

- status: practicing
- depends-on: git-basics
- introduced: 2026-08-21
- last-reviewed: 2026-08-21
- evidence: Ran `git add .` and `git commit` themselves, correctly predicted the commit confirmation output, and distinguished staged-but-uncommitted from committed.

## github

- status: seed
- depends-on: git-basics
- introduced: —
- last-reviewed: —
- evidence: —

## gitignore

- status: practicing
- depends-on: git-basics
- introduced: 2026-08-21
- last-reviewed: 2026-08-21
- evidence: Read `git status` output correctly to identify `.claude/settings.local.json` as excluded; after a nudge, reasoned that it's excluded for being machine-specific, not just private.

## node-and-npm

- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## vite

- status: seed
- depends-on: node-and-npm
- introduced: —
- last-reviewed: —
- evidence: —

## react-components

- status: seed
- depends-on: vite
- introduced: —
- last-reviewed: —
- evidence: —

## jsx

- status: seed
- depends-on: react-components
- introduced: —
- last-reviewed: —
- evidence: —

## typescript-basics

- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## http-requests-and-responses

- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## endpoints-and-routes

- status: seed
- depends-on: http-requests-and-responses
- introduced: —
- last-reviewed: —
- evidence: —

## json

- status: seed
- depends-on: http-requests-and-responses
- introduced: —
- last-reviewed: —
- evidence: —

## virtual-environments

- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## fastapi-basics

- status: seed
- depends-on: virtual-environments, endpoints-and-routes
- introduced: —
- last-reviewed: —
- evidence: —

## auto-docs-page

- status: seed
- depends-on: fastapi-basics
- introduced: —
- last-reviewed: —
- evidence: —

## fetch

- status: seed
- depends-on: http-requests-and-responses, react-components
- introduced: —
- last-reviewed: —
- evidence: —

## async-await

- status: seed
- depends-on: fetch
- introduced: —
- last-reviewed: —
- evidence: —

## cors

- status: seed
- depends-on: fetch
- introduced: —
- last-reviewed: —
- evidence: —

## react-state

- status: seed
- depends-on: react-components
- introduced: —
- last-reviewed: —
- evidence: —

## useeffect

- status: seed
- depends-on: react-state
- introduced: —
- last-reviewed: —
- evidence: —

## loading-and-error-states

- status: seed
- depends-on: react-state, fetch
- introduced: —
- last-reviewed: —
- evidence: —

## postgres-setup

- status: seed
- depends-on: why-postgres
- introduced: —
- last-reviewed: —
- evidence: —

## psql

- status: seed
- depends-on: postgres-setup
- introduced: —
- last-reviewed: —
- evidence: —

## tables-and-schemas

- status: seed
- depends-on: postgres-setup
- introduced: —
- last-reviewed: —
- evidence: —

## sql-select

- status: seed
- depends-on: tables-and-schemas
- introduced: —
- last-reviewed: —
- evidence: —

## sql-insert

- status: seed
- depends-on: tables-and-schemas
- introduced: —
- last-reviewed: —
- evidence: —

## parameterized-queries

- status: seed
- depends-on: sql-select, sql-insert
- introduced: —
- last-reviewed: —
- evidence: —

## sql-injection

- status: seed
- depends-on: parameterized-queries
- introduced: —
- last-reviewed: —
- evidence: —

## database-connections

- status: seed
- depends-on: postgres-setup, secrets-and-dotenv
- introduced: —
- last-reviewed: —
- evidence: —

## env-and-environment-variables

- status: seed
- depends-on: secrets-and-dotenv
- introduced: —
- last-reviewed: —
- evidence: —

## what-is-an-api

- status: seed
- depends-on: http-requests-and-responses
- introduced: —
- last-reviewed: —
- evidence: —

## api-keys-and-secrets

- status: seed
- depends-on: what-is-an-api, secrets-and-dotenv
- introduced: —
- last-reviewed: —
- evidence: —

## oauth-flow

- status: seed
- depends-on: what-is-an-api, api-keys-and-secrets
- introduced: —
- last-reviewed: —
- evidence: —

## access-and-refresh-tokens

- status: seed
- depends-on: oauth-flow
- introduced: —
- last-reviewed: —
- evidence: —

## calling-an-external-api

- status: seed
- depends-on: access-and-refresh-tokens
- introduced: —
- last-reviewed: —
- evidence: —

## storing-tokens-safely

- status: seed
- depends-on: access-and-refresh-tokens, database-connections
- introduced: —
- last-reviewed: —
- evidence: —

## syncing-and-deduplication

- status: seed
- depends-on: calling-an-external-api, sql-insert
- introduced: —
- last-reviewed: —
- evidence: —

## recharts

- status: seed
- depends-on: react-components
- introduced: —
- last-reviewed: —
- evidence: —

## filtering-data

- status: seed
- depends-on: recharts
- introduced: —
- last-reviewed: —
- evidence: —

## react-forms

- status: seed
- depends-on: react-state
- introduced: —
- last-reviewed: —
- evidence: —

## post-requests

- status: seed
- depends-on: fetch, endpoints-and-routes
- introduced: —
- last-reviewed: —
- evidence: —

## input-validation

- status: seed
- depends-on: post-requests
- introduced: —
- last-reviewed: —
- evidence: —

## computing-derived-values

- status: seed
- depends-on: sql-select
- introduced: —
- last-reviewed: —
- evidence: —

## hosted-postgres

- status: seed
- depends-on: postgres-setup
- introduced: —
- last-reviewed: —
- evidence: —

## deploying-a-backend

- status: seed
- depends-on: fastapi-basics, env-and-environment-variables
- introduced: —
- last-reviewed: —
- evidence: —

## deploying-a-static-frontend

- status: seed
- depends-on: vite
- introduced: —
- last-reviewed: —
- evidence: —

## production-environment-variables

- status: seed
- depends-on: env-and-environment-variables, deploying-a-backend
- introduced: —
- last-reviewed: —
- evidence: —

## production-vs-development-config

- status: seed
- depends-on: production-environment-variables
- introduced: —
- last-reviewed: —
- evidence: —

## reading-free-tier-limits

- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## reviewing-a-diff

- status: seed
- depends-on: commits
- introduced: —
- last-reviewed: —
- evidence: —

## writing-a-good-plan

- status: introduced
- depends-on: none
- introduced: 2026-08-20
- last-reviewed: 2026-08-20
- evidence: Walked every stack decision and pushed back on two of them (React over plain HTML, raw SQL over an ORM) with reasons.

## agent-memory-and-claude-md

- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —