import requests
import subprocess
import os

def generate_password(reference_string):
    reference_string_decremented = ""
    for char in reference_string:
        # Converting chars to ASCII values, decrementing, and converting back to char
        next_char = chr(ord(char) - 1)
        reference_string_decremented += next_char
    return reference_string_decremented

def check_password(password, binary_path="./ELF_02_downloaded"):
    result = subprocess.run([binary_path, password], capture_output=True, text=True)
    if "Yes" in result.stdout:
        return True
    return False

def brute():
    # Étape 1: Téléchargez le fichier
    url = "http://reverse.blackfoot.io:8080/ELF_02"
    response = requests.get(url)
    with open("ELF_02_downloaded", "wb") as file:
        file.write(response.content)
    os.chmod("ELF_02_downloaded", 0o755)

    # Étape 2: Générez le mot de passe
    result = subprocess.run(["strings", "ELF_02_downloaded"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    stringsGet = lines[18]
    if (len(stringsGet) != 20): stringsGet = lines[17]
    print(stringsGet)

    password = generate_password(stringsGet)
    print(password)
    # Étape 3: Vérifiez le mot de passe avec le binaire
    if check_password(password):
        print(f"Password found: {password}")

        # Étape 4: Faites une requête HTTP pour valider le flag
        validate_url = f"http://reverse.blackfoot.io:8080/validate/ELF_02/{password}"
        response = requests.get(validate_url)

        # Étape 5: Vérifiez la réponse
        print(response.text)
        return

    print("Failed to find the correct password.")

brute()

