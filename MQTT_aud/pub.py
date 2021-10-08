import time 
import paho.mqtt.client as paho
import random
import json

broker="broker.himemq.com"
required_QoS = 1
client = paho.Client("client-isu-002")

message_amount = 10

print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Publishing")

for i in range(message_amount):
  state = json.dumps({
    'time': time.time()
    'value': random.randint(0, 100)
  })
  print(f"state is {state}")
  client.publish("house/humidity", state, qos=required_QoS)
  time.sleep(random.randint(0, 1))
  
client.disconnect()
client.loop_stop()
