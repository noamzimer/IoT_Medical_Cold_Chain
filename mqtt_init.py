import socket

broker_ip = "broker.hivemq.com"
port = 1883
username = "" 
password = ""

my_id = "5976397"
comm_topic = "pr/medical/" + my_id + "/"   
topic_temp = comm_topic + "sts"
topic_actuator = comm_topic + "act"
topic_alarm = comm_topic + "alarm"

# Medical Cold Chain Thresholds (Vaccine Safe Range)
MIN_TEMP = 2.0 
MAX_TEMP = 8.0
