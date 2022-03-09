from scratch_verify import create_code, verify_code
from time import sleep as delay

username = input("Enter your Scratch username: ")
code = create_code()
print(
    f"Go to https://scratch.mit.edu/projects/440710593 and provide the code {code}"
)

while True:
    delay(2.5)
    if verify_code(username, code):
        break

print(f"Verified as {username}")
