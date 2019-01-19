emptybytes = bytes(4)
print(emptybytes)
print(type(emptybytes))

# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)


print()
# integer to bytes
i = 16

# Create one byte from the integer 16
single_byte = i.to_bytes(1, byteorder='big', signed=True)
print(single_byte)

# Create four bytes from the integer
four_bytes = i.to_bytes(4, byteorder='big', signed=True)
print(four_bytes)

# Compare the difference to little endian
print(i.to_bytes(4, byteorder='little', signed=True))

# Create bytes from a list of integers with values from 0-255
bytes_from_list = bytes([255, 254, 253, 252])
print(bytes_from_list)

# Create a byte from a base 2 integer
one_byte = int('11110000', 2)
print(one_byte)

# Print out binary string (e.g. 0b010010)
print(bin(22))



print('\n')
# bytes to integer:

# Create an int from bytes. Default is unsigned.
some_bytes = b'\x00\xF0'
i = int.from_bytes(some_bytes, byteorder='big')
print(i)

# Create a signed int
i = int.from_bytes(b'\x00\x0F', byteorder='big', signed=True)
print(i)

# Use a list of integers 0-255 as a source of byte values
i = int.from_bytes([255, 0, 0, 0], byteorder='big')
print(i)



print('\n\n')
#  TEXT ENCODING

# Binary to Text
binary_data = b'I am text.'
print(binary_data)
text = binary_data.decode('utf-8')
print(text)

binary_data = bytes([65, 66, 67])  # ASCII values for A, B, C
print(binary_data)
print(type(binary_data))
text = binary_data.decode('utf-8')
print(text)

# Text to Binary
message = "Hello"  # str
binary_message = message.encode('utf-8')
print(type(binary_message))  # bytes

# Python has many built in encodings for different languages,
# and even the Caeser cipher is built in
import codecs
cipher_text = codecs.encode(message, 'rot_13')
print(cipher_text)
