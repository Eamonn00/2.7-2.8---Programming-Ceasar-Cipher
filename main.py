answer = input(print("Do you want to encrypt or decrypt a message?"))


if answer == "encrypt":
    initial_text = input(print("Enter the message you want to encrypt"))


    index_key = int(input(print("what number do you want to use as your key?")))

    encryption = ""

    for char in initial_text:
        if char.isupper():
             char_code = ord(char)
             char_pos = ord(char) - ord("A")
             new_pos = (char_pos + index_key) % 26
             new_char_code = new_pos + ord("A")
             new_char = chr(new_char_code)
             encryption = encryption + new_char

        elif char.islower(): #
                char_code = ord(char)
                char_pos = ord(char) - ord("a")
                new_pos = (char_pos + index_key) % 26
                new_char_code = new_pos + ord("a")
                new_char = chr(new_char_code)
                encryption = encryption + new_char

        elif c.isdigit():
             new_c = (int(c) + index_key) % 10
             encryption = encryption + str(new_c)

        else:
            encryption = encryption + c

    print(encryption)


elif answer == "decrypt":
        
    initial_text = input(print("Enter the message you want to decrypt"))


    index_key = int(input(print("what number do you want to use as your key?")))


    decryption = ""

    for c in initial_text:
        if c.isupper():
            c_code = ord(c)
            c_pos = ord(c) - ord("A")
            new_pos = (c_pos - index_key) % 26
            new_c_code = new_pos + ord("A")
            new_c = chr(new_c_code)
            decryption = decryption + new_c

        elif c.islower():
            c_code = ord(c)
            c_pos = ord(c) - ord("a")
            new_pos = (c_pos - index_key) % 26
            new_c_code = new_pos + ord("a")
            new_c = chr(new_c_code)
            decryption = decryption + new_c

        elif c.isdigit():
            new_c = (int(c) - index_key) % 10
            decryption = decryption + str(new_c)

        else:
            decryption = decryption + c

    print(decryption)

else:
    print("type encrypt to encrypt a message or decrypt to decrypt one.")