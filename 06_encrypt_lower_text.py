encryption = ""

for c in initial_text:
    if c.islower():
        c_code = ord(c)
        c_pos = ord(c) - ord("a")
        new_pos = (c_pos + index_key) % 26
        new_c_code = new_pos + ord("a")
        new_c = chr(new_c_code)
        encryption = encryption + new_c