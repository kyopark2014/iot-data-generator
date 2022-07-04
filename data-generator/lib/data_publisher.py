###############################################################################
# data_publisher.py
#
# Start the DataPublisher connection and publish when called
#
# Chris Green greenzcg@amazon.com
###############################################################################

import boto3
import json
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder

class DataPublisher:

    def __init__(self, endpoint, client_id, root_ca, cert, key):
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        self.__mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint = endpoint,
            cert_filepath = cert,
            pri_key_filepath = key,
            client_bootstrap = client_bootstrap,
            ca_filepath = root_ca,
            client_id = client_id,
            clean_session = False,
            keep_alive_secs = 30)
        connect_future = self.__mqtt_connection.connect()
        connect_future.result()
        #print("Connected! {}".format(client_id))

    def publish(self, topic, payload):
        response = self.__mqtt_connection.publish(
            topic = topic,
            payload = json.dumps(payload),
            qos = mqtt.QoS.AT_MOST_ONCE # mqtt.QoS.AT_LEAST_ONCE
            )
        # Wait for the result if need to run synchrounously
        #print(response[0].result())




################################################################################
# This main is for unit testing only
################################################################################
if __name__ == '__main__':
    print("Created publisher")
    dp = DataPublisher(endpoint=endpoint, client_id="LoadGenerator", root_ca=root_ca, cert=cert, key=key)
    print("Called publish()")
    dp.publish(topic="sim/test", payload='{"msg": "Hello from the DataPublisher 1"}')
    dp.publish(topic="sim/test", payload='{"msg": "Hello from the DataPublisher 2"}')
    dp.publish(topic="sim/test", payload='{"msg": "Hello from the DataPublisher 3"}')
