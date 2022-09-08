import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    QOS,
    PublishToIoTCoreRequest
)

TIMEOUT = 10

def publish(data):
    ipc_client = awsiot.greengrasscoreipc.connect()
                        
    topic = "pollution"
    message = '{"message": {"pm25":'+str(data['pm2.5'])+',"pm10":' +str(data['pm10'])+'}}'

    print('MQTT MESSAGE'+message)
    qos = QOS.AT_LEAST_ONCE

    request = PublishToIoTCoreRequest()
    request.topic_name = topic
    request.payload = bytes(message, "utf-8")
    request.qos = qos
    operation = ipc_client.new_publish_to_iot_core()
    operation.activate(request)
    future_response = operation.get_response()
    future_response.result(TIMEOUT)
    print('MQTT PUBLISHED')