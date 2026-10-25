"""Verify participant-safe v1.0.1 asset and every ZIP member. MIT licensed."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main(asset):
    expected = json.loads(Path(__file__).with_name('provenance_manifest.json').read_text())
    path = Path(asset)
    assert path.stat().st_size == expected['asset']['bytes']
    with path.open('rb') as f:
        assert hashlib.file_digest(f, 'sha256').hexdigest() == expected['asset']['sha256']
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == set(expected['members'])
        for name, item in expected['members'].items():
            data = z.read(name)
            assert len(data) == item['bytes'] and sha256(data) == item['sha256'], name
    print('Verified asset and', len(expected['members']), 'members')


if __name__ == '__main__':
    main(sys.argv[1])
