ssn = input()
ssnList = ssn.split("-")
ssnStr = "".join(ssnList)

# print(ssn)
# print(ssnList)
# print(ssnStr)

if len(ssn) != 11:
    print("Invalid SSN")
elif len(ssnList[0]) != 3 or len(ssnList[1]) != 2 or len(ssnList[2]) != 4:
    print("Invalid SSN")
elif not ssnStr.isdigit():
    print("Invalid SSN")
else:
    print("Valid SSN")
