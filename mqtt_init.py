broker_ip = "broker.hivemq.com"
port = 8883
username = "admin" 
password = "secure_password_123"

my_id = "5976397"
comm_topic = "pr/medical/" + my_id + "/"   
topic_temp = comm_topic + "sts"
topic_actuator = comm_topic + "act"
topic_alarm = comm_topic + "alarm"
topic_control = comm_topic + "control"

MIN_TEMP = 2.0 
MAX_TEMP = 8.0