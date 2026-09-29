# For the AI assistant helping a Team 09 member

You are helping **one** member of Team 09 finish their Sprint 2 work on the
**Sports Venue Booking System** (course project `SE-FDA-NEU/G9_AI66A_SE`).

## What to do
1. Ask the user which member they are (name or GitHub handle) and match the table in `README.md`.
2. Open that member's folder `g9-<name>/START-HERE.md` and read it fully.
   (If you only see the zip `g9-<name>.zip`, unzip it first.)
3. For each issue listed there, open its `GUIDE.md` and follow the steps **in order** —
   the GUIDE has the exact `git` / commit / PR commands to run.
4. Also do the **reviews** listed in `START-HERE.md` (open the teammate's PR, leave a real
   English comment on a specific line, then **Approve**).

## Rules — do not break these
- The member works under **their own GitHub account only**. Never use another person's
  SSH key or token; never commit or open PRs as someone else.
- Everything pushed to GitHub is in **English**: branch names, commit messages (subject
  **and** body), PR title and body, code, and comments.
- **One issue = one branch = one pull request.** Branch name: `<issue-number>-<english-slug>`
  (no `feature/` or `chore/` prefix).
- Commit and PR text must contain **no AI-tool attribution** (no `Co-Authored-By`,
  no "Generated with ...", no tool name). Fill the PR template's author line neutrally,
  e.g. `AI assistant used for <what>`.
- To do the work, clone the real project separately:
  `git clone https://github.com/SE-FDA-NEU/G9_AI66A_SE` — each GUIDE says where files go.

## Order of work (dependencies)
`#43 → #44 → #45` must merge in that order (the walking skeleton needs the Flask skeleton
and the seeded database first). `#46` and `#47` can start right away. `#49` waits for `#47`;
`#50` and `#51` are last.
