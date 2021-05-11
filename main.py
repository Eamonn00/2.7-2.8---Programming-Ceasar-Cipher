answer = input(print("Do you want to encrypt or decrypt a message?"))


if answer == "encrypt":
    initial_text = input(print("Enter the message you want to encrypt."))

    try:
        index_key = int(input(print("What number do you want to use as your key?")))
    except:
        print("Type a whole number to use as the key.")
        
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

        elif char.isdigit():
             new_char = (int(char) + index_key) % 10
             encryption = encryption + str(new_char)

        else:
            encryption = encryption + char

    print(encryption)


elif answer == "decrypt":
        
    initial_text = input(print("Enter the message you want to decrypt."))

    try:
        index_key = int(input(print("What number do you want to use as your key?")))
    except:
        print("Type a whole number to use as the key.")

    decryption = ""

    for char in initial_text:
        if char.isupper():
            char_code = ord(char)
            char_pos = ord(char) - ord("A")
            new_pos = (char_pos - index_key) % 26
            new_char_code = new_pos + ord("A")
            new_char = chr(new_char_code)
            decryption = decryption + new_char

        elif char.islower():
            char_code = ord(char)
            char_pos = ord(char) - ord("a")
            new_pos = (char_pos - index_key) % 26
            new_char_code = new_pos + ord("a")
            new_char = chr(new_char_code)
            decryption = decryption + new_char

        elif char.isdigit():
            new_char = (int(char) - index_key) % 10
            decryption = decryption + str(new_char)

        else:
            decryption = decryption + char

    print(decryption)

else:
    print("Type encrypt to encrypt a message or decrypt to decrypt one.")