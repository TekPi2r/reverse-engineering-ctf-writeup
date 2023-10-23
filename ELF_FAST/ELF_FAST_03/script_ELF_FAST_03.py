import requests
import subprocess
import os

def generatePassword(part1, part2):
    local_values = [2, 3, 2, 3, 5]
    password = ""
    for i in range(len(part1)):
        password += chr(ord(part1[i]) + local_values[i])
        if (i == len(local_values) - 1): break
    return password


def check_password(password, binary_path="./ELF_03_downloaded"):
    result = subprocess.run([binary_path, password], capture_output=True, text=True)
    if "Yes" in result.stdout:
        return True
    return False

# # Étape 1: Téléchargez le fichier
# url = "http://reverse.blackfoot.io:8080/ELF_03"
# response = requests.get(url)
# with open("ELF_03_downloaded", "wb") as file:
#     file.write(response.content)
# os.chmod("ELF_03_downloaded", 0o755)

# Étape 2: Exécutez `strings` sur le fichier téléchargé
result = subprocess.run(["strings", "ELF_03_downloaded"], capture_output=True, text=True)
lines = result.stdout.splitlines()
part1 = lines[12]
part2 = lines[13]

if len(part1) != len("g5Eeil7QH"):
    part1 = lines[13]
    part2 = lines[14]
print(part1)
print(part2)

password = generatePassword(part1, part2)
# Étape 3: Vérifiez le mot de passe avec le binaire
if check_password(password):
    print(f"Password found: {password}")

    # # Étape 4: Faites une requête HTTP pour valider le flag
    # validate_url = f"http://reverse.blackfoot.io:8080/validate/ELF_03/{password}"
    # response = requests.get(validate_url)

    # # Étape 5: Vérifiez la réponse
    # print(response.text)
    exit(0)

print("Failed to find the correct password.")
