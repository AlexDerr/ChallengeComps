new_list = []

with open("comps.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if int(line[0]) >= 6:
        new_list.append(line)

with open("comps 6+.txt", "w") as f:
    f.writelines(new_list)