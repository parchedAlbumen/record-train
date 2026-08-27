# File map

## /

- learning/project.md — known (2026-08-20) — the project, its MVP, and the trunk
- learning/plan.md — known (2026-08-20) — the build plan and the locked decisions
- learning/knowledge-graph.md — known (2026-08-20) — the living map of what you actually know → \[\[writing-a-good-plan\]\]
- learning/file-map.md — known (2026-08-20) — this file: why every file in the repo exists
- .claude/ — parked (section 1) — configuration for the coding agent; sorted out when the git repo is set up → \[\[agent-memory-and-claude-md\]\]
- altitude-skills/ — parked (section 1) — the skills folder that came with this setup, not part of your app; we decide in section 1 whether it belongs in the repo → \[\[gitignore\]\]
- .gitignore — known (2026-08-21) — tells git which files to skip when snapshotting (currently: local Claude settings, `node_modules/`, build output, editor files) → \[\[gitignore\]\]
- package.json — known (2026-08-21) — the project's manifest: its name, its npm scripts (`dev`, `build`, `lint`), and its list of dependencies → \[\[node-and-npm\]\]
- package-lock.json — known (2026-08-21) — the exact installed version of every dependency, including sub-dependencies; auto-generated, never hand-edited → \[\[node-and-npm\]\]
- node_modules/ — known (2026-08-21) — the actual downloaded code for every dependency; generated, gitignored, rebuildable anytime with `npm install` → \[\[node-and-npm\]\]
- src/ — known (2026-08-27) — where the actual React app code lives; `App.tsx` is the main component (now holds your own heading text), `main.tsx` boots it → \[\[react-components\]\] \[\[jsx\]\]
- index.html — known (2026-08-21) — the one HTML page the whole React app gets injected into → \[\[vite\]\]
- README.md — known (2026-08-21) — replaced Vite's boilerplate with a real one-line description of the project
- vite.config.ts — parked (section 1) — Vite's own configuration; not touched yet → \[\[vite\]\]
- tsconfig.json, tsconfig.app.json, tsconfig.node.json — parked (section 1) — TypeScript compiler settings; not touched yet → \[\[typescript-basics\]\]
- eslint.config.js — parked (section 1) — code-quality linter rules; not touched yet
- public/ — parked (section 1) — static files served as-is; not touched yet