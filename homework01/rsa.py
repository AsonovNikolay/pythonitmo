import random
import typing as tp


def is_prime(n: int) -> bool:
    main = []
    if n == 1:
        return False
    for x in range(1, n):
        if n % x == 0:
            main.append(x)
    if len(main) > 1:
        print("False")
        return False
    return True


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def multiplicative_inverse(e: int, phi: int) -> int:
    main = [[], []]
    ost = e % phi
    A = e
    B = phi
    main[0].append(A)
    main[1].append(B)
    step = 1
    while ost != 0 :
        A, B, ost = B, ost, B % ost
        step += 1
        main[0].append(A)
        main[1].append(B)
    x = 0
    y = 1
    for i in range(step, 1, -1):
        c = x
        x = y
        y = c - y * (main[0][i - 2] // main[1][i - 2])
        #print(main[0][i - 2], main[1][i-2])
    return(x % phi)

def generate_keypair(p: int, q: int):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    # PUT YOUR CODE HERE

    phi = (p-1) * (q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
