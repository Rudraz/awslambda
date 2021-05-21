# authentication bypass checks with SQLi

import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import re


def lambda_handler(event, context):
    # TODO implement
    print(event)

    Username = event['Username']
    Password = event['Password']
    print(Username, Password)

    client = boto3.resource('dynamodb')
    table = client.Table('user_table')

    item = {
        'Username': Username,
        'Password': Password
    }

    print("Item", item)
    validate_inputs(Username, Password)

    print("Post validation check Username and password:", Username, Password)

    '''
    #Scan DynamoDB user_table to validate incoming data 
    response = table.scan(
    FilterExpression = Attr("Username").eq(Username) & Attr("Password").eq(Password)
    )

    print("response:", response)
    output = response["Items"]
    print ("Output", output)

    for x in output:
        print ("Login Matches")
        break
    else:
        print ("Login Failed")
    '''


def validate_inputs(Username, Password):
    print("Start validation check")
    if not (Username and Password):
        return {'error': 'Username and password not provided.'}
    if re.search(r"[A-Za-z0-9@#$%^&]{8,}", Username) is None:
        return {'error': Username}
    if re.search(r"[A-Za-z0-9@#$%^&]{8,}", Password) is None:
        return {'error': Password}

    try:
        re.match(r"[A-Za-z0-9@#$%^&]{8,}", Username)
        pattern = re.compile(r"[A-Za-z0-9@#$%^&]{8,}")
        Username = pattern.match(Username)
        print("The username is in accordance to validation input checks performed")

        re.match(r"[A-Za-z0-9@#$%^&]{8,}", Password)
        pattern = re.compile(r"[A-Za-z0-9@#$%^&]{8,}")
        Username = pattern.match(Password)
        print("The password is in accordance to validation input checks performed")

        return {'Username': Username,
                'Password': Password}
    except:
        return {'error': 'Invalid Username and Password'}
    print("Exit validation")

    '''
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    '''
