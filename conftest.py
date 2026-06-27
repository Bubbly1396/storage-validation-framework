import pytest
import json

from main.ssh_client import SSHClient
from main.logger import Log

@pytest.fixture(scope="session")
def ssh():

    logger = Log.get_logger()
    
    with open("config/config.json") as f:
        data = json.load(f)
        
    client = SSHClient(
        data['host'],
        data['username'],
        data['password']
    )

    logger.info(f"SSH connection established to {data['host']}")

    client.connect()
    print("connected successfully")
    
    yield client
    logger.info("testing")
    
    client.disconnect()
    logger.info("SSH disconnected successfully")