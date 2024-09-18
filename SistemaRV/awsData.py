import boto3

ssm = boto3.client('ssm')

response = ssm.get_parameter(Name='/Qickart/dev/testVariable')



api_url = response['Parameter']['Value']
