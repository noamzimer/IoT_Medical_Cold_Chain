import paho.mqtt.client as mqtt
import time
import random
from icecream import ic
from mqtt_init import broker_ip, port, topic_temp

def main():
    client = mqtt.Client()
    client.connect(broker_ip, port)
    
    ic('Vaccine Fridge Sensor is running...')
    
    while True:
        temperature = round(random.uniform(0.0, 12.0), 1)
        message = f"Temperature: {temperature}"
        
        client.publish(topic_temp, message)
        ic(f"Sent: {message}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
    