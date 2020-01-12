from collections import defaultdict

fp = open("output.txt", "w")

dict = defaultdict(list)

name = ""
for line in open("./laputa.txt", "r"):
    if line == "\n":
        pass
    else:
        line = line.rstrip()
        lis = line.split("\u3000")
        lis = list(filter(lambda x: x != "", lis))
        if (len(lis) != 1):
            name = lis[0]
            dict[name].append(lis[1])
        else:
            dict[name].append(lis[0])

for name in dict:
    fp.write("------------------------------\n" +
             name + "\n------------------------------\n")
    for serif in dict[name]:
        fp.write(serif + "\n")

fp.close()
