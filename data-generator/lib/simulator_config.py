#
# Changes to this file require a restart
#
class AppConfig:

    # us-east-1 IDA configuration
    # endpoint = "a1ugybrd70xbxf-ats.iot.us-east-1.amazonaws.com"
    # cert = "./certs/6263808b729c6e118726d7b1e933369ef71345963dcee52bca4a16fc4580c27a-certificate.pem.crt"
    # key = "./certs/6263808b729c6e118726d7b1e933369ef71345963dcee52bca4a16fc4580c27a-private.pem.key"
    # root_ca = "./certs/AmazonRootCA1.pem"

    #client_id = "DeviceSimulator"

    # ap-southeast-2 SYD configuration
    endpoint = "anr3wll34rul5-ats.iot.us-east-1.amazonaws.com"
    cert = "./certs/data-generator.cert.pem"
    key = "./certs/data-generator.private.key"
    root_ca = "./certs/root-CA.crt"

    # client_id = "water-rig-sim"
    client_id = "room1temperature"


    topic = "sim/test" # Can be overridem in the configs/*.json files with the optional "topic:" element

    scan_interval = 1 # seconds

    config_dir = "./data_sources"
    config_file_exclusions = [config_dir+"/sample.json", config_dir+"/config-template.json"]
