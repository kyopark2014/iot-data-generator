# IoT Core에서 Rule 설정

1) [IoT Core의 Rule Console](https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/rulehub)로 이동하여 [Create rule]을 선택합니다. 

2) [Specify rule properties]에서 [Rule name]으로 "RuleDataGenerator"라고 입력후에 [Next]를 선택합니다.


![noname](https://user-images.githubusercontent.com/52392004/177545100-cfa26a68-575b-4b96-b568-0fc751c76419.png)

3) 아래와 같이 [SQL statement]로 "SELECT value FROM 'sim/test'"라고 입력하고, [Next]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177545520-d6880790-e868-440b-b3da-e225cad7ea79.png)

4) [Rule actions]에서 [Action1]으로 "Timestream table]을 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177545926-7f709b78-8868-4e1f-b706-964cddcd12df.png)

5) [Database name]으로 기 생성한 Timestream의 Database인 "DataGenerator"를 선택합니다. [Table name]으로 역시 기생성한 "IoTData"를 선택합니다. [Dimension]은 "alias"를 "${alias}"로 아래처럼 입력합니다. 이후 [Create new role]을 선택합니다.

![noname](https://user-images.githubusercontent.com/52392004/177547869-9646493f-0dcb-4e53-8670-6fbc9388d4ea.png)

6) [Create role]에서 "IoT_Data_Generation"라고 입력하고, [Create]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/177548425-b2db3a58-b511-41c3-bfda-f8f14ae58ba6.png)

7) [Next]를 선택하고 다시 [Create]를 선택해 Rule을 생성합니다. 


