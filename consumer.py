import boto3
import json
import os
from datetime import datetime

# Initialize the SQS client
sqs = boto3.client("sqs")

# The URL for your SQS FIFO queue
QUEUE_URL = os.environ.get('QUEUE_URL')

def calculate_exponential_backoff(attempts, base=2):
    """
    Calculate the exponential backoff time.

    Parameters:
    - attempts (int): The number of times the message has been processed.
    - base (int): The base for the exponential backoff calculation.

    Returns:
    - int: The backoff time in seconds.
    """
    # Calculate the exponential backoff
    timeout = base**attempts
    return timeout


def handler(event, context):
    records = event.get("Records")
    failures = []
    attempts = 0

    for record in records:
        body = record.get("body")
        payload = json.loads(body)

        print(f"Timestamp for MessageId '{payload.get('messageId')}': {datetime.utcnow().isoformat()}")

        receipt_handle = record.get("receiptHandle")
        if receipt_handle:
            # Calculate the number of attempts
            attributes = record.get("attributes", {})
            attempts = int(attributes.get("ApproximateReceiveCount", 0))

            # Calculate the new visibility timeout
            new_timeout = calculate_exponential_backoff(attempts)

            # Update the visibility timeout for the message
            try:
                sqs.change_message_visibility(
                    QueueUrl=QUEUE_URL,
                    ReceiptHandle=receipt_handle,
                    VisibilityTimeout=new_timeout,
                )
                print(
                    f"Visibility timeout increased to {new_timeout} seconds for message"
                )
            except Exception as e:
                print(f"Error increasing visibility timeout: {str(e)}")

            # Add the message to the failures list
            failures.append(
                {
                    "itemIdentifier": receipt_handle,
                }
            )

    # For this sample code, we will limit to 5 attempts
    if failures and attempts <= 5:
        return {"batchItemFailures": failures}
