from encrypting_methods import encrypt
from decrypting_methods import decrypt

def encrypt_message():
    original_message = input("Enter a message to encrypt: ")
    encryption_key = input("Enter a key for encryption: ")


    encrypted, encrypt_time = encrypt(original_message, encryption_key)
    
    print(f"Your encrypted a message at {encrypt_time}. Here is your message encrypted:\n{encrypted}")
    

def decrypt_message():
    encrypted = input("Enter a message to decrypt: ")
    encryption_key = input("Enter a key for decryption: ")
    encrypt_time = input("Enter the time when the message was encrypted (HH:MM:SS): ")

    decrypted = decrypt(encrypted, encryption_key, encrypt_time)
    print("Decrypted message:", decrypted)
    

while True:
    print("Welcome to the encryption program!")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")
    if choice == '1':
        encrypt_message()
    elif choice == '2':
        decrypt_message()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")