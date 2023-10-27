import string
import subprocess

# Les valeurs de DAT_00012008 que vous avez trouvées dans GDB
data = [0x2f, 0xb9, 0x87, 0xc2, 0xfe, 0x98, 0x95, 0x8e, 0xeb, 0x96, 0x6d, 0xa1]

# Tous les caractères ASCII imprimables que vous souhaitez tester
chars = string.ascii_letters + string.digits  # Lettres majuscules et minuscules + chiffres

def is_printable(s):
    """Vérifie si tous les caractères de la chaîne sont imprimables"""
    return all(c in string.printable for c in s)

def test_password(password):
    """Exécutez le binaire avec le mot de passe et vérifiez s'il renvoie 'Yes'"""
    try:
        result = subprocess.run(['./simple_binary', password], capture_output=True, text=True, timeout=2)
        return "Yes" in result.stdout
    except subprocess.TimeoutExpired:
        print(f"Timeout for password: {password}")
        return False
    except Exception as e:
        return False


# Testez toutes les combinaisons possibles de 3 caractères
charsK = chars[len('abcdefghij'):len(chars)]
for c1 in charsK:
    for c2 in chars:
        for c3 in chars:
            password = c1 + c2 + c3
            print(f"Test: {password}")
            if test_password(password):
                print(f"Flag found: {password}")
                exit(0)  # Arrête le script s'il trouve le bon mot de passe
