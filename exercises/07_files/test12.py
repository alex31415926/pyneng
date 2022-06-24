words = ["duplex", "alias", "configuration"]
string = "Current configuration : 2033 bytes"
n = 0
for word in words:
    if word in string:
        n = n+1
print(n)