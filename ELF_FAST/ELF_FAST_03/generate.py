stringsGet1 = "aI6yUVsaHg8FqvZE"
offset = [2, 3, 2, 3, 5]
password = ""

for i in range(len(stringsGet1)):
    password += chr(ord(stringsGet1[i]) - offset[i % 5])

print(f"Generated password: {password}")
print(f"Generated password len: {len(password)}")
