
UPPER_CASE = []
LOWER_CASE = []
OTHER_CHARS = []

with open("file.txt", "r") as file:
    content = file.read()

for char in content:
    if char.isupper():
        UPPER_CASE.append(char)
    elif char.islower():
        LOWER_CASE.append(char)
    else:
        OTHER_CHARS.append(char)

with open("UPPER_CASE.txt", "w") as file:
    file.writelines(UPPER_CASE)
with open("LOWER_CASE.txt", "w") as file:
    file.writelines(LOWER_CASE)
with open("OTHER_CHARS.txt", "w") as file:
    file.writelines(OTHER_CHARS)