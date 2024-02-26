#project 1 shifted kdu5
# Define the function to decipher an encrypted message
def decipher_message(encrypted_message):
    decrypted_message = ""
    #Loop through each character in the encrypted message
    for char in encrypted_message:
        # Check if the character is alphabetic
        if char.isalpha():
            # Decipher the character by shifting it back by 3 positions
            decrypted_char = chr(((ord(char) - ord('a') - 3) % 26) + ord('a'))
            decrypted_message += decrypted_char
        # If the character is not alphabetic (e.g. space), leave it unchanged
        else:
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
