# Learning plan: Training Board

## Locked decisions

- **Backend language: Python** — already shipped a Python backend on the transit project, so the language stops being new and the difficulty lands on OAuth, the database, and deployment instead. Accepted cost: types are described twice (once in Python, once in TypeScript) and kept in sync by hand.
- **Frontend: React with TypeScript, kept deliberately minimal** — no router, no state library, no component library. Chosen over plain HTML/JS to consolidate React, which the learner has only just started touching. Accepted costs: a build toolchain, two processes to run in development, and CORS.
- **Backend framework: FastAPI** — modern Python default, strong in job listings, and its auto-generated docs page lets the backend be tested in isolation before any frontend exists.
- **Database: PostgreSQL** — the boring industry default, deepest docs, free hosted tiers. Rejected SQLite because hosting platforms can wipe files on redeploy and deployment is in the MVP. Runs locally during the build, hosted after deployment.
- **Database access: raw SQL with parameterized queries, plus** `psql` **in the terminal** — chosen over SQLAlchemy deliberately, because learning SQL is the point and an ORM would hide it. Parameterized queries (never string concatenation) are the standing habit that prevents SQL injection.
- **Charting: Recharts** — React-native charting, most beginner-friendly in this ecosystem. Low-stakes and swappable.
- **Hosting: shape locked, providers chosen during section 7** — three homes: a static frontend, a running backend, a hosted database. Providers are deferred because free-tier terms change; the learner will read the limits themselves rather than trust a stale recommendation.
- **Chart data: reuse the existing runs endpoint to start** — split into a dedicated chart endpoint only if the 5km filtering pushes back. A decision to make from evidence rather than up front.

## Sections

### 1. Foundations and the first page \[x\] done

**Deliverable:** a git repo on GitHub, and a React page running locally that says something the learner wrote. **Concepts:** git-basics, commits, github, gitignore, node-and-npm, vite, react-components, jsx, typescript-basics

- [x] Initialize a git repository and make your first commit

- [x] Create a GitHub repo and push your code there

- [x] Scaffold a React + TypeScript app with Vite

- [x] Run the dev server and see the default page in your browser

- [x] Edit the page to say something you wrote, and see it update live

- [x] Commit and push the frontend scaffold

### 2. A backend that answers \[ \] not started

**Deliverable:** a FastAPI server running locally, with an endpoint that can be hit from its auto-generated docs page and returns fake run data. **Concepts:** http-requests-and-responses, endpoints-and-routes, json, virtual-environments, fastapi-basics, auto-docs-page

- [x] Make a `backend/` folder with its own Python virtual environment, and activate it

- [x] Install FastAPI and uvicorn into the venv, and record them in `requirements.txt`

- [x] Write a minimal FastAPI app with one root endpoint, run it, and see its JSON in the browser

- [x] Open the auto-generated `/docs` page and call the endpoint from there

- [x] Add a `/runs` endpoint that returns a hardcoded list of fake runs, and test it from `/docs`

- [x] Commit the backend

### 3. The two halves talk \[ \] not started

**Deliverable:** the React page displaying that fake run data, fetched live from the backend. **Concepts:** fetch, async-await, cors, react-state, useeffect, loading-and-error-states

- [x] Add CORS middleware to the FastAPI backend so the browser is allowed to call it from a different origin

- [x] Add React state for the list of runs and a loading flag

- [x] Write a `useEffect` that fetches `/runs` on page load and stores the result in state

- [x] Render the fetched runs as a simple list on the page

- [x] Add an error state for when the fetch fails, and display it

- [ ] Commit the frontend fetch work

### 4. Remembering things \[ \] not started

**Deliverable:** runs and lifting sets stored in Postgres locally, surviving restarts, visible in the page. **Concepts:** postgres-setup, psql, tables-and-schemas, sql-select, sql-insert, parameterized-queries, database-connections, env-and-environment-variables

### 5. Strava \[ \] not started

**Deliverable:** click "Connect Strava," approve it, and real runs appear in the list. **Concepts:** what-is-an-api, api-keys-and-secrets, oauth-flow, access-and-refresh-tokens, calling-an-external-api, storing-tokens-safely, syncing-and-deduplication, git-branches, pull-requests

_Workflow note: this section runs on a `strava` feature branch off `main`, pushed to GitHub, and merged back with a pull request — the biggest, most breakable part of the project is the right place to learn branching for real._

### 6. The features you came for \[ \] not started

**Deliverable:** the pace chart drawn from real runs, and a working form for logging lifting sets. **Concepts:** recharts, filtering-data, react-forms, post-requests, input-validation, computing-derived-values

_Parked (optional, added 2026-09-02): add in-memory response caching to the chart endpoint — a dict of `key → (result, timestamp)` with a TTL check. Learn the expiry-and-invalidation logic; Redis is deferred until there's more than one backend process to share the cache._

### 7. Live on the internet \[ \] not started

**Deliverable:** the URL open on a phone at the gym, laptop closed. **Concepts:** hosted-postgres, deploying-a-backend, deploying-a-static-frontend, production-environment-variables, production-vs-development-config, reading-free-tier-limits

_Parked (optional, added 2026-09-02): add a basic in-memory rate limiter to the backend's own endpoints — a dict of `client → (tokens_left, last_refill)` implementing the token-bucket algorithm. Learn the refill math; the distributed (Redis) version waits until there's a real multi-server reason for it._

## Shape of the journey

Sections 1–3 produce a working shell quickly. 4–5 are the substantial ones. 6 is the payoff the project was chosen for. 7 is the part the old Discord bot never had.