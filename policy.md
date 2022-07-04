# Data Generator Policy 수정하기

1) 아래와 같이 [AWS IoT] - [Security] - [Policies]에서 "data-generator-Policy"를 선택합니다. 

https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/policyhub

![noname](https://user-images.githubusercontent.com/52392004/177150450-c142142f-0e60-414c-a6f8-369b4134b4d6.png)

2) 상단의 [Edit active version]을 선택하고, [Json]을 선택한 후에, 아래와 같이 수정합니다. 이때 아래의 "123456789012"일때 account id로 입력합니다. 아래처럼 수정하면 들어오는 topic이나 resource에 제한을 걸수 없어서 일반적인 IoT Device에서 아래처럼 수정하지 않도록 주의바랍니다. 다만, Data Generator는 테스트를 위해 생성한 thing이므로 편의상 아래처럼 설정하였습니다. 

```java
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish",
        "iot:Receive",
        "iot:RetainPublish"
      ],
      "Resource": [
        "arn:aws:iot:us-east-1:123456789012:topic/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": [
        "arn:aws:iot:us-east-1:123456789012:topicfilter/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": "arn:aws:iot:us-east-1:123456789012:client/*"
    }
  ]
}
```

account id는 아래 명령어로 확인 할 수 있습니다.

```c
$ aws sts get-caller-identity --query Account --output text
```

3) Policy를 업데이트 한후에 아래처럼 새로운 버전을 Active로 변경하여야 사용할 수 있습니다. 

![noname](https://user-images.githubusercontent.com/52392004/177152772-acc63cc1-0f02-455f-bfde-cf7d56fe1db9.png)
