# IoT Data Generator
A configurable, dynamically updatable, simulated data generator for AWS IoT Core.

Author: Chris Green (AWS)

Version: 0.1 alpha<br>

GitLab: https://gitlab.aws.dev/greenzcg/iot-data-generator.git<br>

----
## Concept
This is an attempt to break the habit of creating a new and unique quick data source script every time we need to generate some test data for IoT demonstrations or application development and testing. Instead, this application provides a framework where all you have to do is add or remove data source definitions (see example below) - even while the simulator is running - without having to write any code for the new data source. The basic principles are:
- One *.json configuration file per simulator data source
- The simulator runs continuously
- The simulator monitors data source files for changes (e.g. additions or  enabled --> disabled or frequency changes)
- Data source files can be added or removed or edited while the simulator is running and changes will take effect on the next scan (as defined in ```lib/simulator_config.py:scan_interval```)

## Architecture

![diagram](https://user-images.githubusercontent.com/52392004/177172997-d6af2ba4-641b-4999-9af7-bbf47ad56093.png)

## Pseudo Code
1. Read data source files and create generator records for each
2. Process generator records to determine whether or not to publish
3. Publish enabled and scheduled generated data to AWS IoT Core
4. Update generator record with the last published time
5. Loop 1 to 4 indefinitely

## Samples
- You can copy and paste data source ```*.json``` files from the ```samples``` directory to
the ```data_sources``` directory at any time to add or remove data sources or write
your own data source ```*.json``` file.

# Data Source Config Files
A data source configuration file can contain the following
```json
{
  "id": "717324-32487324648", # (optional) A UUID
  "clientId": "MyThingName",  # (optional) If not default specify IoT Thing name
  "enabled": true,            # To stop/start processing this data source
  "name": "Motor 1 RPM",      # Human readable
  "topic": "motor/1/rpm",     # (optional) MQTT topic to publish to otherwise use the default specified in lib/simulator_config.py:topic
  "alias": "motor/1/rpm",     # The alias used in SiteWise. This is used in the IoT Core Rule
  "type": "Double",           # Double, Integer, Boolean
  "shape": "TRIANGLE",        # (optional) string that defines the shape of the data. Supported shapes are JITTER, TRIANGLE, RAMPUP, RAMPDOWN, PWM25PC, PWM50PC, PWM75PC
  "frequency": 5,             # Publish a new value every x seconds
  "min": 0,                   # Floor value. Randoms lower than this will be set to this value
  "max": 100,                 # Ceiling value. Randoms higher than this will be set to this value
  "initial": 50,              # (not implemented) Start the data sequence with this value
  "max_delta": 5,             # Max +/- deviation for subsequent random values
  "last_pub": 1645397833,     # (system generated) Epoch timetsamp of the last pub time. This is used to calculate the next pub time
  "last_value": 24            # (system generated) The last value published. This is used as the basis for the next random value
}

```
## Sample waveform shapes from the DataGenerator

![sample_waveforms](https://user-images.githubusercontent.com/52392004/177173247-c5a5d986-112f-40b9-b590-02da0e716147.png)
