#project 2 kdu5
import random
#task 1 encoder
#Define the encoder function


def encode_sequence(string):
    # Initialize an empty string to store the DNA bases
    dna_sequence = ""

    # Iterate through each character in the input string
    for char in string:
        # Get the ASCII value of the character
        ascii_value = ord(char)
        
        # Convert the ASCII value to binary representation
        binary_value = bin(ascii_value)[2:].zfill(8)  # Convert to binary and fill with leading zeros
        
        # Split the binary value into two parts and map each part to a DNA base
        for i in range(0, 8, 2):
            dna_pair = binary_value[i:i+2]
            if dna_pair == '00':
                dna_sequence += 'A'
            elif dna_pair == '01':
                dna_sequence += 'C'
            elif dna_pair == '10':
                dna_sequence += 'G'
            else:
                dna_sequence += 'T'

    return dna_sequence

# Test the function
print(encode_sequence("Frieza"))  # Output: TATCTGACTCCTTCTTTGCCTCAT



def encode_sequence(string):
    # Initialize an empty string to store the DNA bases
    dna_sequence = ""

    # Iterate through each character in the input string
    for char in string:
        # Get the ASCII value of the character
        ascii_value = ord(char)
        
        # Convert the ASCII value to binary representation
        binary_value = bin(ascii_value)[2:].zfill(8)  # Convert to binary and fill with leading zeros
        
        # Split the binary value into two parts and map each part to a DNA base
        for i in range(0, 8, 2):
            dna_pair = binary_value[i:i+2]
            if dna_pair == '00':
                dna_sequence += 'A'
            elif dna_pair == '01':
                dna_sequence += 'C'
            elif dna_pair == '10':
                dna_sequence += 'G'
            else:
                dna_sequence += 'T'

    return dna_sequence

# Test the function
encoded_sequence = encode_sequence("Frieza")
print(encoded_sequence)



#task 3 encryption
def encrypt_decrypt(string, key='CAT'):
    # Initialize an empty string to store the encrypted/decrypted sequence
    result = ""

    # Repeat the key to match the length of the input string
    repeated_key = (key * ((len(string) // len(key)) + 1))[:len(string)]

    # Iterate through each character in the input string and perform XOR with the corresponding key character
    for i in range(len(string)):
        # Perform XOR operation between the ASCII values of the characters
        encrypted_char = chr(ord(string[i]) ^ ord(repeated_key[i]))
        # Append the result to the output string
        result += encrypted_char

    return result


# Test the function with encryption
input_string = "CGGC"
key = "CAT"
encrypted_sequence = encrypt_decrypt(input_string, key)
print("Encrypted Sequence:", encrypted_sequence)  # Output: TAAT

# Test the function with decryption
decrypted_sequence = encrypt_decrypt(encrypted_sequence, key)
print("Decrypted Sequence:", decrypted_sequence)  # Output: CGGC

#task 4 synthesizer


def synthesizer(sequence):
    synthesized_sequence = ""
    for base in sequence:
        # Introduce random errors with 10% probability
        if random.random() < 0.1:
            # Randomly select a different base
            new_base = random.choice(['A', 'C', 'G', 'T'])
            synthesized_sequence += new_base
        else:
            synthesized_sequence += base
    return synthesized_sequence


def error_count(seq1, seq2):
    count = 0
    min_length = min(len(seq1), len(seq2))
    # Compare sequences letter by letter
    for i in range(min_length):
        if seq1[i] != seq2[i]:
            count += 1
    # Add the remaining characters if the sequences have different lengths
    count += abs(len(seq1) - len(seq2))
    return count


# Test Task 4: synthesizer function
original_sequence = "ATCGATCG"
synthesized_sequence = synthesizer(original_sequence)
print("Original Sequence:", original_sequence)
print("Synthesized Sequence:", synthesized_sequence)

# Test Task 5: error_count function
sequence1 = "ATCGATCG"
sequence2 = "ATCGAACG"
mismatch_count = error_count(sequence1, sequence2)
print("Mismatch count between the sequences:", mismatch_count)


def redundancy(n, input_string):
    # Synthesize n copies of the input string
    synthesized_copies = [synthesizer(input_string) for _ in range(n)]

    # Initialize the error-corrected string with the first synthesized copy
    error_corrected_string = synthesized_copies[0]

    # Iterate over each position in the input string
    for i in range(len(input_string)):
        # Initialize a dictionary to store the count of each base at the current position
        base_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        # Count occurrences of each base at the current position across all synthesized copies
        for copy in synthesized_copies:
            base_count[copy[i]] += 1

        # Find the base with the highest count
        correct_base = max(base_count, key=base_count.get)

        # Update the error-corrected string with the correct base at the current position
        error_corrected_string = error_corrected_string[:i] + correct_base + error_corrected_string[i + 1:]

    return error_corrected_string


# Test Task 7: Test the redundancy scheme with different values of n
input_string = "ATCGATCG" * 10  # Sample input string with length 80
n_values = [1, 2, 3, 4, 5]  # Different values of n to test

print("Testing redundancy scheme with different values of n:")
for n in n_values:
    error_corrected_sequence = redundancy(n, input_string)
    error_count_result = error_count(input_string, error_corrected_sequence)
    print(f"For n={n}, Error count: {error_count_result}")
