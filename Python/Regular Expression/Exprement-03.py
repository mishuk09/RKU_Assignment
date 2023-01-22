import re
phone = "007069089661"

result = re.sub(r'^', "", phone)
print(result)

# add something

result = re.sub(r'\d', "91", phone)
print(result)
