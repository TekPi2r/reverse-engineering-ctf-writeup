# Les 3 premiers octets courants pour le prologue d'une fonction
prologues = [
    [0x55, 0x48, 0x89],
    [0x53, 0x48, 0x83],
    [0x48, 0x83, 0xEC]
]

# Les 3 premiers octets de la clé en dur
key_first_three = [0x2f, 0xb9, 0x87]

# Calcul du XOR pour obtenir les trois premiers octets du mot de passe
for j in range(len(prologues)):
    password_first_three = ''.join([chr(prologues[j][i] ^ key_first_three[i]) for i in range(3)])
    print("Les trois premiers caractères du mot de passe sont:", password_first_three)
