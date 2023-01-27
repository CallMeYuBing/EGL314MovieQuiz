import time
import paho.mqtt.client as mqtt


def on_publish(client, userdata, mid):
    print("message published")

def pubpic(output):
    k = output
    msg = str(k)
    pubMsg = client.publish(
        topic='studentpi/team1', #Please change according to your respective Group  
        payload=msg.encode('utf-8'),
        qos=0,
    )

    pubMsg.wait_for_publish()
    print(pubMsg.is_published())



client = mqtt.Client("mqtt_client1") #this name should be unique to every student group
client.on_publish = on_publish
client.connect('192.168.254.100',1883) #IP address of Gateway Pi
# start a new thread

client.loop_start()