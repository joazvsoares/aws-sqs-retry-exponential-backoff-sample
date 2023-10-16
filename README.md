# aws-sqs-retry-exponential-backoff-sample

## Producer Logs

---

| message                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INIT_START Runtime Version: python:3.8.v29 Runtime Version ARN: arn:aws:lambda:us-east-1::runtime:f9c3ba8b837f717bec7b7bfa0ad52e1ef3430b18134a4e29a8a2a19442f0f7a2    |
| START RequestId: e46c8162-51a9-4571-8201-62104d5c1da6 Version: $LATEST                                                                                                |
| Sent message 0 with ID 07af0e49-dc42-4e32-927a-af2012be7970                                                                                                           |
| Sent message 1 with ID de343ad3-f760-4aa3-9bf0-344e834cc413                                                                                                           |
| Sent message 2 with ID aeaa5a5f-a878-4a45-8572-7a159dd03bdb                                                                                                           |
| Sent message 3 with ID e4bfb401-2644-47ab-b451-2b95fee4df6d                                                                                                           |
| Sent message 4 with ID 239de627-3807-42db-bed7-b2160e0d41a0                                                                                                           |
| END RequestId: e46c8162-51a9-4571-8201-62104d5c1da6                                                                                                                   |
| REPORT RequestId: e46c8162-51a9-4571-8201-62104d5c1da6 Duration: 96.00 ms Billed Duration: 97 ms Memory Size: 1024 MB Max Memory Used: 66 MB Init Duration: 403.73 ms |

---

## Consumer Logs

---

