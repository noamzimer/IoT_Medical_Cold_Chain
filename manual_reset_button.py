import paho.mqtt.client as mqtt
import time
import ssl
import mqtt_init

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Reset Button Connected to Broker!")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect

client.username_pw_set(mqtt_init.username, mqtt_init.password)
client.tls_set()

client.connect(mqtt_init.broker_ip, mqtt_init.port, 60)
client.loop_start()

print("Press Ctrl+C to stop the button emulator.")

try:
    while True:
        user_input = input("Press 'r' and Enter to ACKNOWLEDGE/RESET alert: ")
        if user_input.lower() == 'r':
            client.publish(mqtt_init.topic_control, "RESET")
            print(">>> Reset signal sent to System.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping Button Emulator...")
finally:
    client.disconnect()
    client.loop_stop()