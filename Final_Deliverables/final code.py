#Bin 1
import wiotp.sdk.device
import time
import random

myConfig = {
  "identity": {
    "orgId": "fzv53v",
    "typeId": "Bin",
    "deviceId":"Bin_1"
  },
  "auth": {
    "token": "1234567890"
  }
}


def myCommandCallback (cmd): 
  print ("Message received from IBM IoT Platform: %s" % cmd.data['command']) 
  m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def pub (data): 
  client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
  print ("Published data Successfully: %s", myData)
  if weight == 10:
            print ('ALERT !! Weight is HIGH')
  if level == 10:
            print ('ALERT !! Level is HIGH')
        

while True:
        level=random.randint(0,10)
        weight=random.randint(0,10)
        myData={'name': 'Bin_1', 'lat': 13.092677, 'lon': 80.188314 ,'Level':level,'Weight':weight}
        pub (myData)
        time.sleep (5)
        client.commandCallback = myCommandCallback
client.disconnect ()
