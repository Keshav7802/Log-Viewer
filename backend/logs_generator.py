# This file is to randomly generate a list of logs, which we can ingest into our system.
# Currently I tested it for 10000, we can test it for more by passing appropriate value of num_logs
# The logs will be stored in sample_logs.txt

import json
import random
import string
from datetime import datetime, timedelta, timezone
def generate_sample_logs(num_logs):
    sample_logs = []

    for _ in range(num_logs):
        log = {
            "level": random.choice(["info", "warning", "error"]),
            "message": ''.join(random.choices(string.ascii_letters + string.digits, k=20)),
            "resourceId": ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            "timestamp": (datetime.now(timezone.utc) - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "traceId": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            "spanId": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            "commit": ''.join(random.choices(string.ascii_letters + string.digits, k=7)),
            "metadata": {
                "parentResourceId": ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            }
        }
        sample_logs.append(log)

    return sample_logs

# Example: Generate 100 sample logs
sample_logs = generate_sample_logs(10000)

# Save sample logs to a JSON file
with open('sample_logs.txt', 'w') as file:
    json.dump(sample_logs, file, indent=2)
