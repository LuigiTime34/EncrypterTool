def decrypt(encrypted_message, key, encryption_time):
    """
    Decrypt a message that was encrypted using the specified key and time.
    
    Args:
    encrypted_message (str): The message to decrypt
    key (str): The decryption key
    encryption_time (str): The time used during encryption
    
    Returns:
    str: The original decrypted message
    """
    # Remove random characters (every other character)
    cleaned_message = []
    for i in range(0, len(encrypted_message), 2):
        cleaned_message.append(encrypted_message[i])
    
    decrypted_message = []
    key_length = len(key)
    
    # Decrypt each character
    for i, char in enumerate(cleaned_message):
        # Get the corresponding key character (cycling through key)
        key_char = key[i % key_length]
        
        # Subtract the key character value to get original character
        decrypted_char = chr((ord(char) - ord(key_char)) % 128)
        decrypted_message.append(decrypted_char)
    
    return ''.join(decrypted_message)