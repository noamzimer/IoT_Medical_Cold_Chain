import paho.mqtt.client as mqtt
import ssl
from icecream import ic
import mqtt_init

def on_message(client, userdata, msg):
    command = msg.payload.decode()
    ic("Received command: " + command)
    
    if "ON" in command:
        ic("!!! BACKUP GENERATOR IS NOW ON (Fixing Temp) !!!")
    elif "OFF" in command:
        ic("!!! BACKUP GENERATOR IS NOW OFF (Optimal Temp) !!!")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    
    client.username_pw_set(mqtt_init.username, mqtt_init.password)
    client.tls_set()
    
    client.on_message = on_message
    client.connect(mqtt_init.broker_ip, mqtt_init.port)
    client.subscribe(mqtt_init.topic_actuator)
    
    ic("Medical Actuator is listening for commands...")
    client.loop_forever()

if __name__ == "__main__":
    main()
    