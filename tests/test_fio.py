import pytest
import re
import json

from utils.fio_utils import FioRunner


def test_fio_installed(ssh):

    result = ssh.execute("sudo fio --version")

    assert result['stderr'] == ""
    assert "fio" in result['stdout']

def test_fio_help(ssh):
    result = ssh.execute("sudo fio --help")

    assert result['stderr'] == ""


def test_fio_iops(ssh):
    fio = FioRunner(ssh)
    result = fio.run_fio()


    out = result['stdout'].strip()

    patt = r'IOPS=([\d.]+)([kKmM])?'

    match = re.search(patt, out)

    iops = float(match.group(1))
    suffix = match.group(2)

    if suffix.lower() == 'k':
        iops *= 1000
    elif suffix.lower() == 'm':
        iops *= 100000

    assert iops >= 10000, f"Expected iops > 100000, got {iops}"

@pytest.mark.skip(reason="Not implemented")
def test_fio_json(ssh):

    fio = FioRunner(ssh)

    result = fio.fio_json()

    output = ssh.execute("cat /home/basheer/fio.json")

    assert "jobs" in output

