stringsGet = "MasKerade133742A"
offsetTab = [2, 3, 2, 3, 5]
password = ""

for i in range(len(offsetTab)):
    password += chr(ord(stringsGet[i]) + offsetTab[i])

password = password + stringsGet[5:16]
print(f"Generated password: {password}")
print(f"Generated password len: {len(password)}")

# Password should start with "OduNjra"
