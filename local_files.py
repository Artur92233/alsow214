import requests

url = 'https://reedhoffmann.com/wp-content/uploads/2022/03/JPEG_007.jpeg'

response = requests.get(url)

with open('spring.jpg', mode='wb') as file:
    content = response.content
    # content += b'23235656 Vasja'
    file.write(content)

with open('spring.jpeg', mode='rb') as f:
    print(f.read())
pass