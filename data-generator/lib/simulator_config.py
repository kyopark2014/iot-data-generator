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
    endpoint = "a1ugybrd70xbxf-ats.iot.ap-southeast-2.amazonaws.com"
    cert = "./certs/1aced057decd2d5acf93933e14d7e4e805617d1e8ad5fb57b4a162d271e20660-certificate.pem.crt"
    key = "./certs/1aced057decd2d5acf93933e14d7e4e805617d1e8ad5fb57b4a162d271e20660-private.pem.key"
    root_ca = "./certs/AmazonRootCA1.pem"

    client_id = "water-rig-sim"

    topic = "sim/test" # Can be overridem in the configs/*.json files with the optional "topic:" element

    scan_interval = 1 # seconds

    config_dir = "./data_sources"
    config_file_exclusions = [config_dir+"/sample.json", config_dir+"/config-template.json"]
