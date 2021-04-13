encryption = ""

for c in initial_text:
    if c.isupper():
        c_code = ord(c)
        c_pos = ord(c) - ord("A")
        new_pos = (c_pos + key) % 26
        new_c_code = new_pos + ord("A")
        new_c = chr(new_c_code)
        encryption = encryption + new_c

