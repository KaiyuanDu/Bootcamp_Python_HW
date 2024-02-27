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
            dna_pair = binary_value[i:i + 2]
            if dna_pair == '00':
                dna_sequence += 'A'
            elif dna_pair == '01':
                dna_sequence += 'T'
            elif dna_pair == '10':
                dna_sequence += 'C'
            else:
                dna_sequence += 'G'

    return dna_sequence


#task 2 decoder


def decode_sequence(dna_sequence):
    # Initialize an empty string to store the decoded text
    decoded_text = ""

    # Iterate through the DNA sequence in chunks of 4
    for i in range(0, len(dna_sequence), 4):
        # Get the DNA group of 4 bases
        dna_group = dna_sequence[i:i + 4]

        # Decode the DNA group into a character
        binary_value = ""
        for base in dna_group:
            if base == 'A':
                binary_value += '00'
            elif base == 'T':
                binary_value += '01'
            elif base == 'C':
                binary_value += '10'
            elif base == 'G':
                binary_value += '11'
            else:
                # Handle unrecognized DNA base
                raise ValueError("Unrecognized DNA base: " + base)

        # Convert the binary value to ASCII and then to character
        decoded_char = chr(int(binary_value, 2))

        # Append the decoded character to the string
        decoded_text += decoded_char

    return decoded_text


def encrypt_decrypt(string, key="CAT"):
    bases = ('A', 'T', 'C', 'G')
    # If the length of the key is 0, terminate recursion
    if len(key) == 0:
        # When the base case is reached, return the encrypted/decrypted string
        return string

    encrypted = ""
    # Determine the index of the first letter of the key in the bases
    key_index = bases.index(key[0])

    # Iterate through the entire string to ensure each character is encrypted
    while len(string) > 0:
        # Determine the index of the first letter of the string in the bases
        string_index = bases.index(string[0])
        # Use the XOR operator to find the new index associated with the encrypted/decrypted character in the bases
        index = string_index ^ key_index
        # Construct the encrypted/decrypted string character by character
        encrypted += bases[index]
        # Update the string variable to change the loop condition
        string = string[1::]

    # The method recursively calls itself until the length of the key reaches 0
    return encrypt_decrypt(encrypted, key[1::])

# Test the function


encrypted_result = encrypt_decrypt("TAAT")
print("Encrypted:", encrypted_result)

decrypted_result = encrypt_decrypt(encrypted_result)
print("Decrypted:", decrypted_result)

#task 4 synthesizer


def synthesizer(sequence):
    # Define the mapping of bases
    base_mapping = {'A': ['A', 'C', 'G', 'T'],
                    'C': ['C', 'A', 'T', 'G'],
                    'G': ['G', 'T', 'C', 'A'],
                    'T': ['T', 'G', 'A', 'C']}

    # Initialize an empty string to store the synthesized DNA sequence
    synthesized_sequence = ""

    # Iterate through each base in the input sequence
    for base in sequence:
        # Randomly select a base from the mapping
        rand = random.random()

        if base.__eq__('A'):
            synthesized_sequence += 'A'
        if base.__eq__('T'):
            add = 'G' if rand < 0.02 else 'C' if rand < 0.05 \
                else 'A' if rand < 0.10 else 'T'
            synthesized_sequence += add
        if base.__eq__('C'):
            add = 'A' if rand < 0.01 else 'T' if rand < 0.02 \
                else 'G' if rand < 0.03 else 'C'
            synthesized_sequence += add
        if base.__eq__('G'):
            add = 'A' if rand < 0.01 else 'T' if rand < 0.03 \
                else 'C' if rand < 0.05 else 'G'
            synthesized_sequence += add

    return synthesized_sequence



def error_count(seq1, seq2):
    count = 0
    min_length = min(len(seq1), len(seq2))
    # Compare sequences letter by letter
    for i in range(len(seq1)):
        if not seq1[i].__eq__(seq2[i]):
            count += 1
    # Add the remaining characters if the sequences have different lengths
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
