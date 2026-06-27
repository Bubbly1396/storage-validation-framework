class Disk:
    def __init__(self, ssh):
        self.ssh = ssh
        
    def get_disk_health(self, disk):
        cmd = f"smartctl -H {disk}"
        return self.ssh.execute(cmd)