import yaml
import logging

# Set up logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 1: Read config.yaml
try:
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        logging.info("Config loaded successfully.")
except FileNotFoundError:
    logging.error("config.yaml not found.")
    print("ERROR: config.yaml not found.")
    exit(1)  # Exit the program if config is missing

# 2: Print connection string
db = config.get('database', {})
host = db.get('host')
port = db.get('port')
user = db.get('user')

connection_string = f"Connecting to {host}:{port} as {user}"
print(connection_string)
