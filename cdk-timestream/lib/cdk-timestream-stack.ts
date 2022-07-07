import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as timestream from 'aws-cdk-lib/aws-timestream';
import * as iot from 'aws-cdk-lib/aws-iot';

export class CdkTimestreamStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const databaseName = 'iot';
    const tableName = 'sources';

    const timestreamDB = new timestream.CfnDatabase(this, "TimestreamDatabase", {
      databaseName: databaseName
    }); 
    new cdk.CfnOutput(this, 'timestreamDBarn', {
      value: timestreamDB.attrArn,
      description: 'The arn of timestreamDB',
    }); 

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

    // Rule Role for timestream
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

    // defile Rule for timestream
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
  }
}
