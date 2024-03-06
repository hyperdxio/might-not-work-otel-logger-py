import requests
import time

body = {
    "resourceLogs": [
        {
            "resource": {
                "attributes": [
                    {"key": "service.name", "value": {"stringValue": "my-service"}}
                ],
                "droppedAttributesCount": 0,
            },
            "scopeLogs": [
                {
                    "scope": {"name": "otel-logger"},
                    "logRecords": [
                        {
                            "timeUnixNano": int(time.time() * 1000000000),
                            "observedTimeUnixNano": int(time.time() * 1000000000),
                            "severityNumber": 9,
                            "severityText": "INFO",
                            "body": {"stringValue": "👋 Hello from HyperDX!"},
                            "attributes": [
                                {
                                    "key": "loggerName",
                                    "value": {"stringValue": "my-otel-logger"},
                                }
                            ],
                            "droppedAttributesCount": 0,
                            "flags": 1,
                            "traceId": "047833eeef9af7e048839f4685667c44",
                            "spanId": "e897c0c71b979fcb",
                        },
                        {
                            "timeUnixNano": int(time.time() * 1000000000),
                            "observedTimeUnixNano": int(time.time() * 1000000000),
                            "severityNumber": 17,
                            "severityText": "ERROR",
                            "body": {"stringValue": "Oh no an error!!"},
                            "attributes": [
                                {
                                    "key": "loggerName",
                                    "value": {"stringValue": "my-otel-logger"},
                                }
                            ],
                            "droppedAttributesCount": 0,
                            "flags": 1,
                            "traceId": "047833eeef9af7e048839f4685667c44",
                            "spanId": "e897c0c71b979fcb",
                        },
                        {
                            "timeUnixNano": int(time.time() * 1000000000),
                            "observedTimeUnixNano": int(time.time() * 1000000000),
                            "severityNumber": 9,
                            "severityText": "INFO",
                            "body": {"stringValue": '{"foo":"bar","baz":"qux"}'},
                            "attributes": [
                                {
                                    "key": "loggerName",
                                    "value": {"stringValue": "my-otel-logger"},
                                }
                            ],
                            "droppedAttributesCount": 0,
                            "flags": 1,
                            "traceId": "047833eeef9af7e048839f4685667c44",
                            "spanId": "e897c0c71b979fcb",
                        },
                    ],
                }
            ],
        }
    ]
}


class Logger:
    def __init__(self, api_key):
        self.api_key = api_key

    def info(self):
        requests.post(
            "http://localhost:4318/v1/logs",
            headers={"Authorization": self.api_key},
            json=body,
        )
