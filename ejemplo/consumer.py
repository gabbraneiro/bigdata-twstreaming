from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(
                            'twitter', 
                            bootstrap_servers=['ec2-3-143-249-144.us-east-2.compute.amazonaws.com:9092'], 
                            api_version=(0, 10)
                        )

for message in consumer:
    print(message.value)    

#172.31.43.88