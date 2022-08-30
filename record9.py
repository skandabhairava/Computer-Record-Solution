with open("file.txt", "r") as file:
    content = file.read()

content = content.split("\n")
content = [line + "\n" for line in content if "a" not in line.lower()]

with open("file2.txt", "w") as file:
    file.writelines(content)