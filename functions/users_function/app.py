import requests

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "msg": "Hello from Users Function"
    }
