in_file = open("switch.txt", 'r')
switch = in_file.read()
print(switch)
in_file.close()
if switch == "on\n":
    switch = "off"
else:
    switch = "on"
print(switch)
out_file = open("switch.txt", 'w')
print(switch, file=out_file)
out_file.close()
