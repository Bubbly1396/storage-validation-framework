import paramiko

class SSHClient:
    
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.client = None
        
    def connect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            self.client.connect(
                hostname=self.host,
                username=self.username,
                password=self.password
            )
            return self.client
        except Exception as e:
            print(f"connection failed {e}")
            return None

        
    def execute(self, command):
        if not self.client:
            raise Exception("SSHClient not connected")

        stdin, stdout, stderr = self.client.exec_command(command)
        
        return {
            "stdout" : stdout.read().decode(),
            "stderr" :  stderr.read().decode()
        }
        
    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
        