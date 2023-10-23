# stringsGet1 = "aI6yUVsaHg8FqvZE"
# stringsGet1 = "I6yUVsaHg8FqvZED"
stringsGet1 = "aI6yUVsag8FqvZED"
offset = [2, 3, 2, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
password = ""

for i in range(len(stringsGet1)):
    password += chr(ord(stringsGet1[i]) + offset[i])

print(f"Generated password: {password}")
print(f"Generated password len: {len(password)}")
