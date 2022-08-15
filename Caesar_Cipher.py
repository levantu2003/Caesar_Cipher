def encrypt_char(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + key) % 26)

def decrypt_messenger(cipher, key):
    messenger = ''
    for c in cipher:
        if c in ' .,':
            messenger = messenger + c
        else:
            messenger = messenger + encrypt_char(c, key)
    return messenger
if __name__ == "__main__":
    cipher = input("Type your messenge you want to decrypt: ")
    key = int(input("Type the key: "))
    print(f"The decrypt messenge is : {decrypt_messenger(cipher, 26 -  key)}");

