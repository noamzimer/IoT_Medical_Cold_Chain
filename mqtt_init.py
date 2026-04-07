import socket

broker_ip = "broker.hivemq.com"
port = 1883
username = "" 
password = ""

my_id = "5976397"
comm_topic = "pr/home/" + my_id + "/"

topic_temp = comm_topic + "sts"
topic_actuator = comm_topic + "act"
topic_alarm = comm_topic + "alarm"

TEMP_THRESHOLD = 28.0
