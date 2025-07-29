#  https://helloworld.co.in/article/mqtt-raspberry-pi-esp32

import paho.mqtt.client as mqtt
import time

def on_connect(client, user_data, flags, rc):
    print(f"Connected with result code {rc}")
    print(f"User data: {user_data}")
    print(f"Flags: {flags}")

def publish(client):
     msg_count = 1
     while True:
         time.sleep(1)
         msg = f"messages: {msg_count}"
         result = client.publish(topic, msg)
         # result: [0, 1]
         status = result[0]
         if status == 0:
             print(f"Send `{msg}` to topic `{topic}`")
         else:
             print(f"Failed to send message to topic {topic}")
         msg_count += 1
         if msg_count > 5:
             break

topic = "esp32/grasp_power"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"rpi_client2") #this should be a unique name

client.on_connect = on_connect #this function is called when the client gets connected to the MQTT broker
#client.on_disconnect = on_disconnect #this function is called when the client gets disconnected from the MQTT broker

client.connect('127.0.0.1',1883) #1883 is default port of MQTT broker. 
client.loop_start()
publish(client)
client.loop_stop()




