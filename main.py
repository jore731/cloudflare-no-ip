import json

from src.assignIP import update_ips
import logging

logging.getLogger().setLevel(logging.INFO)
with open('/var/config/config.json', 'r') as file:
    configs = json.load(file)


def main():
    logging.info("Executting...")
    for config in configs:
        update_ips(config['urls'], config['email'], config['api_key'], config['zone_id'])


if __name__ == "__main__":
    main()
