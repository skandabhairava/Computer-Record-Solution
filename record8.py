with open("file.txt", "r") as file:
    original_content = file.read()

content = original_content.replace("Red", "White")
lines = content.split("\n")

lines = [line for line in lines if "Green" not in line]

lines_str = ""
for i in lines:
    lines_str += i + "\n"

print("Before:\n" + content)
print("------")
print("After:\n" + lines_str)