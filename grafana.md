# Grafana 설정

Open Source인 Grafana를 이용하여 IoT Data Generator를 통해 생성된 데이터를 확인하고자 합니다.

## IAM Role

[Amazon Timestream - Grafana](https://grafana.com/grafana/plugins/grafana-timestream-datasource/)에 설명되어 있는것처럼 IAM user는 아래의 퍼미션을 가지고 있어야 합니다. 

```java
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["timestream:*"],
      "Resource": "*"
    }
  ]
}
```

## Grafana 설정

1) [Grafana Console](https://us-east-1.console.aws.amazon.com/grafana/home?region=us-east-1#/workspaces)로 진입하여, [Create workspace]를 선택합니다. 

2) 아래와 같이 [Workspace name]으로 "DataGenerator"를 입력하고, [Next]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177551522-018255de-6e3d-4751-b0af-b3b0c707017a.png)

3) 아래와 같이 [AWS Single Sign-On]을 설정하고, [Permission type]으로 [Service managed]를 선택한 후에 [Next]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177552309-c1de4218-e44e-411f-828a-8f3f9cb0eeec.png)

4) [Data source name]으로 "Amazon TimeStream"을 선택하고, [Next]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177552692-98be40bf-9944-484d-a9cf-fd2d89f5742b.png)

5) 이후, [Create workspace]를 선택합니다. 

6) 아래와 같이 [Workspace Console](https://us-east-1.console.aws.amazon.com/grafana/home?region=us-east-1#/workspaces)에서 "DataGenerator"를 선택힙니다. 

![noname](https://user-images.githubusercontent.com/52392004/177553232-c75e96d4-23a6-4599-88d6-22ffa5684bb4.png)

아래처럼 [Data sources]에서 [Configure in Grafana]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177553640-6725bcbe-abb1-4dc4-b122-cf5eba3ac42c.png)

이때 아래처럼 [Default region]으로 "US East(N. Virginia"를 선택한 후, "Add data source"를 선택하면, 아래처럼 "Amazon Timestream us-east-1"이 생성됩니다. 

![noname](https://user-images.githubusercontent.com/52392004/177554438-828f20a0-2c15-4e0a-8c92-4c8ed41435de.png)

[Go to settings]를 선택한 후에 아래처럼 [Database]로 "DataGenerator"를 선택하고, "Table"로 "IoTData"를 선택한 후에 [Measure]로 "value"를 선택합니다. 이후, [Save & test]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177555001-9661a6f0-0564-42ce-a7f1-df47f6727770.png)

7) 아래처럼 [+]를 선택하여 [New dashboard]를 이동후, [Add a new panel]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177555552-ce4ee887-cb41-4a71-a23a-e8e6eaf8c3ed.png)

8) 아래처럼 [Data source]를 선택하여, [Amazon Timestream us-east-1]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177557897-52504279-d407-4f36-8e9d-6658373eb405.png)

9) Query문으로 "SELECT * FROM "DataGenerator"."IoTData" WHERE alias = 'sage-5/DeviceSet/PLC_1/Memory/Pump1_Speed_RPM'"와 같이 입력후에, 아래처럼 [Title]을 "sage-5/DeviceSet/PLC_1/Memory/Pump1_Speed_RPM"라고 입력합니다. 이후 Appliy를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177557188-ee6c34f2-df0b-4fa2-bd31-96e2dd1e1605.png)

설정이 잘되면 아래처럼 IoT Data Generator가 생성한 파형을 확인 할 수 있습니다. 

![image](https://user-images.githubusercontent.com/52392004/177558544-e51ac8b9-ede7-406a-8300-46482fde4abd.png)

10) 마찬가지로 "sage-5/DeviceSet/PLC_1/Memory/Pump2_Speed_RPM"와 "sage-5/DeviceSet/PLC_1/Memory/Pump3_Speed_RPM"을 추가하고, 저장합니다. 



