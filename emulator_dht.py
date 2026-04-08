import paho.mqtt.client as mqtt
import time
import random
import ssl
from icecream import ic
import mqtt_init

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    
    client.username_pw_set(mqtt_init.username, mqtt_init.password)
    client.tls_set()
    
    client.connect(mqtt_init.broker_ip, mqtt_init.port)
    
    ic("Vaccine Fridge Sensor is running...")
    
    while True:
        temperature = round(random.uniform(0.0, 12.0), 1)
        message = f"Temperature: {temperature}"
        
        client.publish(mqtt_init.topic_temp, message)
        ic(f"Sent: {message}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
    