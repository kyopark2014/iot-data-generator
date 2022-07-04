###############################################################################
# config-manager.py
#
# Read and monitor configs for changes.
# Update config files with last update time
#
# Chris Green greenzcg@amazon.com
###############################################################################

import json
import glob
from lib.simulator_config import AppConfig

class ConfigManager:
    config_dir = AppConfig.config_dir
    configs = []
    config_file_exclusions = AppConfig.config_file_exclusions

    # This is the working list of enabled configs which is dynamically updated
    # for the life of the ConfigManager instance
    enabled_configs = []
    config_file_list = []

    def __init__(self):
        self.read_configs()

    def update_config_file_list(self):
        self.config_file_list = glob.glob(self.config_dir + "/*.json")

    def write_config(self, data):
        # Write the updated config record back to disk
        for file in self.config_file_list:
            if file in self.config_file_exclusions:
                continue
            x = open(file)
            try:
                file_data = json.load(x)
            except json.JSONDecodeError as e:
                print("Error decoding JSON for update in " + file + ". " + e.msg + " at line " + str(e.lineno) + " column " + str(e.colno) + ". Skipping.")
                continue
            if file_data['name'] == data['name']:
                with open(file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

    def read_configs(self):
        # read all of the files in the config directory and process each one
        self.update_config_file_list()
        self.configs = []

        for file in self.config_file_list:
            if file in self.config_file_exclusions:
                continue
            else:
                with open(file, 'r') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError as e:
                        print("Error decoding JSON in " + file + ". " + e.msg + " at line " + str(e.lineno) + " column " + str(e.colno) + ". Skipping.")
                        continue
                    self.configs.append(data)

    def update_last_pub(self, name, last_pub ):
        self.update_config_file_list()
        self.read_configs()
        for c in self.configs:
            if c['name'] == name:
                c['last_pub'] = int(last_pub)
                self.write_config(c)

    def update_last_value(self, name, last_value):
        self.update_config_file_list()
        self.read_configs()
        for c in self.configs:
            if c['name'] == name:
                c['last_value'] = int(last_value)
                self.write_config(c)

    def get_configs(self):
        # return the list of enabled configs
        self.enabled_configs = []
        self.read_configs()

        for c in self.configs:
            if c["enabled"] == True:
                self.enabled_configs.append(c)
        return self.enabled_configs

    def get_config(self, name):
        # return a specific config regardless of it's enabled state
        # if not found return null
        conf = None
        for c in self.configs:
            if c["name"] == name:
                conf = c
                break
        return conf

# Just for unit testing
if __name__ == '__main__':
    cm = ConfigManager()
    cm.read_configs()
    print("Enabled configs are: " + json.dumps(cm.get_configs(), indent = 2) )
    print("Getting \"valve 1\" results in " + json.dumps(cm.get_config("valve 1"), indent=2))
    print("Getting \"valve 10\" results in " + json.dumps(cm.get_config("valve 10"), indent=2))
