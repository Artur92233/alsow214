import base64
import io
import pyotp
import qrcode

secret = "hgjkgjkhkk"

totp = pyotp.TOTP(secret)

# otp_user = input('Your otp: ')
# is_valid = totp.verify(otp_user)
# print(is_valid)

uri = totp.provisioning_uri(
    name="user2@example.com",
    issuer_name="MyApp2",
    image="https://cdn.hexnode.com/blogs/wp-content/uploads/2023/03/15084406/App-management-101-Cover-Image.png",
)
print(uri)
qr = qrcode.make(uri)
qr.show()
qr.save("hh.png")

buffer = io.BytesIO()
qr.save(buffer, format="PNG")

base64_qr = base64.b64encode(buffer.getvalue()).decode()
print(base64_qr)

print(f"data:image/png;base64,{base64_qr}")
