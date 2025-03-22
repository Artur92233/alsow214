import datetime
import time
import jwt

secret = "kjhkjjjjhikhkjk"
false_secret = "aaaaaaaaaaa"
payload = {
    "name": "Artur",
    "age": 14,
    "favourite_city": "San Jose",
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=500),
}

encode_jwt = jwt.encode(payload=payload, key=secret, algorithm="HS256")
print(encode_jwt)
# time.sleep(15)

decoded = jwt.decode(
    encode_jwt,
    false_secret,
    algorithms=["HS256"],
    # options={
    #     'verify_signature': False
    # }
)
print(decoded)
