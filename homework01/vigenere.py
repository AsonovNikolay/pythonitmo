def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for indx, ch in enumerate(plaintext):
        if ch.isalpha():
            if ch.islower():
                ciphertext += alphabet[
                     (alphabet.index(ch) + alphabet.index(keyword[indx % len(keyword)].lower())) % len(alphabet)]
            else:
                ciphertext += alphabet[
                    (alphabet.index(ch.lower()) + alphabet.index(keyword[indx % len(keyword)].lower())) % len(alphabet)].upper()
        else:
            ciphertext += ch

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for indx, ch in enumerate(ciphertext):
        if ch.isalpha():
            if ch.islower():
                plaintext += alphabet[
                    (alphabet.index(ch) - alphabet.index(keyword[indx % len(keyword)].lower())) % len(alphabet)]
            else:
                plaintext += alphabet[
                    (alphabet.index(ch.lower()) - alphabet.index(keyword[indx % len(keyword)].lower())) % len(
                        alphabet)].upper()
        else:
            plaintext += ch
    return plaintext
