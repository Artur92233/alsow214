import redis

r = redis.Redis(
    host='redis-15067.c289.us-west-1-2.ec2.redns.redis-cloud.com',
    port=15067,
    decode_responses=True,
    username="default",
    password="nbJcWDD2YVC3AAoomZE7jOCRbVIb9dLz",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

