class FioRunner:

    def __init__(self, ssh):
        self.ssh = ssh

    def run_fio(self):

        cmd = """
        fio --name=test --rw=read --bs=4k --filename=/dev/sda  --runtime=30s \
            --iodepth=32 \
            --ioengine=libaio
        """

        return self.ssh.execute(cmd)