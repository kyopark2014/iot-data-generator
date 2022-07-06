# Amazon Timestream

Timestream은 시계열 데이터를 저장하고 활용하는 좋은 방법입니다. 여기서는 IoT Sensor로 부터 올라오는 데이터를 IoT Core를 통해 어떻게 Timestream에 저장하는 방법에 대해 소개합니다. 

1) [Timestream Console](https://us-east-1.console.aws.amazon.com/timestream/home?region=us-east-1#databases)로 접속하여 [Create database]를 선택합니다. 

2) [Create database]에서 "Standard database"를 선택하고, Name을 입력합니다. 여기서는 "DataGenerator"라고 합니다. Timestream은 모든 데이터를 암호화합니다. 아래와 같이 KMS key를 지정할 수 있습니다. [Create database]를 선택하여 Database를 생성합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177542879-1fcc7c0d-6235-4765-833d-f40f9da68037.png)

3) 아래처럼 "DataGenerator"를 선택하여 상세화면으로 진입합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177543387-25362fa2-192b-4a48-95d6-f9b7d8d57c58.png)

4) 아래와 같이 [Tables]에서 [Create table]을 선택합니다.

![noname](https://user-images.githubusercontent.com/52392004/177543801-65989cc8-eedd-4a9b-8cce-86a40759d61b.png)

5) 아래와 같이 [Table name]으로 "IoTData"라고 입력합니다. [Data retention]으로 여기서는 [Memory store retention]을 1 day와 [Magnetic store retention]을 5 days로 선택하였습니다. 아래로 스크롤하여 [Create table]을 선택합니다. 


![noname](https://user-images.githubusercontent.com/52392004/177544412-ae7b8bfd-3579-442c-b5b3-7cf9bd470f2b.png)

