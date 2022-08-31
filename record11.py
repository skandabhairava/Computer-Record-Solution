with open("Rhyme.txt", "r") as file:
    content = file.read()

idx = 0
main_str = ""

for line in content.split("\n"):
    if line == "":
        continue
    for word in line.split(" "):
        main_str += str(idx) + " "
        idx += 1
    main_str += "\n"

with open("RhymeIndex.txt", "w") as file:
    file.write(main_str)
with open("RhymeIndex.txt", "r") as file:
    print(file.read())