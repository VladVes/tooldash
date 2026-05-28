# AGENTS.md — tooldash

## Project structure

- `client/` — frontend (React 19 + Vite + Tailwind v4, JSX, no TS)
- `server/` — backend (single-file Python stdlib HTTP server)
- `.opencode/tools/` — custom OpenCode tools

## Commands (run from `client/`)

- `npm run dev` — Vite dev server (HMR)
- `npm run build` — production build into `client/dist/`
- `npm run lint` — ESLint (flat config)
- `npm run preview` — Vite preview server

## Server

- `python server/app.py` — serves `client/dist/` on port 3000
- No pip dependencies (stdlib only)
- For development use Vite dev server instead

## Notable
- If you see changes that you didn't make, ignore them.

