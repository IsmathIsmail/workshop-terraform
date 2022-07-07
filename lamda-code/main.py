import json
import logging
import os,sys
import urllib3
from urllib.request import Request, urlopen, URLError, HTTPError
from urllib import parse
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
def lambda_handler(event, context):

    http = urllib3.PoolManager()
    response = http.request('GET', os.environ['END_POINT_URL'])

    print(response.status) # Status code.

    fallback_message = response.status

    if response.status:
        print("post slack message")
    elif a == b:
        print("send slack message that the endpoint is not functioning")

    if response.status:
        slack_status=":heavy_check_mark: SUCCEEDED"
        slack_colour="#36a64f"
    else :
        slack_status=":X: FAILED"
        slack_colour="#FF0000"


    slack_message ={
    "username": "Lamda_alerts",
    "attachments": [
        {
            "fallback": fallback_message,
            "color": slack_colour,
            "blocks": [
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": " End point hit from lamda is success ".format(slack_status)
                        }
                    ]
                }
            ]
        }
    ]
    }

    if SLACK_WEBHOOK_URL:
        req = Request(SLACK_WEBHOOK_URL, json.dumps(slack_message).encode('utf-8'))
        try:
            response = urlopen(req)
            response.read()
            logger.info("Message posted!")
        except HTTPError as e:
            logger.error("Request failed: %d %s", e.code, e.reason)
        except URLError as e:
            logger.error("Server connection failed: %s", e.reason)

        return "Success"
    else:
        logger.error("Invalid SLACK_WEBHOOK_URL")
