# Smart Medical Cold Chain - IoT Project 🏥❄️

## Overview
This project simulates an autonomous **Medical Cold Chain Monitoring System** for vaccine refrigerators. Certain medical supplies (like vaccines and insulin) must be stored strictly between **2°C and 8°C**. 
This IoT system continuously monitors the temperature, logs the data to a database, and autonomously activates a backup cooling generator while triggering an alert if the temperature falls out of the safe range.

## System Architecture
The system is built using a decentralized IoT architecture over the MQTT protocol:
1. **Sensor Node (`emulator_dht.py`):** Simulates a temperature sensor inside the vaccine fridge, publishing data every 5 seconds.
2. **MQTT Broker:** Cloud-based message broker (HiveMQ) that handles the communication between all components.
3. **Data Manager (`data_manager.py`):** The "Brain" of the system. It subscribes to sensor data, logs it to a local SQLite database, and executes the business logic (threshold validation).
4. **Actuator Node (`emulator_actuators.py`):** Simulates the backup cooling generator that turns ON/OFF based on the Manager's commands.
5. **Dashboard (`main_gui.py`):** A real-time graphical user interface (GUI) built with Tkinter, displaying the current fridge status, temperature, and active alerts.

## Technologies Used
* **Language:** Python 3
* **Communication:** MQTT Protocol (Paho-MQTT client)
* **Broker:** HiveMQ Cloud (`broker.hivemq.com`)
* **Database:** SQLite3 (`project_db.sqlite`)
* **GUI:** Tkinter
* **Debugging:** IceCream (`ic`)

## How to Run the Project
To see the system in action, you need to run the components concurrently in separate terminal windows. **Please follow this exact order:**

**Terminal 1 (Actuator):**
Runs the backup cooling system listener.
    python emulator_actuators.py

**Terminal 2 (Data Manager):**
Starts the logic and database logger.
    python data_manager.py

**Terminal 3 (GUI Dashboard):**
Opens the visual interface for the medical staff.
    python main_gui.py

**Terminal 4 (Sensor Emulator):**
Starts generating and publishing temperature data. (Run this last so the other components catch the first readings).
    python emulator_dht.py

## Security & Automation Highlights
* **Authentication:** Ready for MQTT username/password integration.
* **Validation:** Payload validation prevents system crashes from malformed sensor data.
* **Continuous Monitoring:** Designed to run 24/7 autonomously without human intervention.
