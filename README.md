# IoT Data Generator 

AWS TwinMaker를 통해서 digital twin을 만들다보면, 데이터 시뮬레이터가 필요할 수 있습니다. 여기서는 Data Simuator에 대해 소개합니다. 

## Prerequisite

[Prerequisite](https://github.com/kyopark2014/iot-data-generator/blob/main/prerequisite.md)에 따라 실행할 준비를 합니다.
 
## Data Generator를 Thing으로 등록

[Data Generator](https://github.com/kyopark2014/iot-data-generator/blob/main/registration.md)을 참조하여, Thing으로 등록합니다.

해당 폴더에는 TLS 인증과 관련된 "data-generator.cert.pem", "data-generator.private.key", "root-CA.crt"을 확인 할 수 있습니다. 

## 소스 다운로드

아래와 같이 [github](https://github.com/kyopark2014/iot-data-generator)에서 소스를 다운르도 한후 data-generator이름의 폴더로 이동합니다.

```
$ git clone https://github.com/kyopark2014/iot-data-generator
$ cd data-generator
$ mkdir certs
$ cd certs
```

Data Generator를 Thigs로 등록후 생성된 "data-generator.cert.pem", "data-generator.private.key", "root-CA.crt"을 certs 폴더에 복사합니다. 

## Data Generator 소스 수정하기 

1) Visual Studio Code와 같은 툴을 이용하여 "lib/simulator_config.py"을 오픈합니다.

2) "endpoint"에 [Prerequisite](https://github.com/kyopark2014/iot-data-generator/blob/main/prerequisite.md)에서 확인한 endpoint를 입력합니다.

3) 아래와 같이 cert, key, root_ca을 업데이트 합니다.


```java
    endpoint = "samplel34rul5-ats.iot.us-east-1.amazonaws.com"
    cert = "./certs/data-generator.cert.pem"
    key = "./data-generator.private.key"
    root_ca = "./certs/root-CA.crt"
```    

## Data Generator Policy 수정하기

[Data Generator Policy 수정하기](https://github.com/kyopark2014/iot-data-generator/blob/main/policy.md)을 따라 Polcy가 "Data Generator"로 부터 들어오는 MQTT request를 allow 하도록 수정합니다. 

