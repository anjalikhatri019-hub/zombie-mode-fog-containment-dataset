# ZOMBIE MODE dataset v1.0.1

Original creator-owned synthetic sensor corpus for **ZOMBIE MODE: Fog of Containment**. This release is the canonical participant-safe Source URL for the dataset.

Asset: `zombie_mode_public.zip` — 269,229,943 bytes — SHA-256 `6d95b76335e7ad6d8855aaab49d14aa3d3781b7749c33e1256bb11cb768d6ca2`.

Inside the asset: `train.csv` (384 cases), `test.csv` (128 cases), `sample_submission.csv`, 512 `sensors/<case_id>.npy` arrays, `DATASET_CARD.md`, and `task_prompt.txt`. Arrays are `(8,64,64,8)` uint16. Training CSV includes realized payoffs; held-out CSV does not. See the repository [dataset card](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/DATASET_CARD.md), [member hashes](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/provenance_manifest.json), and [verifier](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/verify_release.py).

Source type: original synthetic simulation, no upstream observations. Dataset licence: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Intended use: benchmark temporal inference and ordered deployment under fictional sensor noise. No public-health validity claim.

The platform organizer ingestion ZIP, private test answers, generator, and seed-index manifest are **not** part of this public release. The platform provides prepared public files; no network lookup is needed to solve the challenge.
