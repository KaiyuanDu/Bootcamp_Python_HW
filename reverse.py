# Project 1 Reverse kdu5

# Define the function to decipher an encrypted message
def decipher_message(encrypted_message):
    decrypted_message = ""
    # Loop through each character in the encrypted message
    for char in encrypted_message:
        # Check if the character is alphabetic
        if char.isalpha():
            # Decipher the character by subtracting its ASCII value from 219
            decrypted_char = chr(219 - ord(char))
            decrypted_message += decrypted_char
        else:
            # If the character is not alphabetic, leave it unchanged
            decrypted_message += char
    return decrypted_message

# Define the main function to take user input and decipher the message
def main():
    # Take input of the encrypted message from the user
    encrypted_message = input("Enter the encrypted message: ")
    # Call the decipher_message function to decrypt the message
    decrypted_message = decipher_message(encrypted_message)
    # Print the decrypted message
    print("The plaintext message is:", decrypted_message)

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function if the script is being run directly
    main()
