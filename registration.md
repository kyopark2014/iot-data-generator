# IoT Data Generator를 Thing으로 등록

1) IoT console로 진입하여 [Connect Device]를 선택합니다.

https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/home

![noname](https://user-images.githubusercontent.com/52392004/177144145-2064a088-6ddf-4019-be82-f91271c8b1b0.png)


2) [CONNECT TO AWS IOT]에서 [Get started]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177144332-53aa07e9-7b78-421a-95f3-ac3d273c0463.png)

3) [How are you connecting to AWS IoT?]에서 [Choose a platform]은 "Linux/OSX"를 선택하고, [Choose a AWS IoT Device SDK]에서는 [Python]을 선택합니다. 이후 [Next]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177144832-6f7124bf-dad9-438b-86a9-dcfaba345f04.png)


4) [Register a thing]에서 [Name]으로 "data-generator"라고 입력합니다. 이후 [Next step]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177145168-6bb6559e-137c-428c-9184-2541cb552507.png)

5) [Download a connection kit]에서 [Download connection kit for]에서 [Linux/OSX]를 선택하여 다운로드 합니다. 다운로드가 다 되면, [Next step]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177145451-494b1dfe-2e2d-47b4-ad4f-666b30cbab1c.png)

6) 아래처럼 [Done]으로 Thing 등록을 완료합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177145729-d4e06410-b964-4d8a-94ca-3de66e4992c0.png)

7) [AWS IoT] - [Manage] - [Things]로 이동하면 아래와 같이 Thing으로 등록된것을 확인할 수 있습니다.

![noname](https://user-images.githubusercontent.com/52392004/177145952-854e7e08-6afe-4ba8-8913-6a1b2a54539c.png)

8) 다운로드 받은 zip파일로 이동하여 압축을 풀고 아래와 같이 "data-generator"를 아래와 같이 싱행하여, 정상적으로 동작하는지 확인합니다. 

```c
$ unzip connect_device_package.zip
$ cd connect_device_package
$ chmod +x start.sh
$ ./start.sh
2022-07-04 20:42:21,272 - AWSIoTPythonSDK.core.protocol.internal.workers - DEBUG - Produced [puback] event
2022-07-04 20:42:21,272 - AWSIoTPythonSDK.core.protocol.internal.workers - DEBUG - Dispatching [puback] event
2022-07-04 20:42:21,272 - AWSIoTPythonSDK.core.protocol.internal.clients - DEBUG - Invoking custom event callback...
2022-07-04 20:42:21,272 - AWSIoTPythonSDK.core.protocol.internal.clients - DEBUG - This custom event callback is for pub/sub/unsub, removing it after invocation...
2022-07-04 20:42:21,299 - AWSIoTPythonSDK.core.protocol.internal.workers - DEBUG - Produced [message] event
2022-07-04 20:42:21,299 - AWSIoTPythonSDK.core.protocol.internal.workers - DEBUG - Dispatching [message] event
Received a new message:
b'{"message": "Hello World!", "sequence": 0}'
from topic:
sdk/test/Python
--------------
```

잘 동작하면 "Ctrl-C"로 종료합니다. 


9) zip 파일의 압축 해제 및 스크립트 실행("start.sh")후에 아래와 같은 파일들이 생성되어 있음을 알 수 있습니다.

![image](https://user-images.githubusercontent.com/52392004/177213906-dbe60ea2-1c21-46e6-9499-d2c1f6a42f6b.png)






