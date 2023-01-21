

# Regular expression


# There are many regular expression
# findall,  search,  split,  sub,  finditer


# match

import re
name = r"color"

if re.match(name, "Color red is my fav color"):
    print("Match")
else:
    print("Not match")
