# tuxhe-engineer-practice

Public repo: unsolved exercises for the Tuxhe Engineer Shorts. Everything here is in English.

- Exercises are generated from the validated code in the private `editor-video-ai` repo with
  `scripts/export_practice.py`; never write or edit an exercise by hand here, and never commit a solution.
- One folder per video under `python/` (later `rust/`), named exactly like the video: `<ID>-<slug>`.
- `just check` is the gate: ruff, pyright, and that every test loads. Exercise tests fail until solved, so CI
  does not run them.
