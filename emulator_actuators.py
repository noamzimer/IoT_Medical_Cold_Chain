import paho.mqtt.client as mqtt
from icecream import ic
from mqtt_init import broker_ip, port, topic_actuator

def on_message(client, userdata, msg):
    command = msg.payload.decode()
    ic("Received command: " + command)
    
    if "ON" in command:
        ic('!!! BACKUP GENERATOR IS NOW ON (Fixing Temp) !!!')
    elif "OFF" in command:
        ic('!!! BACKUP GENERATOR IS NOW OFF (Optimal Temp) !!!')

def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker_ip, port)
    client.subscribe(topic_actuator)
    
    ic('Medical Actuator is listening for commands...')
    client.loop_forever()

if __name__ == "__main__":
    main()