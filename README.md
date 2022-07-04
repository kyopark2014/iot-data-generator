# IoT Data Generator 

AWS TwinMaker를 통해서 digital twin을 만들다보면, 데이터 시뮬레이터가 필요할 수 있습니다. 여기서는 Data Simuator에 대해 소개합니다. 

## 1) Prerequisite

[Prerequisite](https://github.com/kyopark2014/iot-data-generator/blob/main/prerequisite.md)에 따라 실행할 준비를 합니다.
 
## 2) Data Generator를 Thing으로 등록

[Data Generator](https://github.com/kyopark2014/iot-data-generator/blob/main/registration.md)을 참조하여, Thing으로 등록합니다.

해당 폴더에는 TLS 인증과 관련된 "data-generator.cert.pem", "data-generator.private.key", "root-CA.crt"을 확인 할 수 있습니다. 

## 3) 소스 다운로드 및 인증서 복사

아래와 같이 [github](https://github.com/kyopark2014/iot-data-generator)에서 소스를 다운르도 한후 data-generator이름의 폴더로 이동합니다.

```
$ git clone https://github.com/kyopark2014/iot-data-generator
$ cd data-generator
$ mkdir certs
$ cd certs
```

Data Generator를 Thing으로 등록후 생성된 "data-generator.cert.pem", "data-generator.private.key", "root-CA.crt"을 certs 폴더에 복사합니다. 

## 4) Data Generator 소스 수정하기 

아래와 같이 Data Generator의 TLS credential을 업데이트 합니다. 

1) Visual Studio Code와 같은 툴을 이용하여 "lib/simulator_config.py"을 오픈합니다.

2) "endpoint"에 [Prerequisite](https://github.com/kyopark2014/iot-data-generator/blob/main/prerequisite.md)에서 확인한 endpoint를 입력합니다.

3) 아래와 같이 cert, key, root_ca을 업데이트 합니다.


```java
    endpoint = "samplel34rul5-ats.iot.us-east-1.amazonaws.com"
    cert = "./certs/data-generator.cert.pem"
    key = "./certs/data-generator.private.key"
    root_ca = "./certs/root-CA.crt"
```    

## 5) Data Generator Policy 수정하기

[Data Generator Policy 수정하기](https://github.com/kyopark2014/iot-data-generator/blob/main/policy.md)을 따라 Polcy가 "Data Generator"로 부터 들어오는 MQTT request를 allow 하도록 수정합니다. 

## 6) Data Generator 실행하기 

정상적으로 실행되면 아래와 같이 5초 간격으로 IoT Sample 데이터가 생성되어서 MQTT로 IoT Core로 전달됩니다. 

```c
$ python3 simulator.py
Mon Jul  4 21:18:44 2022
Mon Jul  4 21:18:44 2022 Water rig OEE trigger last value = 8 new value = 9
Mon Jul  4 21:18:44 2022 Water rig Pump 3 RPM last value = 3000 new value = 3000.0
Mon Jul  4 21:18:44 2022 Water rig Pump 2 RPM last value = 2985 new value = 2985.0
Mon Jul  4 21:18:45 2022
Mon Jul  4 21:18:46 2022
Mon Jul  4 21:18:47 2022
Mon Jul  4 21:18:48 2022
Mon Jul  4 21:18:49 2022
Mon Jul  4 21:18:49 2022 Water rig OEE trigger last value = 9 new value = 10
Mon Jul  4 21:18:49 2022 Water rig Pump 3 RPM last value = 3000 new value = 3000.0
Mon Jul  4 21:18:49 2022 Water rig Pump 2 RPM last value = 2985 new value = 2985.4582583995502
Mon Jul  4 21:18:50 2022
Mon Jul  4 21:18:51 2022
Mon Jul  4 21:18:52 2022
Mon Jul  4 21:18:53 2022
Mon Jul  4 21:18:54 2022
Mon Jul  4 21:18:54 2022 Water rig OEE trigger last value = 10 new value = 9
Mon Jul  4 21:18:54 2022 Water rig Pump 3 RPM last value = 3000 new value = 3000
Mon Jul  4 21:18:54 2022 Water rig Pump 2 RPM last value = 2985 new value = 2985
```

## MQTT test client에서 동작 확인하기 

1) MQTT test client console로 이동합니다.

https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/test

2) 아래와 같이 [Subscribe to a topic]의 [Topic filter]를 "#"으로 입력하고 [Subscribe]를 선택하면, 아래와 같이 "sim/test"라는 topic으로 Data Generator가 data를 생성하여 전송하는것을 알 수 있습니다. 


![noname](https://user-images.githubusercontent.com/52392004/177160702-11a3506e-a89f-4648-af12-ba9b87e3f183.png)


