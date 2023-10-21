def decode_function(key, data):
    decoded = []
    key_len = len(key)
    for i in range(len(data)):
        decoded_char = chr(data[i] ^ ord(key[i % key_len]))
        decoded.append(decoded_char)
    return "".join(decoded)

def is_printable_ascii(s):
    return all(32 <= ord(c) < 127 for c in s)

def brute_force_key(data):
    for i in range(32, 127):  # ASCII printable characters
        for j in range(32, 127):
            for k in range(32, 127):
                key = chr(i) + chr(j) + chr(k)
                decoded_data = decode_function(key, data)
                if is_printable_ascii(decoded_data):
                    print(f"Potential Key: {key}, Decoded Data: {decoded_data}")

data = [0x2F, 0xB9, 0x87, 0xC2, 0xFE, 0x98, 0x95, 0x8E, 0xEB, 0x96, 0x6D, 0xA1]
brute_force_key(data)
