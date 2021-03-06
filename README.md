# IoT Data Generator를 이용하여 다양한 Data Source를 생성하고 Timestream과 Grafana를 이용하여 Dashboard 생성하기

AWS TwinMaker를 통해서 digital twin을 만드는 경우와 같이, 실제 IoT Sensor가 아닌 데이터 시뮬레이터를 통해 동작을 시험하여야 할 필요가 있습니다. 여기서는 IoT Data Generator에 대해 소개하고, Timestream으로 데이터를 모아서, Grafana로 보여주는 일련의 과정을 소개합니다. 전체적인 Architecture는 아래와 같습니다.

<img width="705" alt="image" src="https://user-images.githubusercontent.com/52392004/177564305-5af2a69a-a395-41d7-b3c3-c3e827d2cab9.png">

IoT Data를 IoT Core의 Rule을 통해 Timestream에 저장하는 인프라 생성 및 배포는 Console을 통해 구현하는 방법과 [AWS CDK](https://github.com/kyopark2014/technical-summary/blob/main/cdk-introduction.md)를 이용해 구현하는 방법을 각각 설명하고 있습니다. 처음에 IoT Service들에 익숙해질때가지는 Console을 이용하지만, 장기적으로 인프라를 관리하기 위해서는 AWS CDK와 같은 [IaC](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)툴을 사용하는것이 좋습니다. 

## IoT Data Generator

[IoT Data Generator](https://github.com/kyopark2014/iot-data-generator/tree/main/data-generator)는 IoT Data Generator의 Concept과 구조에 대해 설명합니다. IoT Data Generator는 Python으로 각종 IoT Data Souce를 생성하여, MQTT로 IoT Core로 보낼 수 있습니다. 이것은 실행중에 쉽게 add, remove, enable, disable, adjust/modify와 같은 작업을 수행할 수 있으며, 여러개의 Data Source를 각각의 설정 파일을 통해 쉽게 생성 할 수 있습니다. 

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

이때, IoT Core로 인입되는 json포멧의 데이터는 "sim/test"라는 Topic으로 인입되고, 포맷은 아래와 같습니다. 여기서 "value"가 Measure이고 "alias"는 Dimension에 해당합니다. 

```java
{
  "alias": "sage-5/DeviceSet/PLC_1/Memory/Pump3_Speed_RPM",
  "ts": 1657075869,
  "value": 35
}
```

2) [Timestram](https://github.com/kyopark2014/iot-data-generator/blob/main/timestream.md)을 따라 Timestream database와 Table을 생성합니다.

3) [IoT Rule설정](https://github.com/kyopark2014/iot-data-generator/blob/main/iot-rule.md)에 따라 IoT core로 들어오는 Data를 Timestream에 저장합니다. 

4) Timestream에 저장된 데이터를 Query해보기 위하여 [Query Editor Console](https://us-east-1.console.aws.amazon.com/timestream/home?region=us-east-1#query-editor:)로 접속합니다. 이때 Query문으로 "SELECT * FROM "DataGenerator"."IoTData" WHERE alias = 'sage-5/DeviceSet/PLC_1/Memory/Pump2_Speed_RPM' AND time between ago(15m) and now() ORDER BY time DESC LIMIT 10"라고 입력하고 [Run]을 하면 아래와 같이 IoT Data Generator가 생성하여 IoT Core로 인입되어, Timestream에 저장된 데이터를 확인 할 수 있습니다. 

![noname](https://user-images.githubusercontent.com/52392004/177549737-d3394fd4-9b08-4cb7-a028-badc9cc5a127.png)


## Grafana를 이용한 파형 확인

아래는 [Grafana 설정](https://github.com/kyopark2014/iot-data-generator/blob/main/grafana.md)를 이용하여 TRIANGLE, RAMPUP, PWM50PC와 같은 파형을 생성한 모습입니다. 

![image](https://user-images.githubusercontent.com/52392004/177568268-71026768-bc9f-4040-abe2-d127c80babb7.png)

## AWS CDK를 이용한 인프라 구축

인프라를 지속적으로 관리하기 위해서는 [AWS CDK](https://github.com/kyopark2014/technical-summary/blob/main/cdk-introduction.md)와 같은 [IaC](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)를 툴을 사용하여야 합니다.

[AWS CDK를 이용한 IoT 인프라 구축](https://github.com/kyopark2014/iot-data-generator/tree/main/cdk-timestream)에서는 IoT Core Rule과 Timestream을 정의하고 인프라를 배포합니다. 


## Reference

[Ingesting Data into Amazon Timestream with AWS IoT Core](https://www.youtube.com/watch?v=00Wersoz2Q4)

[aws-cdk-lib.aws_timestream module](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_timestream-readme.html)

[Amazon Timestream - grafana](https://grafana.com/grafana/plugins/grafana-timestream-datasource/)


[Visualizing Data in Amazon Timestream using Grafana](https://www.youtube.com/watch?v=pilkz645cs4&t=2s)

[Grafana - AWS](https://docs.aws.amazon.com/timestream/latest/developerguide/Grafana.html#Grafana.sample-app)
