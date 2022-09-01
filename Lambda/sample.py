import json 
def lambda_handler(event, context):

	name = event['firstName'] +' '+ event['lastName'] 
	return 	{ 
	'statusCode': 200, 
	'body': json.dumps('Hello from Lambda, ' + name) 
	}
