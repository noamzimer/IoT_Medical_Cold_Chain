import tkinter as tk
import paho.mqtt.client as mqtt
from mqtt_init import broker_ip, port, topic_temp, topic_alarm, topic_actuator

class IoTGui:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Temperature Monitoring System")
        self.root.geometry("400x300")
        
        # Temperature Display
        self.temp_label = tk.Label(root, text="Current Temp: --°C", font=("Arial", 20))
        self.temp_label.pack(pady=20)
        
        # Status/Alarm Display
        self.status_label = tk.Label(root, text="Status: OK", font=("Arial", 14), fg="green")
        self.status_label.pack(pady=10)

        # Relay/Actuator Display
        self.relay_label = tk.Label(root, text="Relay: OFF", font=("Arial", 14), fg="blue")
        self.relay_label.pack(pady=10)

        # MQTT Client Setup
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.connect(broker_ip, port)
        self.client.subscribe([(topic_temp, 0), (topic_alarm, 0), (topic_actuator, 0)])
        self.client.loop_start()

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        
        if msg.topic == topic_temp:
            self.temp_label.config(text=f"Current {payload}°C")
        
        elif msg.topic == topic_alarm:
            self.status_label.config(text=f"ALERT: {payload}", fg="red")
        
        elif msg.topic == topic_actuator:
            if "ON" in payload:
                self.relay_label.config(text="Relay: ON (Cooling)", fg="orange")
            else:
                self.relay_label.config(text="Relay: OFF", fg="blue")
                self.status_label.config(text="Status: OK", fg="green")

# Start the App
if __name__ == "__main__":
    root = tk.Tk()
    app = IoTGui(root)
    root.mainloop()
    