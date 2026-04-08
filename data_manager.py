import paho.mqtt.client as mqtt
import sqlite3
import ssl
from icecream import ic
import mqtt_init

def init_db():
    conn = sqlite3.connect("project_db.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS temp_logs 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, value REAL)''')
    conn.commit()
    return conn

def save_to_db(temp_value):
    conn = sqlite3.connect("project_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temp_logs (value) VALUES (?)", (temp_value,))
    conn.commit()
    conn.close()

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    
    if msg.topic == mqtt_init.topic_control and "RESET" in payload:
        ic("Manual Reset Received! Turning off alarms.")
        client.publish(mqtt_init.topic_alarm, "Status: Optimal (2 C - 8 C)")
        client.publish(mqtt_init.topic_actuator, "RELAY: OFF")
        return
        
    if msg.topic == mqtt_init.topic_temp:
        ic("Manager received: " + payload)
        try:
            temp_value = float(payload.split(": ")[1])
            save_to_db(temp_value)
            
            if temp_value < mqtt_init.MIN_TEMP or temp_value > mqtt_init.MAX_TEMP:
                ic("CRITICAL ALERT! Temp out of safe range: " + str(temp_value))
                client.publish(mqtt_init.topic_alarm, f"CRITICAL: Temp is {temp_value} C!")
                client.publish(mqtt_init.topic_actuator, "RELAY: ON")
            else:
                client.publish(mqtt_init.topic_actuator, "RELAY: OFF")
                client.publish(mqtt_init.topic_alarm, "Status: Optimal (2 C - 8 C)")
                
        except Exception as e:
            ic("Error processing message: " + str(e))

def main():
    init_db()
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    
    client.username_pw_set(mqtt_init.username, mqtt_init.password)
    client.tls_set()
    
    client.on_message = on_message
    client.connect(mqtt_init.broker_ip, mqtt_init.port)
    client.subscribe([(mqtt_init.topic_temp, 0), (mqtt_init.topic_control, 0)])
    
    ic("Medical Cold Chain Manager is running and logging to DB...")
    client.loop_forever()

if __name__ == "__main__":
    main()