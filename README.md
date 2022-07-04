# IoT Data Generator 

AWS TwinMaker를 통해서 digital twin을 만들다보면, 데이터 시뮬레이터가 필요할 수 있습니다. 여기서는 Data Simuator에 대해 소개합니다. 

## Prerequisite

#### IoT Core Endpoint

[IoT Core Endpoint](https://github.com/kyopark2014/IoT-Core-Contents/blob/main/endpoint.md)을 참조하여, 자신의 IoT Endpoint URL을 확인합니다. 

아래는 aws cli를 통해 확인하는 방법입니다. 

```java
$ aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

#### libarary 설치


AWS IoT Device SDK v2 for Python


```c
$ python -m pip install boto3
Collecting boto3
  Downloading boto3-1.24.22-py3-none-any.whl (132 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 132.5/132.5 KB 374.7 kB/s eta 0:00:00
Collecting jmespath<2.0.0,>=0.7.1
  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting botocore<1.28.0,>=1.27.22
  Downloading botocore-1.27.22-py3-none-any.whl (8.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 5.5 MB/s eta 0:00:00
Collecting s3transfer<0.7.0,>=0.6.0
  Downloading s3transfer-0.6.0-py3-none-any.whl (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.6/79.6 KB 2.7 MB/s eta 0:00:00
Collecting urllib3<1.27,>=1.25.4
  Using cached urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
Collecting python-dateutil<3.0.0,>=2.1
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: urllib3, six, jmespath, python-dateutil, botocore, s3transfer, boto3
Successfully installed boto3-1.24.22 botocore-1.27.22 jmespath-1.0.1 python-dateutil-2.8.2 s3transfer-0.6.0 six-1.16.0 urllib3-1.26.9
```

```c
$ python3 -m pip install awscrt
Collecting awscrt
  Downloading awscrt-0.13.13-cp39-cp39-macosx_10_9_universal2.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 1.5 MB/s eta 0:00:00
Installing collected packages: awscrt
Successfully installed awscrt-0.13.13
```

```c
$ python3 -m pip install awsiot
Collecting awsiot
  Downloading awsiot-0.1.3-py3-none-any.whl (5.5 kB)
Requirement already satisfied: boto3 in /Users/ksdyb/.pyenv/versions/3.9.12/lib/python3.9/site-packages (from awsiot) (1.24.22)
Requirement already satisfied: botocore in /Users/ksdyb/.pyenv/versions/3.9.12/lib/python3.9/site-packages (from awsiot) (1.27.22)
Collecting click
  Using cached click-8.1.3-py3-none-any.whl (96 kB)
Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /Users/ksdyb/.pyenv/versions/3.9.12/lib/python3.9/site-packages (from boto3->awsiot) (1.0.1)
Requirement already satisfied: s3transfer<0.7.0,>=0.6.0 in /Users/ksdyb/.pyenv/versions/3.9.12/lib/python3.9/site-packages (from boto3->awsiot) (0.6.0)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /Users/ksdyb/.pyenv/versions/3.9.12/lib/python3.9/site-packages (from botocore->awsiot) (2.8.2)
Requirement already satisfied: urllib3<1.27,>=1.25.4 in /Users/ksdyb/.pyenv/versions/3.9.12/lib/python3.9/site-packages (from botocore->awsiot) (1.26.9)
Requirement already satisfied: six>=1.5 in /Users/ksdyb/.pyenv/versions/3.9.12/lib/python3.9/site-packages (from python-dateutil<3.0.0,>=2.1->botocore->awsiot) (1.16.0)
Installing collected packages: click, awsiot
Successfully installed awsiot-0.1.3 click-8.1.3
```

