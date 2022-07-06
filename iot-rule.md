# IoT Core에서 Rule 설정

1) [IoT Core의 Rule Console](https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/rulehub)로 이동하여 [Create rule]을 선택합니다. 

2) [Specify rule properties]에서 [Rule name]으로 "RuleDataGenerator"라고 입력후에 [Next]를 선택합니다.


![noname](https://user-images.githubusercontent.com/52392004/177545100-cfa26a68-575b-4b96-b568-0fc751c76419.png)

3) 아래와 같이 [SQL statement]로 "SELECT value FROM 'sim/test'"라고 입력하고, [Next]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177545520-d6880790-e868-440b-b3da-e225cad7ea79.png)

4) [Rule actions]에서 [Action1]으로 "Timestream table]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177545926-7f709b78-8868-4e1f-b706-964cddcd12df.png)

5) [Database name]으로 기 생성한 Timestream의 Database인 "DataGenerator"를 선택합니다. [Table name]으로 역시 기생성한 "IoTData"를 선택합니다. [Dimension]은 "alias"를 "${alias}"로 아래처럼 입력합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177546731-8f31c664-937c-41fa-b33c-3ea3eb908cb6.png)
