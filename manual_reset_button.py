import paho.mqtt.client as mqtt
import time
import json

# --- Configuration ---
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_CONTROL = "medical/fridge/control"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Reset Button Connected to Broker!")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect
client.connect(BROKER, PORT, 60)

print("Press Ctrl+C to stop the button emulator.")

try:
    while True:
        user_input = input("Press 'r' and Enter to ACKNOWLEDGE/RESET alert: ")
        if user_input.lower() == 'r':
            message = {"action": "RESET_ALERT", "staff_member": "Duty Nurse"}
            client.publish(TOPIC_CONTROL, json.dumps(message))
            print(">>> Reset signal sent to System.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping Button Emulator...")
finally:
    client.disconnect()