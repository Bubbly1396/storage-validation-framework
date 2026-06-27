import pytest

def test_ssh_connection(ssh):
    result = ssh.execute("uptime")
    assert result['stderr'] == ""
    
def test_drive_detection(ssh):
    result = ssh.execute('lsblk')
    assert 'sda' in result['stdout']
    print("sda in output")