import os
import json

class ConfigManager:
    def __init__(self, root_path):
        self.root_path = root_path
        self.config = self._load_config()

    def get(self, key, default=None):
        return self.config.get(key, default)

    def get_ip_range(self):
        mode_info = self.config.get("netscanner").get("ip_range")
        return mode_info

    def get_port_range(self):
        port_range = self.config.get("netscanner").get("port_range")
        return port_range

    def _load_config(self):
        config_path = os.path.join(self.root_path, "networkscanner/config.json")
        with open(config_path, "r") as f:
            return json.load(f)