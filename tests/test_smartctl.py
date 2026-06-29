import pytest

def test_smartctl_installed(ssh):

    result = ssh.execute("smartctl --version")

    assert "smartctl" in result['stdout']
    assert result['stderr'] == ""


@pytest.mark.skip(reason="SMART support is unavailable in vm")
def test_disk_health(ssh):

    result = ssh.execute("smartctl -H /dev/sda")

    assert result['stderr'] == ""
    assert "PASSED" in result['stdout']


@pytest.mark.skip(reason="SMART support is unavailable in vm")
def test_smart_enabled(ssh):

    result = ssh.execute("smartctl -i /dev/sda")

    assert "SMART support is: Enabled" in result['stdout']

def test_disk_info(ssh):

    result = ssh.execute('smartctl -i /dev/sda')

    assert "Model" in result['stdout']

def test_power_on_hours(ssh):

    result = ssh.execute('smartctl -A /dev/sda')

    assert "Power_On_Hours" in result['stdout']