import re

with open("input.txt", "r") as f:
    data = f.read()

emails = re.findall(r'\S+@\S+', data)

with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")