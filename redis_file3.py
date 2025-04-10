import redis
from pyexpat.errors import messages

r = redis.Redis(
    host='redis-15067.c289.us-west-1-2.ec2.redns.redis-cloud.com',
    port=15067,
    decode_responses=True,
    username="default",
    password="nbJcWDD2YVC3AAoomZE7jOCRbVIb9dLz",
)


pubsub = r.pubsub()
pubsub.subscribe('school')


for data in pubsub.listen():
    messages = str(data['data'])
    print(messages)
    if "контрольна робота" in messages:
        with open('fiiiiiile', mode='a' , encoding='utf-8') as file:
            file.write(messages + '\n')
