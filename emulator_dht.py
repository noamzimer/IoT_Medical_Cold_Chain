import paho.mqtt.client as mqtt
import time
import random
from icecream import ic
from mqtt_init import broker_ip, port, topic_temp

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(broker_ip, port)
    client.loop_start()

    ic("Sensor (DHT) is running...")
    
    try:
        while True:
            temp = round(random.uniform(20.0, 35.0), 1)
            message = f"Temperature: {temp}"
            client.publish(topic_temp, message)
            ic(f"Sent: {message}")
            time.sleep(5)
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()
    