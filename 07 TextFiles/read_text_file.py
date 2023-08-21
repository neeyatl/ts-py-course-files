jabberpath = "C:/Users/Neeyat/Documents/Python Projects/Tim Buchalka Python Course/07 TextFiles/Jabberwocky.txt"
# mytxt = open(jabberpath, 'r')   # not the best way

# for line in mytxt:
#     # print(line, end="")
#     print(line.rstrip())
    
# mytxt.close()

with open(jabberpath, 'r') as txt:
    for line in txt:
        print(line, end='')