import tkinter as tk
import paho.mqtt.client as mqtt
import ssl
import mqtt_init

class IoTGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Medical Cold Chain - Vaccine Monitor")
        self.root.geometry("450x300")
        
        self.temp_label = tk.Label(root, text="Fridge Temp: -- C", font=("Arial", 20))
        self.temp_label.pack(pady=20)
        
        self.status_label = tk.Label(root, text="Status: Optimal (2 C - 8 C)", font=("Arial", 14), fg="green")
        self.status_label.pack(pady=10)

        self.relay_label = tk.Label(root, text="Backup Generator: OFF", font=("Arial", 14), fg="blue")
        self.relay_label.pack(pady=10)

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        
        self.client.username_pw_set(mqtt_init.username, mqtt_init.password)
        self.client.tls_set()
        
        self.client.on_message = self.on_message
        self.client.connect(mqtt_init.broker_ip, mqtt_init.port)
        self.client.subscribe([(mqtt_init.topic_temp, 0), (mqtt_init.topic_alarm, 0), (mqtt_init.topic_actuator, 0)])
        self.client.loop_start()

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        
        if msg.topic == mqtt_init.topic_temp:
            try:
                temp_val = payload.split(": ")[1]
                self.temp_label.config(text=f"Fridge Temp: {temp_val} C")
            except:
                pass
        
        elif msg.topic == mqtt_init.topic_alarm:
            if "CRITICAL" in payload:
                self.status_label.config(text=f"ALERT: {payload}", fg="red")
            else:
                self.status_label.config(text=payload, fg="green")
        
        elif msg.topic == mqtt_init.topic_actuator:
            if "ON" in payload:
                self.relay_label.config(text="Backup System: ON (Fixing Temp)", fg="orange")
            else:
                self.relay_label.config(text="Backup System: OFF", fg="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = IoTGui(root)
    root.mainloop()