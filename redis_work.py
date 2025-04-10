import redis

r = redis.Redis(
    host='redis-15067.c289.us-west-1-2.ec2.redns.redis-cloud.com',
    port=15067,
    decode_responses=True,
    username="default",
    password="nbJcWDD2YVC3AAoomZE7jOCRbVIb9dLz",
)



r.set('favouriteCar', 'ToyotaCorolla')

r.set('myPet', 'Monya' , ex=7200)

r.rpush('productsList', 'cheese', 'bacon' , 'milk' , 'banana')
r.expire('productsList' , 604800)

r.hset('ingrudients', mapping={'flour': 250, 'milk': 500 , 'eggs': 3 , 'salt': 5})
r.hset('ingrudients', mapping={'sugar': 300})
r.hset('ingrudients', mapping={'sugar': 500})
r.delete('ingrudients')


