import paho.mqtt.client as mqtt
import time

grasp_power = 0
data_recieved_at = 0
def on_connect(client, user_data, flags, rc):
    print(f"Connected with result code {rc}")
    print(f"User data: {user_data}")
    print(f"Flags: {flags}")
    flag_connected = 1

def on_disconnect(client):
    print(f"Mqtt disconnected ")
    flag_connected = 0

def on_message(client, user_data, msg):
    print(f"Topic: {msg.topic}")
    print(f"Payload: {msg.payload}")
    grasp_power_str = msg.payload.decode("utf-8")
    print(f"Grasp power: {grasp_power_str}")
    grasp_power = float(grasp_power_str)
    data_received_at = time.now()

#  https://helloworld.co.in/article/mqtt-raspberry-pi-esp32
def get_value(delay):
    if time.now() - data_recieved_at < delay:
        return data_received_at, grasp_power

def start_mqtt(topic):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"rpi_client1") #this should be a unique name
    flag_connected = 0 #flag to monitor if the client is connected to MQTT broker or not

    client.on_connect = on_connect #this function is called when the client gets connected to the MQTT broker
    client.on_disconnect = on_disconnect #this function is called when the client gets disconnected from the MQTT broker

    #client.message_callback_add('esp32/grasp_power', callback_grasp_power)
    client.on_message = on_message
    client.connect('127.0.0.1',1883) #1883 is default port of MQTT broker. 
    client.subscribe(topic) 
    client.loop_forever()
    print("......client setup complete............")
    return client



