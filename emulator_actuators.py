import paho.mqtt.client as mqtt
from icecream import ic
from mqtt_init import broker_ip, port, topic_actuator

def on_message(client, userdata, msg):
    command = msg.payload.decode()
    ic("Received command: " + command)
    if "ON" in command:
        ic("!!! RELAY IS NOW ON (Cooling Started) !!!")
    elif "OFF" in command:
        ic("!!! RELAY IS NOW OFF !!!")

def main():
    # Using older client call to avoid version issues
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker_ip, port)
    client.subscribe(topic_actuator)
    
    ic("Actuator (Relay/Button) is listening...")
    client.loop_forever()

if __name__ == "__main__":
    main()
    