| message                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INIT_START Runtime Version: python:3.8.v29 Runtime Version ARN: arn:aws:lambda:us-east-1::runtime:f9c3ba8b837f717bec7b7bfa0ad52e1ef3430b18134a4e29a8a2a19442f0f7a2    |
| START RequestId: 3184f36d-1650-5e0c-b2f9-aeca964df421 Version: $LATEST                                                                                                |
| Timestamp for MessageId '07af0e49-dc42-4e32-927a-af2012be7970': 2023-10-16T18:16:13.190167                                                                            |
| Visibility timeout increased to 2 seconds for message                                                                                                                 |
| END RequestId: 3184f36d-1650-5e0c-b2f9-aeca964df421                                                                                                                   |
| REPORT RequestId: 3184f36d-1650-5e0c-b2f9-aeca964df421 Duration: 50.17 ms Billed Duration: 51 ms Memory Size: 1024 MB Max Memory Used: 66 MB Init Duration: 348.14 ms |
| START RequestId: 813efd4c-8c47-5473-be48-a0eb0c596964 Version: $LATEST                                                                                                |
| Timestamp for MessageId '07af0e49-dc42-4e32-927a-af2012be7970': 2023-10-16T18:16:15.287103                                                                            |
| Visibility timeout increased to 4 seconds for message                                                                                                                 |
| END RequestId: 813efd4c-8c47-5473-be48-a0eb0c596964                                                                                                                   |
| REPORT RequestId: 813efd4c-8c47-5473-be48-a0eb0c596964 Duration: 13.85 ms Billed Duration: 14 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 2fd7dd27-8055-5f69-87f8-808000756e12 Version: $LATEST                                                                                                |
| Timestamp for MessageId '07af0e49-dc42-4e32-927a-af2012be7970': 2023-10-16T18:16:19.345477                                                                            |
| Visibility timeout increased to 8 seconds for message                                                                                                                 |
| END RequestId: 2fd7dd27-8055-5f69-87f8-808000756e12                                                                                                                   |
| REPORT RequestId: 2fd7dd27-8055-5f69-87f8-808000756e12 Duration: 12.65 ms Billed Duration: 13 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 6d0f5cb2-2206-5a62-acc7-0115a22b404f Version: $LATEST                                                                                                |
| Timestamp for MessageId '07af0e49-dc42-4e32-927a-af2012be7970': 2023-10-16T18:16:27.406621                                                                            |
| Visibility timeout increased to 16 seconds for message                                                                                                                |
| END RequestId: 6d0f5cb2-2206-5a62-acc7-0115a22b404f                                                                                                                   |
| REPORT RequestId: 6d0f5cb2-2206-5a62-acc7-0115a22b404f Duration: 14.02 ms Billed Duration: 15 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 5535916b-50c0-5cde-9bdf-ccccd0f8a882 Version: $LATEST                                                                                                |
| Timestamp for MessageId '07af0e49-dc42-4e32-927a-af2012be7970': 2023-10-16T18:16:43.484135                                                                            |
| Visibility timeout increased to 32 seconds for message                                                                                                                |
| END RequestId: 5535916b-50c0-5cde-9bdf-ccccd0f8a882                                                                                                                   |
| REPORT RequestId: 5535916b-50c0-5cde-9bdf-ccccd0f8a882 Duration: 16.39 ms Billed Duration: 17 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 686afbca-08d4-5f8d-be34-a66d8883e29a Version: $LATEST                                                                                                |
| Timestamp for MessageId '07af0e49-dc42-4e32-927a-af2012be7970': 2023-10-16T18:17:15.550953                                                                            |
| Visibility timeout increased to 64 seconds for message                                                                                                                |
| END RequestId: 686afbca-08d4-5f8d-be34-a66d8883e29a                                                                                                                   |
| REPORT RequestId: 686afbca-08d4-5f8d-be34-a66d8883e29a Duration: 19.25 ms Billed Duration: 20 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 7226ab53-dde9-524d-903e-f6f45db27336 Version: $LATEST                                                                                                |
| Timestamp for MessageId 'de343ad3-f760-4aa3-9bf0-344e834cc413': 2023-10-16T18:17:15.598216                                                                            |
| Visibility timeout increased to 2 seconds for message                                                                                                                 |
| END RequestId: 7226ab53-dde9-524d-903e-f6f45db27336                                                                                                                   |
| REPORT RequestId: 7226ab53-dde9-524d-903e-f6f45db27336 Duration: 13.34 ms Billed Duration: 14 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: cb5f2e90-e4af-592d-9be7-733764f3328f Version: $LATEST                                                                                                |
| Timestamp for MessageId 'de343ad3-f760-4aa3-9bf0-344e834cc413': 2023-10-16T18:17:17.660456                                                                            |
| Visibility timeout increased to 4 seconds for message                                                                                                                 |
| END RequestId: cb5f2e90-e4af-592d-9be7-733764f3328f                                                                                                                   |
| REPORT RequestId: cb5f2e90-e4af-592d-9be7-733764f3328f Duration: 12.42 ms Billed Duration: 13 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 05239eea-f888-5f9f-928c-c34d78d76bc3 Version: $LATEST                                                                                                |
| Timestamp for MessageId 'de343ad3-f760-4aa3-9bf0-344e834cc413': 2023-10-16T18:17:21.704323                                                                            |
| Visibility timeout increased to 8 seconds for message                                                                                                                 |
| END RequestId: 05239eea-f888-5f9f-928c-c34d78d76bc3                                                                                                                   |
| REPORT RequestId: 05239eea-f888-5f9f-928c-c34d78d76bc3 Duration: 12.32 ms Billed Duration: 13 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 566d3301-d498-5fc9-ae5a-6ea654f3e2de Version: $LATEST                                                                                                |
| Timestamp for MessageId 'de343ad3-f760-4aa3-9bf0-344e834cc413': 2023-10-16T18:17:29.732995                                                                            |
| Visibility timeout increased to 16 seconds for message                                                                                                                |
| END RequestId: 566d3301-d498-5fc9-ae5a-6ea654f3e2de                                                                                                                   |
| REPORT RequestId: 566d3301-d498-5fc9-ae5a-6ea654f3e2de Duration: 15.04 ms Billed Duration: 16 ms Memory Size: 1024 MB Max Memory Used: 67 MB                          |
| START RequestId: 0b9a8bfe-d90a-5527-9339-d659597cce35 Version: $LATEST                                                                                                |
| Timestamp for MessageId 'de343ad3-f760-4aa3-9bf0-344e834cc413': 2023-10-16T18:17:45.791507                                                                            |
| Visibility timeout increased to 32 seconds for message                                                                                                                |
| END RequestId: 0b9a8bfe-d90a-5527-9339-d659597cce35                                                                                                                   |
| REPORT RequestId: 0b9a8bfe-d90a-5527-9339-d659597cce35 Duration: 17.53 ms Billed Duration: 18 ms Memory Size: 1024 MB Max Memory Used: 68 MB                          |
| START RequestId: 3ec67785-db6f-534e-ae81-2a225bf9a8ec Version: $LATEST                                                                                                |
| Timestamp for MessageId 'de343ad3-f760-4aa3-9bf0-344e834cc413': 2023-10-16T18:18:17.840569                                                                            |
| Visibility timeout increased to 64 seconds for message                                                                                                                |
| END RequestId: 3ec67785-db6f-534e-ae81-2a225bf9a8ec                                                                                                                   |
| REPORT RequestId: 3ec67785-db6f-534e-ae81-2a225bf9a8ec Duration: 15.49 ms Billed Duration: 16 ms Memory Size: 1024 MB Max Memory Used: 68 MB                          |
| START RequestId: b4ec8643-031d-5392-87d6-dbe4838457ce Version: $LATEST                                                                                                |
| Timestamp for MessageId 'aeaa5a5f-a878-4a45-8572-7a159dd03bdb': 2023-10-16T18:18:17.889964                                                                            |
| Visibility timeout increased to 2 seconds for message                                                                                                                 |
| END RequestId: b4ec8643-031d-5392-87d6-dbe4838457ce                                                                                                                   |
| REPORT RequestId: b4ec8643-031d-5392-87d6-dbe4838457ce Duration: 14.27 ms Billed Duration: 15 ms Memory Size: 1024 MB Max Memory Used: 68 MB                          |
| START RequestId: 24b59345-3653-58b7-b8cd-cee2b6ce450a Version: $LATEST                                                                                                |
| Timestamp for MessageId 'aeaa5a5f-a878-4a45-8572-7a159dd03bdb': 2023-10-16T18:18:19.929421                                                                            |
| Visibility timeout increased to 4 seconds for message                                                                                                                 |
| END RequestId: 24b59345-3653-58b7-b8cd-cee2b6ce450a                                                                                                                   |
| REPORT RequestId: 24b59345-3653-58b7-b8cd-cee2b6ce450a Duration: 16.09 ms Billed Duration: 17 ms Memory Size: 1024 MB Max Memory Used: 68 MB                          |
| START RequestId: 56a1b6ba-df79-54be-9b22-eb1d5fe71490 Version: $LATEST                                                                                                |
| Timestamp for MessageId 'aeaa5a5f-a878-4a45-8572-7a159dd03bdb': 2023-10-16T18:18:23.979654                                                                            |
| END RequestId: 56a1b6ba-df79-54be-9b22-eb1d5fe71490                                                                                                                   |
| REPORT RequestId: 56a1b6ba-df79-54be-9b22-eb1d5fe71490 Duration: 10.85 ms Billed Duration: 11 ms Memory Size: 1024 MB Max Memory Used: 68 MB                          |
| Visibility timeout increased to 8 seconds for message                                                                                                                 |
| START RequestId: ad9d26a9-96f9-54b8-b54a-7b0e165f2698 Version: $LATEST                                                                                                |
| Timestamp for MessageId 'aeaa5a5f-a878-4a45-8572-7a159dd03bdb': 2023-10-16T18:18:32.033968                                                                            |
| Visibility timeout increased to 16 seconds for message                                                                                                                |
| END RequestId: ad9d26a9-96f9-54b8-b54a-7b0e165f2698                                                                                                                   |
| REPORT RequestId: ad9d26a9-96f9-54b8-b54a-7b0e165f2698 Duration: 13.07 ms Billed Duration: 14 ms Memory Size: 1024 MB Max Memory Used: 68 MB                          |
| START RequestId: a60835cc-4066-50ad-b9ce-686bc0d3b78d Version: $LATEST                                                                                                |
| Timestamp for MessageId 'aeaa5a5f-a878-4a45-8572-7a159dd03bdb': 2023-10-16T18:18:48.080508                                                                            |
| Visibility timeout increased to 32 seconds for message                                                                                                                |
| END RequestId: a60835cc-4066-50ad-b9ce-686bc0d3b78d                                                                                                                   |
| REPORT RequestId: a60835cc-4066-50ad-b9ce-686bc0d3b78d Duration: 15.81 ms Billed Duration: 16 ms Memory Size: 1024 MB Max Memory Used: 68 MB                          |

---
