# ZOMBIE MODE: Fog of Containment dataset

Canonical participant-safe source for the original fictional ZOMBIE MODE benchmark, release **v1.0.2**. The release asset is `zombie_mode_public.zip` (269,230,266 bytes; SHA-256 `bb4f60b58b4f283b4be378328fd12cc8a859428be7d00afe1d2335174d5e7e22`). Download it from the [v1.0.2 release page](https://github.com/anjalikhatri019-hub/zombie-mode-fog-containment-dataset/releases/tag/v1.0.2).

The ZIP contains 384 labeled training cases, 128 held-out cases, a sample submission, 512 temporal sensor arrays, a dataset card, and the challenge prompt. Its exact member inventory and SHA-256 hashes are in [`provenance_manifest.json`](provenance_manifest.json). The public `verify_release.py` checks the downloaded archive and every member. The [dataset card](DATASET_CARD.md) describes columns, arrays, units, split, limitations, and intended use.

All observations and labels are creator-owned synthetic data. No external dataset or real human/outbreak data were collected. The dataset is dedicated under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/); see [`LICENSE_DATA.md`](LICENSE_DATA.md). The fictional response model has no public-health validity claim.

This page is a provenance and reproducibility mirror. The challenge platform supplies prepared public train/test/sample files to participants. The organizer ingestion archive, private held-out answers, generator, and seed-index manifest are intentionally **not** published here. The public archive does not contain private test payoff fields.

This v1.0.2 patch changes only the public `DATASET_CARD.md` member from v1.0.1. It explicitly inventories the private answer CSV in the organizer upload and its `private_dir` destination. Sensor arrays, train/test CSVs, sample submission, and private answers remain byte-identical. The local Prepare script also removes a stale answer file from a reused public output directory; that script is supplied through the challenge upload, not this public dataset. Official challenge acceptance and agent difficulty are not claimed by this release.
