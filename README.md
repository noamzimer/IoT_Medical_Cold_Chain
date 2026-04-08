# ❄️🏥 Smart Medical Cold Chain - IoT Project

## 📌 Overview
This project implements an **Autonomous Medical Cold Chain Monitoring System** for vaccine refrigerators.

Medical supplies such as vaccines and insulin must be stored strictly between **2°C and 8°C**.  
This IoT-based system continuously monitors temperature, logs data locally, and automatically reacts to abnormal conditions.

### 🚀 Key Capabilities
- Real-time temperature monitoring
- Automatic activation of backup cooling system
- Visual alerts for abnormal conditions
- Data logging to local database
- Manual human intervention (ACK/reset)

---

## 🏗️ System Architecture

The system uses a decentralized IoT architecture based on the **MQTT protocol** with a secure cloud broker.

### 🧠 Components

- **`data_manager.py`**  
  The "brain" of the system:
  - Processes incoming sensor data  
  - Stores data in **SQLite database**  
  - Applies threshold logic  
  - Sends commands to actuators  

- **`emulator_actuators.py`**  
  Simulates a cooling system (relay/generator) that:
  - Turns ON/OFF based on commands  

- **`main_gui.py`**  
  A **Tkinter-based dashboard** displaying:
  - Current temperature  
  - System status  
  - Active alerts  

- **`manual_reset_button.py`**  
  Simulates a human operator:
  - Allows acknowledgment (ACK) of alerts  
  - Resets system after critical events  

- **`emulator_dht.py`**  
  Simulates a **DHT22 sensor**:
  - Publishes temperature every 5 seconds  

---

## 🛠️ Technologies Used

- **Language**: Python 3  
- **Protocol**: MQTT (`paho-mqtt >= 1.6`)  
- **Broker**: HiveMQ Cloud  
- **Database**: SQLite3  
- **GUI**: Tkinter  
- **Security**: TLS/SSL Encryption & Authentication  

---

## ⚙️ Installation

Install required dependencies:
pip install paho-mqtt icecream

▶️ How to Run
Run each component in a separate terminal in this exact order:
# Terminal 1 - Data Manager
python data_manager.py

# Terminal 2 - Actuator
python emulator_actuators.py

# Terminal 3 - GUI Dashboard
python main_gui.py

# Terminal 4 - Manual Reset Button
python manual_reset_button.py

# Terminal 5 - Sensor Emulator
python emulator_dht.py

## 🔐 Security & Features

### 🔑 Authentication
Requires valid credentials for HiveMQ Cloud broker

### 🔒 Encryption
Uses secure MQTTS (TLS/SSL) on port 8883

### 🧪 Data Validation
- Robust error handling using `try-except`
- Validates incoming MQTT payloads

### 🤖 Automation
Fully autonomous system response to temperature deviations

### 👩‍⚕️ Human-in-the-Loop
Manual acknowledgment required after critical alerts

## 📊 System Logic

- ✅ **Normal Range:** 2°C – 8°C  

- ⚠️ **Out of Range:**
  - Alert triggered  
  - Cooling system activated  

- 🔁 **Reset:**
  - Requires manual ACK from operator  

## 💡 Use Case

Designed for:

- Hospitals 🏥  
- Clinics  
- Pharmacies  
- Vaccine storage facilities  
