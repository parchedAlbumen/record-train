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

### 1. Foundations and the first page \[ \] not started

**Deliverable:** a git repo on GitHub, and a React page running locally that says something the learner wrote. **Concepts:** git-basics, commits, github, gitignore, node-and-npm, vite, react-components, jsx, typescript-basics

- [ ] Initialize a git repository and make your first commit

- [ ] Create a GitHub repo and push your code there

- [ ] Scaffold a React + TypeScript app with Vite

- [ ] Run the dev server and see the default page in your browser

- [ ] Edit the page to say something you wrote, and see it update live

- [ ] Commit and push the frontend scaffold

### 2. A backend that answers \[ \] not started

**Deliverable:** a FastAPI server running locally, with an endpoint that can be hit from its auto-generated docs page and returns fake run data. **Concepts:** http-requests-and-responses, endpoints-and-routes, json, virtual-environments, fastapi-basics, auto-docs-page

### 3. The two halves talk \[ \] not started

**Deliverable:** the React page displaying that fake run data, fetched live from the backend. **Concepts:** fetch, async-await, cors, react-state, useeffect, loading-and-error-states

### 4. Remembering things \[ \] not started

**Deliverable:** runs and lifting sets stored in Postgres locally, surviving restarts, visible in the page. **Concepts:** postgres-setup, psql, tables-and-schemas, sql-select, sql-insert, parameterized-queries, database-connections, env-and-environment-variables

### 5. Strava \[ \] not started

**Deliverable:** click "Connect Strava," approve it, and real runs appear in the list. **Concepts:** what-is-an-api, api-keys-and-secrets, oauth-flow, access-and-refresh-tokens, calling-an-external-api, storing-tokens-safely, syncing-and-deduplication

### 6. The features you came for \[ \] not started

**Deliverable:** the pace chart drawn from real runs, and a working form for logging lifting sets. **Concepts:** recharts, filtering-data, react-forms, post-requests, input-validation, computing-derived-values

### 7. Live on the internet \[ \] not started

**Deliverable:** the URL open on a phone at the gym, laptop closed. **Concepts:** hosted-postgres, deploying-a-backend, deploying-a-static-frontend, production-environment-variables, production-vs-development-config, reading-free-tier-limits

## Shape of the journey

Sections 1–3 produce a working shell quickly. 4–5 are the substantial ones. 6 is the payoff the project was chosen for. 7 is the part the old Discord bot never had.