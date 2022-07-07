# AWS CDK를 이용한 IoT 인프라 구축

여기에서는 [AWS CDK](https://github.com/kyopark2014/technical-summary/blob/main/cdk-introduction.md)를 이용하여, IoT Core의 Rule과 Timestream을 생성합니다. 또한, 여기서는 CDK 2.0을 기준으로 Typescript를 이용해 구현하였습니다.

Timestream의 Database 이름과 Table을 아래와 같이 정의 합니다. 

```java
    const databaseName = 'iot';
    const tableName = 'sources';
```    

Timestrem Database를 정의 합니다. 
```java
    const timestreamDB = new timestream.CfnDatabase(this, "TimestreamDatabase", {
      databaseName: databaseName
    }); 
    new cdk.CfnOutput(this, 'timestreamDBarn', {
      value: timestreamDB.attrArn,
      description: 'The arn of timestreamDB',
    }); 
```    

Timestream의 table을 정의합니다. 여기서는 편의상 48시간 in-memory, 2년의 magnetic store를 정의하였습니다.

```java
    if (timestreamDB.databaseName) {
      const timestreamTable = new timestream.CfnTable(this, "TimestreamTable", {
        databaseName: timestreamDB.databaseName, // create implicit CFN dependency
        tableName: tableName,
        retentionProperties: {
          memoryStoreRetentionPeriodInHours: (24*2).toString(10),   // Keep data for 48 in-mem
          magneticStoreRetentionPeriodInDays: (365*2).toString(10)    // Keep data on disk for 2 years
        },
      });
      timestreamTable.node.addDependency(timestreamDB);
      new cdk.CfnOutput(this, "TimestreamDatabaseName", { value: `${timestreamDB.databaseName}` });
      new cdk.CfnOutput(this, "TimestreamTableName", { value: `${timestreamTable.tableName}` });
    } 
```    

IoT Core의 Rule을 통해 특정 topic에서 데이터를 Timestream으로 보내기 위한 IAM Role을 아래와 같이 정의합니다. 생성한 Timestream database에 대한 WriteRecords 권한을 주고 있습니다. 

```java
    const timestreamRole = new iam.Role(this, "timestreamRole", {
      roleName: 'timestreamRole',
      assumedBy: new iam.ServicePrincipal("iot.amazonaws.com"),
      description: "Role of Rule for Timestream",
    }); 
    timestreamRole.addToPolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "timestream:WriteRecords",
      ],
      resources: [
        timestreamDB.attrArn+'/*'
      ],
    })); 
    timestreamRole.addToPolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "timestream:DescribeEndpoints"
      ],
      resources: ['*'],
    })); 
    new cdk.CfnOutput(this, 'timestreamRoleArn', {
      value: timestreamRole.roleArn,
      description: 'The arn of timestreamRole for IoT',
    }); 
```    

Timestream으로 'sim/test' Topic으로 들어오는 모든 데이터를 전송하기 위한 Rule을 아래와 같이 정의하였습니다. 

```java
    new iot.CfnTopicRule(this, "TopicRule", {
      topicRulePayload: {
        actions: [
          {
            timestream: {
              databaseName: databaseName,
              tableName: tableName,
              dimensions: [{
                name: 'alias',
                value: '${alias}',
              }],
              roleArn: timestreamRole.roleArn,
              batchMode: false,  // the properties below are optional
              timestamp: { 
                unit: 'SECONDS', 
                value: '${ts}'
              },  
            },
          },
        ],
        sql: "SELECT value FROM 'sim/test'",
        ruleDisabled: false,
      },
      ruleName: "ruleTimestream",
    });
```
