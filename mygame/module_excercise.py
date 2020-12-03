import re

re_module = []
for member in dir(re):
    if "find" in member:
        re_module.append(member)

print(sorted(re_module))
