# IoT Data Generator 

AWS TwinMaker를 통해서 digital twin을 만들다보면, 데이터 시뮬레이터가 필요할 수 있습니다. 여기서는 Data Simuator에 대해 소개합니다. 

## IoT Data Generator 설정

[IoT Data Generator 설정](https://github.com/kyopark2014/iot-data-generator/blob/main/setup.md)에서는 IoT Data Generator에 동작시키기 위한 환경을 설정하고 동작시험을 하는 방법에 대해 설명합니다. 


## Amazon Timestream으로 데이터 보내기

## Grafana를 이용해 Dashboard 생성하기

아래는 Grafana를 이용하여 TRIANGLE, RAMPUP, PWM50PC와 같은 파형을 생성한 모습입니다. 

![image](https://user-images.githubusercontent.com/52392004/177516478-b44595d5-6cdc-4b8a-83ef-d3b259c77972.png)


## Reference

[Ingesting Data into Amazon Timestream with AWS IoT Core](https://www.youtube.com/watch?v=00Wersoz2Q4)

[aws-cdk-lib.aws_timestream module](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_timestream-readme.html)

[Amazon Timestream - grafana](https://grafana.com/grafana/plugins/grafana-timestream-datasource/)


[Visualizing Data in Amazon Timestream using Grafana](https://www.youtube.com/watch?v=pilkz645cs4&t=2s)

[Grafana - AWS](https://docs.aws.amazon.com/timestream/latest/developerguide/Grafana.html#Grafana.sample-app)
