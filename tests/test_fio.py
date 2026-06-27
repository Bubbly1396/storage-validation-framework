import re
from utils.fio_utils import FioRunner


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

def test_fio_throughput(ssh):
    fio = FioRunner(ssh)
    result = fio.run_fio()

    out = result['stdout'].strip()

    patt = r'BW=([\d.]+)\s*([KMG]i?B/s)'
    match = re.search(patt, out)
    speed = float(match.group(1))
    suffix = match.group(2)

    if suffix.startswith('Ki'):
        speed *= 1024
    elif suffix.startswith('Mi'):
        speed *= 1024**2
    elif suffix.startswith('Gi'):
        speed *= 1024**3

    assert speed >= 300

