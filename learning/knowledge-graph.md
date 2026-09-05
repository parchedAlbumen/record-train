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
- last-reviewed: 2026-09-01
- evidence: Correctly predicted `git status` would show everything as untracked right after `git init`; correctly reasoned that deleting `.git/` would leave working files untouched. 2026-09-01: correctly reasoned that an uncommitted-but-committed-locally change is lost forever if the machine dies before a push.

## commits

- status: practicing
- depends-on: git-basics
- introduced: 2026-08-21
- last-reviewed: 2026-09-04
- evidence: Ran `git add .` and `git commit` themselves, correctly predicted the commit confirmation output, and distinguished staged-but-uncommitted from committed. 2026-08-27: after 6 days, recalled unprompted that a commit only saves locally, and predicted "ahead by 1 commit" correctly. 2026-09-04: on review, first guessed an unpushed commit would be recoverable if the machine died; after working through the "no other copy exists" reasoning, correctly restated that a commit living only in local `.git/` is unrecoverable if that machine is destroyed before a push. Downgraded from understood — needs another clean pass before it's solid again.

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
- last-reviewed: 2026-09-01
- evidence: Read `git status` output correctly to identify `.claude/settings.local.json` as excluded; after a nudge, reasoned that it's excluded for being machine-specific, not just private. 2026-09-01: correctly reasoned that a future `.env` file would not be auto-ignored by the current patterns and would need to be added explicitly.

## node-and-npm

- status: practicing
- depends-on: none
- introduced: 2026-08-21
- last-reviewed: 2026-08-21
- evidence: Correctly explained that deleting `node_modules/` would break `npm run dev` and that `npm install` rebuilds it from `package.json`/`package-lock.json`. 2026-09-02: on review, recalled that the frontend breaks and that it's the React setup dependencies, but had lost the recovery command (`npm install`); refreshed.

## vite

- status: practicing
- depends-on: node-and-npm
- introduced: 2026-08-21
- last-reviewed: 2026-09-01
- evidence: Ran the scaffold and dev server themselves, correctly predicted a localhost page would open, and chose "ignore files and continue" correctly reasoning it would preserve `.git/` and `learning/`. 2026-09-01: correctly reasoned that Vite's dev server and FastAPI on different ports count as different origins to the browser.

## react-components

- status: introduced
- depends-on: vite
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Had `App` explained as a function that returns markup; no independent demonstration yet.

## jsx

- status: understood
- depends-on: react-components
- introduced: 2026-08-27
- last-reviewed: 2026-09-04
- evidence: Edited the `<h1>` in App.tsx and saw it update live; correctly predicted `{2 + 2}` renders `4` because the braces evaluate JavaScript. 2026-09-04: independently reasoned that `date` needed a `run.` prefix since it's a field on the loop variable, not a standalone variable; correctly predicted that quoted text outside curly braces (`" - "`) would render the literal quote characters, not act as a separator; then independently diagnosed and fixed a real syntax error (a stray brace left over from a merged TODO comment) after being shown only the browser's error, with no fix given.

## hmr

- status: introduced
- depends-on: vite
- introduced: 2026-08-27
- last-reviewed: 2026-08-27
- evidence: Observed the page repaint without a full reload right after saving an edit to App.tsx.

## typescript-basics

