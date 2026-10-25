# ZOMBIE MODE dataset v1.0.2

Original creator-owned synthetic sensor corpus for **ZOMBIE MODE: Fog of Containment**. This release is the canonical participant-safe Source URL for the dataset.

Asset: `zombie_mode_public.zip` — 269,230,266 bytes — SHA-256 `bb4f60b58b4f283b4be378328fd12cc8a859428be7d00afe1d2335174d5e7e22`.

Inside the asset: `train.csv` (384 cases), `test.csv` (128 cases), `sample_submission.csv`, 512 `sensors/<case_id>.npy` arrays, `DATASET_CARD.md`, and `task_prompt.txt`. Arrays are `(8,64,64,8)` uint16. Training CSV includes realized payoffs; held-out CSV does not. See the repository [dataset card](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/DATASET_CARD.md), [member hashes](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/provenance_manifest.json), and [verifier](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/verify_release.py).

Source type: original synthetic simulation, no upstream observations. Dataset licence: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Intended use: benchmark temporal inference and ordered deployment under fictional sensor noise. No public-health validity claim.

The platform organizer ingestion ZIP contains one additional `answers_private.csv` file. Prepare writes it to the platform private directory; the public release ZIP has the 517 participant files listed above. The organizer archive, private test answers, generator, and seed-index manifest are **not** published here. The platform provides prepared public files; no network lookup is needed to solve the challenge.

Only `DATASET_CARD.md` changed inside the public ZIP relative to v1.0.1. Observations and CSV rows are byte-identical. Official Dataset Quality revalidation is pending.
