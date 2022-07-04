###############################################################################
# Simulator.py
#
# Start and manage enabled DataSource instances
#
# Chris Green greenzcg@amazon.com
###############################################################################

from lib.config_manager import ConfigManager
from lib.data_publisher import DataPublisher
import time
import threading
import random
from lib.simulator_config import AppConfig
from lib.data_generator import DataGenerator, shapes

class Simulator:

    endpoint = AppConfig.endpoint
    cert = AppConfig.cert
    key = AppConfig.key
    root_ca = AppConfig.root_ca
    client_id = AppConfig.client_id

    topic = AppConfig.topic

    scan_interval = AppConfig.scan_interval # seconds

    dp = None
    cm = None
    dg = None

    def __init__(self):
        self.cm = ConfigManager()
        self.dp = DataPublisher(endpoint=self.endpoint, client_id=self.client_id, root_ca=self.root_ca, cert=self.cert, key=self.key)
        self.dg = DataGenerator()

    def start(self):
        # Just diagnostic
        print(time.ctime())
        self.publish_enabled_sources()
        threading.Timer(self.scan_interval, self.start).start()

    def build_payload(self, source):
        # build a json payload like this
        # {
        # "alias": "motor/1/rpm",
        # "ts": 1645414022,
        # "value": random(min, max) +/- random(max_delta)
        # }
        msg = None
        t = source['type']
        value = 0
        boolValue = False

        msg = None

        if t == "Double" or t == "Integer":
            # compute the new value based on the current value within the min/max settings and no more
            # than the delta setting
            last_value = int(source['last_value'])
            delta = random.randrange(int(source['max_delta']))
            sign = random.choice([-1,1])
            delta = delta * sign
            shape = shapes.JITTER # The default unless a shape is specified in the config
            if 'shape' in source.keys():
                if source['shape'] == "TRIANGLE": shape = shapes.TRIANGLE
                elif source['shape'] == "RAMPUP": shape = shapes.RAMPUP
                elif source['shape'] == "RAMPDOWN": shape = shapes.RAMPDOWN
                elif source['shape'] == "PWM25PC": shape = shapes.PWM25PC
                elif source['shape'] == "PWM50PC": shape = shapes.PWM50PC
                elif source['shape'] == "PWM75PC": shape = shapes.PWM75PC
            new_value = self.dg.nextValueFrom(last_value, delta, shape, int(source['max']), int(source['min']))
            # new_value = last_value + delta
            # if new_value > int(source['max']):
            #     new_value = int(source['max'])
            # if new_value < int(source['min']):
            #     new_value = int(source['min'])
            msg = {
                "alias": source['alias'],
                "ts": int(time.time()),
                "value": new_value
                }
            self.cm.update_last_value(name=source['name'], last_value=new_value)
            print(time.ctime() + " " + source['name'] + " last value = " + str(last_value) + " new value = " + str(new_value))

        elif t == "Boolean":
            # generate a random boolean with a bias for True
            if random.randrange(0,100) > 25:
                msg = {
                    "alias": source['alias'],
                    "ts": int(time.time()),
                    "value": True
                    }
            else:
                msg = {
                    "alias": source['alias'],
                    "ts": int(time.time()),
                    "value": False
                    }
        return msg

    def publish_enabled_sources(self):
        enabled_sources = self.cm.get_configs()
        for source in enabled_sources:
            # If now - source last published time >= interval then publish
            if int(time.time()) - int(source['last_pub']) >= source['frequency']:
                # Prepare payload for publish
                message=self.build_payload(source)
                # use the default topic in the config unless a topic has been
                # specified in the source JSON
                topic=self.topic
                if 'topic' in source:
                    topic=source['topic']
                self.dp.publish(topic, payload=message)
                self.cm.update_last_pub(name=source['name'], last_pub=int(time.time()) )
            # else:
            #     print(source['name'] + " still has " + str(int(source['last_pub']) + int(source['frequency']) - int(time.time())) + " seconds to wait")

################################################################################
# The main main()
################################################################################
if __name__ == '__main__':
    sim = Simulator()
    sim.start()
