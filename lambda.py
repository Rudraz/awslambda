#authentication bypass checks with SQLi

import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    Username = event['Username']
    Password = event['Password']
    print (Username, Password)
    
    client = boto3.resource('dynamodb')
    table = client.Table('user_table')
    
    item = {
        'Username' : Username, 
        'Password' : Password
    }
    
    print ("Item", item)
    #validate_inputs(Username,Password)
    print("Username and Password are accepted!")
    #Scan DynamoDB user_table to validate incoming data 
    response = table.scan(FilterExpression = Attr("Username").eq(Username) & Attr("Password").eq(Password))
    print("response:", response)
    output = response["Items"]
    print ("Output", output)
      for x in output:
        print ("Login Matches")
        break
      else:
        print ("Login Failed")
     
    
