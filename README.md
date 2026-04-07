# Smart Medical Cold Chain - IoT Project 🏥❄️

## Overview
This project implements an autonomous Medical Cold Chain Monitoring System for vaccine refrigerators. Medical supplies such as vaccines and insulin must be stored strictly between 2°C and 8°C. This IoT system continuously monitors the temperature, logs data to a local database, and autonomously activates a backup cooling generator while triggering visual alerts if the temperature falls out of the safe range.

## System Architecture
The system follows a decentralized IoT architecture using the MQTT protocol:
1. Sensor Node (emulator_dht.py): Simulates a temperature sensor, publishing data every 5 seconds.
2. MQTT Broker: Cloud-based message broker (HiveMQ) handling communication between all components.
3. Data Manager (data_manager.py): The system's "Brain." It subscribes to sensor data, logs it to a local SQLite database, and executes threshold logic.
4. Actuator Node (emulator_actuators.py): Simulates the backup cooling generator that turns ON/OFF based on commands.
5. Manual Reset Button (manual_reset_button.py): An emulator allowing medical staff to acknowledge and reset system alerts.
6. Dashboard (main_gui.py): A real-time graphical user interface (GUI) displaying fridge status, temperature readings, and active alerts.

## Technologies Used
* Language: Python 3
* Communication: MQTT Protocol (Paho-MQTT client)
* Broker: HiveMQ Cloud
* Database: SQLite3
* GUI: Tkinter
* Diagrams: Mermaid.live

## How to Run the Project
To see the system in action, run the components concurrently in separate terminal windows in this exact order:

Terminal 1 (Actuator):
python emulator_actuators.py

Terminal 2 (Data Manager):
python data_manager.py

Terminal 3 (GUI Dashboard):
python main_gui.py

Terminal 4 (Manual Reset Button):
python manual_reset_button.py

Terminal 5 (Sensor Emulator):
python emulator_dht.py

## Security & Automation Highlights
* Authentication: Secure MQTT connection requiring credentials to ensure only authorized devices access the network.
* Validation: Payload validation prevents system crashes from malformed data.
* Encryption: Support for MQTTS (TLS/SSL) to protect sensitive medical data in transit.
* Continuous Monitoring: Designed for 24/7 autonomous operation without human intervention.
