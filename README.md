# IoT Data Generator 

AWS TwinMaker를 통해서 digital twin을 만드는 경우와 같이, 실제 IoT Sensor가 아닌 데이터 시뮬레이터를 통해 동작을 시험하여야 할 필요가 있습니다. 여기서는 IoT Data Generator에 대해 소개하고, Timestream으로 데이터를 모아서, Grafana로 보여주는 일련의 과정을 소개합니다.  


## IoT Data Generator

[IoT Data Generator](https://github.com/kyopark2014/iot-data-generator/tree/main/data-generator)는 IoT Data Generator의 Concept과 구조에 대해 설명합니다.

[IoT Data Generator 설정](https://github.com/kyopark2014/iot-data-generator/blob/main/setup.md)에서는 IoT Data Generator에 동작시키기 위한 환경을 설정하고 동작시험을 하는 방법에 대해 설명합니다. 

## Amazon Timestream으로 데이터 보내기

1) [IoT Data Generator](https://github.com/kyopark2014/iot-data-generator/blob/main/setup.md) 설정후에 아래처럼 Data를 생성하여 IoT Core로 전송합니다. 

```c
$ python3 simulator.py
Wed Jul  6 20:34:54 2022
Wed Jul  6 20:34:54 2022 Water rig Pump 3 RPM last value = 1 new value = 1
Wed Jul  6 20:34:54 2022 Water rig Pump 2 RPM last value = 48 new value = 49
Wed Jul  6 20:34:54 2022 Water rig Pump 1 RPM last value = 38 new value = 39
Wed Jul  6 20:34:55 2022
Wed Jul  6 20:34:55 2022 Water rig Pump 3 RPM last value = 1 new value = 1
Wed Jul  6 20:34:55 2022 Water rig Pump 2 RPM last value = 49 new value = 50
Wed Jul  6 20:34:55 2022 Water rig Pump 1 RPM last value = 39 new value = 40
Wed Jul  6 20:34:56 2022
```

이때, IoT Core로 인입되는 json포멧의 데이터는 "sim/test"라는 Topic으로 인입되고, 포맷은 아래와 같습니다. 여기서 "value"가 Meature이고 "alias"는 Dimension에 해당합니다. 

```java
{
  "alias": "sage-5/DeviceSet/PLC_1/Memory/Pump3_Speed_RPM",
  "ts": 1657075869,
  "value": 35
}
```

2) [Timestram](https://github.com/kyopark2014/iot-data-generator/blob/main/timestream.md)을 따라 Timestream database과 Table을 생성합니다.

3) [IoT Rule설정](https://github.com/kyopark2014/iot-data-generator/blob/main/iot-rule.md)에 따라 IoT core로 들어오는 Data를 Timestream에 저장합니다. 


## Grafana를 이용해 Dashboard 생성하기

아래는 Grafana를 이용하여 TRIANGLE, RAMPUP, PWM50PC와 같은 파형을 생성한 모습입니다. 

![image](https://user-images.githubusercontent.com/52392004/177516478-b44595d5-6cdc-4b8a-83ef-d3b259c77972.png)


## Reference

[Ingesting Data into Amazon Timestream with AWS IoT Core](https://www.youtube.com/watch?v=00Wersoz2Q4)

[aws-cdk-lib.aws_timestream module](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_timestream-readme.html)

[Amazon Timestream - grafana](https://grafana.com/grafana/plugins/grafana-timestream-datasource/)


[Visualizing Data in Amazon Timestream using Grafana](https://www.youtube.com/watch?v=pilkz645cs4&t=2s)

[Grafana - AWS](https://docs.aws.amazon.com/timestream/latest/developerguide/Grafana.html#Grafana.sample-app)
