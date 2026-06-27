from storage.disk import Disk

def test_disk_health(ssh):
    disk = Disk(ssh)
    output = disk.get_disk_health("/dev/sda")
    
    assert "linux" in output['stdout']