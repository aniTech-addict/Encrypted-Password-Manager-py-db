def xor_encrypt_decrypt(raw_psw, master_key):
    """
    Encrypts or decrypts a password using the XOR cipher.

    This function iterates through each character of the raw password, XORs it with a character from the key,
    and concatenates the resulting characters to form the encrypted/decrypted password.

    :param raw_psw: The password to be encrypted or decrypted (string).
    :param master_key: The encryption/decryption key (string).
    :return: The encrypted or decrypted password (string).

    """
    encrypted_chars=[]
    for i in range(len(raw_psw)):
        char = raw_psw[i]
        key_char = master_key[i % len(master_key)]
        encrypted_chars.append(chr(ord(char) ^ ord(key_char)))

    encrypted_psw = "".join(encrypted_chars)
    return encrypted_psw