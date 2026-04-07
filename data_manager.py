import paho.mqtt.client as mqtt
import sqlite3
from icecream import ic
from mqtt_init import broker_ip, port, topic_temp, topic_actuator, topic_alarm, TEMP_THRESHOLD

# Database Setup
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
    ic("Manager received: " + payload)
    
    try:
        # Extract the number from "Temperature: XX.X"
        temp_value = float(payload.split(": ")[1])
        save_to_db(temp_value)
        
        if temp_value > TEMP_THRESHOLD:
            ic("ALERT! Temperature too high: " + str(temp_value))
            client.publish(topic_alarm, "WARNING: High Temperature!")
            client.publish(topic_actuator, "RELAY: ON")
        else:
            client.publish(topic_actuator, "RELAY: OFF")
            
    except Exception as e:
        ic("Error processing message: " + str(e))

def main():
    init_db()
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker_ip, port)
    client.subscribe(topic_temp)
    
    ic("Data Manager is running and logging to DB...")
    client.loop_forever()

if __name__ == "__main__":
    main()
    