def compute(param_1):
    uVar6 = 0
    while True:
        if len(param_1) <= uVar6:
            return param_1
        for uVar5 in range(len(param_1)):
            if uVar5 % 2 == 0:
                if uVar6 % 2 == 0:
                    param_1 = param_1[:uVar5] + chr(ord(param_1[uVar5]) + 5) + param_1[uVar5+1:]
                else:
                    param_1 = param_1[:uVar5] + chr(ord(param_1[uVar5]) - 5) + param_1[uVar5+1:]
            else:
                if uVar6 % 2 == 0:
                    param_1 = param_1[:uVar5] + chr(ord(param_1[uVar5]) - 5) + param_1[uVar5+1:]
                else:
                    param_1 = param_1[:uVar5] + chr(ord(param_1[uVar5]) + 5) + param_1[uVar5+1:]

        # Comme ptrace renvoie toujours -1, nous sortons immédiatement de la boucle après avoir effectué les transformations
        break

    return param_1


# Example usage
param = "lllloworldabcdef"
result = compute(param)
print(result)
