import random
import datetime
import string

def encrypt(message, key):
    """
    Encrypt a message using the specified key and current time.
    
    Args:
    message (str): The original message to encrypt
    key (str): The encryption key
    
    Returns:
    tuple: The encrypted message and the time used for encryption
    """
    # Get current time in HH:MM:SS format
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Prepare encryption
    encrypted_message = []
    key_length = len(key)
    
    # Printable ASCII characters for random insertion
    printable_chars = string.printable[:-5]  # Excludes whitespace and control characters
    
    # Encrypt each character
    for i, char in enumerate(message):
        # Get the corresponding key character (cycling through key)
        key_char = key[i % key_length]
        
        # Add the values of the message and key characters
        encrypted_char = chr((ord(char) + ord(key_char)) % 128)
        encrypted_message.append(encrypted_char)
        
        # Add a random printable ASCII character after each encrypted character
        random_char = random.choice(printable_chars)
        encrypted_message.append(random_char)
    
    return ''.join(encrypted_message), current_time