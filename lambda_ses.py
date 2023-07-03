import boto3
import json

def lambda_handler(event, context):
    
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']   

    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    email_ids = s3_object['Body'].read().decode('utf-8').split('\n')
    print(s3_bucket)
    print(s3_key)
    print(s3_object)
    print(email_ids)
    ses_client = boto3.client('ses')
    
    for email_id in email_ids:
        email_id = email_id.strip()
        print(email_id)
        response = ses_client.send_email(Source= 'ketan8157@gmail.com',Destination={'ToAddresses': [email_id]},
               Message={'Subject': {'Data': 'ses called '},'Body': {'Text': {'Data': 'hye i send mail from ses using s3 through lambda'}}
                   })
        print("Email sent to {} ".format(email_id))
