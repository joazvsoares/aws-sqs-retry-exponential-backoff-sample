import boto3
import json
import uuid
import os

# Initialize the SQS client
sqs = boto3.client('sqs')

# The URL for your SQS FIFO queue
QUEUE_URL = os.environ.get('QUEUE_URL')

def handler(event, context):
    # Define a constant MessageGroupId
    message_group_id = str(uuid.uuid4())

    # Loop to send multiple messages with the same MessageGroupId
    for i in range(5):  # this will send 5 messages as an example
        message_id = str(uuid.uuid4())

        # Your message payload (adjust this as per your needs)
        payload = {
            "messageGroupId": message_group_id,
            "messageId": message_id
        }

        # Convert the payload to a string format (JSON in this case)
        message_body = json.dumps(payload)

        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=message_body,
            MessageGroupId=message_group_id,
            MessageDeduplicationId=message_id
        )
        print(f"Sent message {i} with ID {message_id}")

    return {
        "statusCode": 200,
        "body": json.dumps("Message sent successfully!")
    }
