# ZOMBIE MODE: Fog of Containment dataset

Canonical participant-safe source for the original fictional ZOMBIE MODE benchmark, release **v1.0.3**. The release asset is `zombie_mode_public.zip` (269,233,438 bytes; SHA-256 `6acc4c9e490d9e8dc4565647f3892b9d2b7ccbac38490aeea5ac6a3cb1e6ca7b`). Download it from the [v1.0.3 release page](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/releases/tag/v1.0.3).

The ZIP contains 384 labeled training cases, 128 held-out cases, a sample submission, 512 temporal sensor arrays, a dataset card, and the [challenge prompt](task_prompt.txt). Its exact member inventory and SHA-256 hashes are in [`provenance_manifest.json`](provenance_manifest.json). The public `verify_release.py` checks the downloaded archive and every member. The [dataset card](DATASET_CARD.md) describes columns, arrays, units, split, limitations, and intended use.

All observations and labels are creator-owned synthetic data. No external dataset or real human/outbreak data were collected. The dataset is dedicated under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/); see [`LICENSE_DATA.md`](LICENSE_DATA.md). The fictional response model has no public-health validity claim.

This page is a provenance and reproducibility mirror. The challenge platform supplies prepared public train/test/sample files to participants. The organizer ingestion archive, private held-out answers, generator, and seed-index manifest are intentionally **not** published here. The public archive does not contain private test payoff fields.

This v1.0.3 patch expands `task_prompt.txt` into a full challenge page with overview, research question, generalization, data, submission, evaluation, and restrictions. `DATASET_CARD.md` changes only its canonical source URL. Sensor arrays, train/test CSVs, sample submission, and private answers remain byte-identical to v1.0.2. The local Prepare and Grade scripts are unchanged. Official challenge acceptance and agent difficulty are not claimed by this release.
