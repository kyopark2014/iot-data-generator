# IoT Data Generator 

AWS TwinMaker를 통해서 digital twin을 만들다보면, 데이터 시뮬레이터가 필요할 수 있습니다. 여기서는 Data Simuator에 대해 소개합니다. 

## Prerequisition

#### IoT Core Endpoint

[IoT Core Endpoint](https://github.com/kyopark2014/IoT-Core-Contents/blob/main/endpoint.md)을 참조하여, 자신의 IoT Endpoint URL을 확인합니다. 

아래는 aws cli를 통해 확인하는 방법입니다. 

```java
$ aws iot describe-endpoint --endpoint-type iot:Data-ATS
```