- status: introduced
- depends-on: none
- introduced: 2026-09-01
- last-reviewed: 2026-09-01
- evidence: Had the `Run` type explained (a type describes an object's required shape/fields); no independent demonstration yet.

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
- last-reviewed: 2026-09-01
- evidence: Given a two-route example, said `list_runs` runs 0 times at startup and only when a request hits `/runs` — separated route registration from per-request dispatch. 2026-09-01: wrote a working `/run` route from scratch unprompted, then reshaped it into `/runs` returning a list of dicts matching the requested shape.

## json

- status: practicing
- depends-on: http-requests-and-responses
- introduced: 2026-08-27
- last-reviewed: 2026-09-01
- evidence: Filled the endpoint's return dict; predicted the browser would show exactly `message: "hello everyone!"` and connected it to the Python-dict → JSON conversion. 2026-09-01: correctly filled a second dict into a list of dicts, matching key shape, which came back as a proper JSON array.

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

- status: practicing
- depends-on: fastapi-basics
- introduced: 2026-09-01
- last-reviewed: 2026-09-01
- evidence: Called `GET /` and `GET /runs` live from `/docs` via "Try it out"; correctly predicted that saving a new route with `--reload` running makes it appear on `/docs` automatically, no extra step, then confirmed it by writing `/run` and seeing it show up on refresh.

## fetch

- status: practicing
- depends-on: http-requests-and-responses, react-components
- introduced: 2026-09-02
- last-reviewed: 2026-09-02
- evidence: Wrote the `fetch(...)` call and both `await` lines themselves inside an async helper in `useEffect`; predicted a `runs` request at status 200 returning the array and confirmed it in the browser Network tab.

## async-await

- status: practicing
- depends-on: fetch
- introduced: 2026-09-02
- last-reviewed: 2026-09-02
- evidence: Explained that `await` pauses until the promise resolves and that without it `response` would be a promise with no `.json()` method; after a wrong first guess (that `.then()` "implicitly refers to" async/await), framed the two as separate syntaxes for consuming the same promise.

## cors

- status: practicing
- depends-on: fetch
- introduced: 2026-09-01
- last-reviewed: 2026-09-01
- evidence: Added `CORSMiddleware` with `allow_origins`; after a wrong first guess (bare port number, then a URL with a trailing slash), reasoned through string-equality themselves and landed on the exact origin string with no path; correctly predicted the `access-control-allow-origin` response header would appear, confirmed via curl.

## react-state

- status: practicing
- depends-on: react-components
- introduced: 2026-09-01
- last-reviewed: 2026-09-02
- evidence: Set `runs` to `[]` correctly on first try. Initially answered `loading`'s starting value backwards (reasoning "hasn't started = false"); after working through the "do we have data yet" vs "are we still waiting" distinction across several exchanges, correctly reasoned to `true` and named the underlying trap (answering an adjacent question, not the one the variable name asks) in their own words. 2026-09-02: distinguished the updater-function form `setCount((c) => c + 1)` (new value built from old) from the plain-value form `setRuns(data)` (value replaced wholesale) and picked the plain form correctly for the fetch.

## useeffect

- status: practicing
- depends-on: react-state
- introduced: 2026-09-02
- last-reviewed: 2026-09-04
- evidence: Predicted correctly that omitting the dependency array makes the effect run on every render, and reasoned it would loop given a `setRuns` inside; predicted the effect runs once on load and not when the count button is clicked; explained that `useEffect` sits above `return` because JSX is markup and hooks belong in the component's setup. 2026-09-04: after exploring why the fetch helper can't be passed to `useEffect` directly as an `async` function, correctly restated in own words that `useEffect`'s return slot must be `undefined` or a plain cleanup function, and that `async` functions always return a `Promise` instead, which is the actual source of the restriction (not a general ban on async arrow functions). Also reasoned correctly that moving the helper outside the component entirely would break its access to `setRuns` via closure (asked but not yet confirmed by them running it).

## callbacks

- status: practicing
- depends-on: none
- introduced: 2026-09-02
- last-reviewed: 2026-09-02
- evidence: After a long stretch of genuine confusion, articulated in own words that a function passed into another function has its parameters filled positionally by the caller; concluded that a state updater's first parameter is the current state value purely because React is built to call it that way, not through any language mechanism. Linked to [[arrow-function-syntax]] and [[react-state]].

## arrow-function-syntax

- status: practicing
- depends-on: none
- introduced: 2026-09-02
- last-reviewed: 2026-09-02
- evidence: Named the left of `=>` as parameters and the right as the returned result; understood that a braced body needs an explicit `return` while a bare expression is returned implicitly.

## list-rendering

- status: practicing
- depends-on: jsx, react-state
- introduced: 2026-09-04
- last-reviewed: 2026-09-04
- evidence: Given the `.map()` + `key` skeleton, correctly filled in the `<li>` content using `run.date`/`run.distance_km`/`run.duration_min`; reasoned through why each field needs the `run.` prefix and why quoted separator text outside braces would render literally.

## loading-and-error-states

- status: practicing
- depends-on: react-state, fetch
- introduced: 2026-09-04
- last-reviewed: 2026-09-04
- evidence: Correctly predicted that a failed fetch with no error handling would fail silently (empty list, no visible sign anything broke). After the fix, correctly predicted the error message would appear when the backend was down, and that runs would reappear once it was restarted; both confirmed live in the browser.

## try-catch

- status: practicing
- depends-on: none
- introduced: 2026-09-04
- last-reviewed: 2026-09-04
- evidence: Recognized `try`/`catch` from prior exposure in other languages. Reasoned unprompted that `try`/`catch` (catching the error) and state (getting it into the UI) are two separate jobs — catching alone doesn't paint anything on screen.

## short-circuit-conditional-rendering

- status: practicing
- depends-on: arrow-function-syntax
- introduced: 2026-09-04
- last-reviewed: 2026-09-04
- evidence: Correctly reasoned that `a && b` stops immediately without evaluating `b` when `a` is falsy, and evaluates/returns `b` when `a` is truthy. Initially said the falsy branch becomes literal `false`; corrected after a nudge to see `&&` returns the original value (`null`), not a converted boolean.

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