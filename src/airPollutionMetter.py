from sds011 import SDS011
import src.mqttClient as mqttClient

def getMetters():
    port = "/dev/ttyUSB0"
    sds = SDS011(port=port)
    sds.set_working_period(rate=1)
    print(sds)
    while 1:
        print("MEASURING POLLUTION...")
        data = sds.read_measurement()
        print("MEASURED POLLUTION: ")
        print(data)
        mqttClient.publish(data)