class Raid:

    def __init__(self, ssh):
        self.ssh = ssh

    def create_raid1(self, md_device, disk1, disk2):

        cmd = f"sudo mdadm --create {md_device} --level=1 --raid-devices=2 {disk1} {disk2}"
        return self.ssh.execute(cmd)

    def stop_raid(self, md_device):

        cmd = f"sudo mdadm --stop {md_device}"

        return self.ssh.execute(cmd)

    def remove_raid(self, md_device):

        cmd = f"sudo mdadm --remove {md_device}"

        return self.ssh.execute(cmd)

    def raid_status(self, md_device):

        cmd = f"sudo cat /proc/mdstat"

        return self.ssh.execute(cmd)

    def raid_detail(self, md_device):

        cmd = f"sudo mdadm --detail {md_device}"

        return self.ssh.execute(cmd)