import boto3

ssm = boto3.client('ssm',
                   aws_access_key_id='YOUR_ACCESS_KEY_ID',
                   aws_secret_access_key='YOUR_SECRET_ACCESS_KEY', 
                   region_name='us-east-1')

response = ssm.get_parameter(Name='arn:aws:ssm:us-east-1:767398014365:parameter/Qickart/dev/testVariable')
print(response)
api_url = response['Parameter']['Value']
print(api_url)