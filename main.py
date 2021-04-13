#ask user for text to encrypt

initial_text = input(print("Enter the message you want to encrypt"))

#ask user for encryption key

index_key = int(input(print("what number do you want to use as your key?")))

#encrypt uppercase letters

encryption = ""

for c in initial_text:
    if c.isupper():
        c_code = ord(c)
        c_pos = ord(c) - ord("A")
        new_pos = (c_pos + index_key) % 26
        new_c_code = new_pos + ord("A")
        new_c = chr(new_c_code)
        encryption = encryption + new_c

