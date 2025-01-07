from flask import Flask
import boto3
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    parameter_name = os.getenv('PARAMETER_NAME', '/hello-world/message')
    region_name = os.getenv('AWS_REGION', 'us-east-1')

    ssm = boto3.client('ssm', region_name=region_name)
    response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    message = response['Parameter']['Value']

    return f"<h1>{message}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
