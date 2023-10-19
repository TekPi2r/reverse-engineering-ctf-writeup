import requests
import subprocess

# Étape 1: Téléchargez le fichier
url = "http://reverse.blackfoot.io:8080/ELF_01"
response = requests.get(url)
with open("ELF_01_downloaded", "wb") as file:
    file.write(response.content)

# Étape 2: Exécutez `strings` sur le fichier téléchargé
result = subprocess.run(["strings", "ELF_01_downloaded"], capture_output=True, text=True)
lines = result.stdout.splitlines()
# Assumption: Le flag est la première ligne, vous devrez peut-être ajuster cela en fonction du format de sortie
flag = lines[14]
print(flag)

# Étape 3: Faites une requête HTTP pour valider le flag
validate_url = f"http://reverse.blackfoot.io:8080/validate/ELF_01/{flag}"
response = requests.get(validate_url)

# Étape 4: Vérifiez la réponse
print(response.text)

