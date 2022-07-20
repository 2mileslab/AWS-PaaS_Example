```
{
    "StartAt": "Check Inventory",
    "States": {
        "Check Inventory": {
            "Type": "Pass",
            "OutputPath": "$",
            "Next": "Place CC Hold"
        },
        "Place CC Hold": {            
            "Type": "Pass",
            "OutputPath": "$",
            "Next": "Request Driver"
        },
        "Request Driver": {
            "Type": "Task",
            "Resource": "arn:aws:states:::sns:publish.waitForTaskToken",
            "TimeoutSeconds": 15,
            "Parameters": {
                "Message": {
                    "TaskToken.$": "$$.Task.Token",
                    "Input.$": "$.OrderNumber"
                },
                "TopicArn": "arn:aws:sns:us-east-2:123456789012:DeliveryRequest"
            },
             "Catch": [ {
                "ErrorEquals": [ "States.Timeout" ],
                "Next": "Notify Customer of Delay"
             } ],
            "Next": "Delivery Assigned to Driver"
        },
        "Delivery Assigned to Driver": {
            "Type": "Pass",
            "OutputPath": "$",
            "End": true
        },
        "Notify Customer of Delay": {
            "Type": "Pass",
            "OutputPath": "$",
            "End": true
        }
    }
}
```
