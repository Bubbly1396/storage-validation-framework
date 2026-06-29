import pytest

from utils import raid
from utils.raid import Raid

def test_mdadm_installed(ssh):

    result = ssh.execute("mdadm --version")

    print(result['stdout'])

    # assert "mdadm" in result['stdout']
    assert result['stdout'] == ""

def test_create_raid(ssh):

    raid = Raid(ssh)

    result = raid.create_raid1("/dev/md0","/dev/sda", "/dev/sdb")

    status = raid.raid_status("/dev/md0")

    assert "md0" in status['stdout']


def test_raid_status(ssh):

    raid = Raid(ssh)

    result = raid.raid_status("/dev/md0")

    assert "active" in result['stdout']

def test_raid_details(ssh):


    raid = Raid(ssh)

    result = raid.raid_detail("/dev/md0")

    assert "Raid Level : raid1" in result['stdout']

