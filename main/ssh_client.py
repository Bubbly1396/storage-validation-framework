import paramiko

from main.logger import Log

logger = Log.get_logger()

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
        logger.info(f"Executing command: {command}")

        stdin, stdout, stderr = self.client.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            logger.error(error)
        else:
            logger.info(output)

        return {
            "stdout" : output,
            "stderr" : error
        }
        
    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
        