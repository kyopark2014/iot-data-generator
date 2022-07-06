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
