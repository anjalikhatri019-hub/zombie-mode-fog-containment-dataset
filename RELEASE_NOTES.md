# ZOMBIE MODE dataset v1.0.3

Original creator-owned synthetic sensor corpus for **ZOMBIE MODE: Fog of Containment**. This release is the canonical participant-safe Source URL for the dataset.

Asset: `zombie_mode_public.zip` — 269,233,438 bytes — SHA-256 `6acc4c9e490d9e8dc4565647f3892b9d2b7ccbac38490aeea5ac6a3cb1e6ca7b`.

Inside the asset: `train.csv` (384 cases), `test.csv` (128 cases), `sample_submission.csv`, 512 `sensors/<case_id>.npy` arrays, `DATASET_CARD.md`, and `task_prompt.txt`. Arrays are `(8,64,64,8)` uint16. Training CSV includes realized payoffs; held-out CSV does not. See the repository [dataset card](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/DATASET_CARD.md), [member hashes](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/provenance_manifest.json), and [verifier](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/blob/main/verify_release.py).

Source type: original synthetic simulation, no upstream observations. Dataset licence: [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Intended use: benchmark temporal inference and ordered deployment under fictional sensor noise. No public-health validity claim.

The platform organizer ingestion ZIP contains one additional `answers_private.csv` file. Prepare writes it to the platform private directory; the public release ZIP has the 517 participant files listed above. The organizer archive, private test answers, generator, and seed-index manifest are **not** published here. The platform provides prepared public files; no network lookup is needed to solve the challenge.

Relative to v1.0.2, only `task_prompt.txt` and the canonical Source URL in `DATASET_CARD.md` changed inside the public ZIP. Observations, CSV rows, and private answer values are byte-identical. The challenge prompt is newly organized into research-style sections and the same public scoring contract. Official checks on this exact release are pending.
