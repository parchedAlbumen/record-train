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

- status: understood
- depends-on: git-basics
- introduced: 2026-08-21
- last-reviewed: 2026-08-27
- evidence: Ran `git add .` and `git commit` themselves, correctly predicted the commit confirmation output, and distinguished staged-but-uncommitted from committed. 2026-08-27: after 6 days, recalled unprompted that a commit only saves locally, and predicted "ahead by 1 commit" correctly.

## github

- status: understood
- depends-on: git-basics
- introduced: 2026-08-21
- last-reviewed: 2026-08-27
- evidence: Correctly predicted push would send nothing without a commit first; connected `--set-upstream` to "link local branch to remote branch" after a nudge, and confirmed the single push command both pushed and set the link. 2026-08-27: named push (not commit) as the step that reaches GitHub, and predicted "up to date with origin/main" after pushing.

## gitignore

- status: practicing
- depends-on: git-basics
- introduced: 2026-08-21
- last-reviewed: 2026-08-21
- evidence: Read `git status` output correctly to identify `.claude/settings.local.json` as excluded; after a nudge, reasoned that it's excluded for being machine-specific, not just private.

## node-and-npm

- status: practicing
- depends-on: none
- introduced: 2026-08-21
- last-reviewed: 2026-08-21
- evidence: Correctly explained that deleting `node_modules/` would break `npm run dev` and that `npm install` rebuilds it from `package.json`/`package-lock.json`.

## vite

- status: practicing
- depends-on: node-and-npm
- introduced: 2026-08-21
- last-reviewed: 2026-08-21
- evidence: Ran the scaffold and dev server themselves, correctly predicted a localhost page would open, and chose "ignore files and continue" correctly reasoning it would preserve `.git/` and `learning/`.

## react-components

- status: introduced
- depends-on: vite
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Had `App` explained as a function that returns markup; no independent demonstration yet.

## jsx

- status: practicing
- depends-on: react-components
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Edited the `<h1>` in App.tsx and saw it update live; correctly predicted `{2 + 2}` renders `4` because the braces evaluate JavaScript.

## hmr

- status: introduced
- depends-on: vite
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Observed the page repaint without a full reload right after saving an edit to App.tsx.

## typescript-basics

- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## http-requests-and-responses

- status: introduced
- depends-on: none
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Worked with the request-in / response-out framing while building the endpoint (method + path matched to a handler, return value sent back); no dedicated check yet.

## decorators

- status: practicing
- depends-on: none
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: After the `@x` = `f = x(f)` rewrite, correctly said the decorator registers the function rather than calling it, passed the "how many times has list_runs run at startup" check, and predicted the `NameError` from renaming `app` while leaving `@app.get` in place.

## reading-stack-traces

- status: practicing
- depends-on: none
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: On a real uvicorn traceback, located `main.py:10` as the failing line among the library frames and tied the `NameError` message to the renamed variable.

## endpoints-and-routes

- status: practicing
- depends-on: http-requests-and-responses
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Given a two-route example, said `list_runs` runs 0 times at startup and only when a request hits `/runs` — separated route registration from per-request dispatch.

## json

- status: practicing
- depends-on: http-requests-and-responses
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Filled the endpoint's return dict; predicted the browser would show exactly `message: "hello everyone!"` and connected it to the Python-dict → JSON conversion.

## virtual-environments

- status: practicing
- depends-on: none
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Built and activated a venv in `backend/`; recognised the `(.venv)` prompt prefix as the "it worked" signal; on a fresh-clone prediction, said each machine must recreate its own `.venv` and reinstall from the requirements list, and named `requirements.txt` before it existed. 2026-08-27: predicted `pip install` lands packages inside `.venv`; reasoned `requirements.txt` would have more than 2 lines because FastAPI's dependencies come too; described the clone-side step as reinstalling from that file.

## fastapi-basics

- status: practicing
- depends-on: virtual-environments, endpoints-and-routes
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Filled in the handler's return value, started the server with `uvicorn main:app --reload`, predicted the JSON page correctly, and predicted/diagnosed the crash when `app` was renamed.

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

## git-branches

- status: seed
- depends-on: commits
- introduced: —
- last-reviewed: —
- evidence: — (parked 2026-08-27 at the learner's request; comes due in section 5, done on a `strava` branch)

## pull-requests

- status: seed
- depends-on: git-branches, github
- introduced: —
- last-reviewed: —
- evidence: — (parked 2026-08-27; comes due in section 5 when the `strava` branch merges back)

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