# Function to encrypt the text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            decrypted_text += char
    return decrypted_text

# Main function to get user input and perform encryption/decryption
def main():
    # Take user input for message and shift value
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    # Encrypt the text
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")

# Run the program
if __name__ == "__main__":
    main()
