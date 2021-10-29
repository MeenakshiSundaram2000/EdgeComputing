# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import random

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "a2ggzwzh6drv2u-ats.iot.us-east-2.amazonaws.com"
CLIENT_ID = "thing"
PATH_TO_CERT = "certificates/device.pem.crt"
PATH_TO_KEY = "certificates/private.pem.key"
PATH_TO_ROOT = "certificates/root.pem"
MESSAGE = "Water Level(in cms) - "
TOPIC = "test/testing"
RANGE = 20

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
    x = random.randrange(3,18,1)
    data = "{} [{}]".format(MESSAGE, x)
    if(x >= 5):
        message = {"Message" : data}
    else:
        message = {"Message" : data,"Alert" : "Water Sprinkles"}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)
print('Publish End')
myAWSIoTMQTTClient.disconnect()