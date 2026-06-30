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

    def fio_json(self):

        cmd = """
            fio --name=test --filename=/dev/sda --bs=4k --rw=randread \
            --runtime=30s --output-format=json --output=/home/basheer/fio.json"""

        return self.ssh.execute(cmd)