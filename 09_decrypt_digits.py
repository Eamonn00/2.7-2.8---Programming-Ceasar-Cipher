decryption = ""

for c in initial_text:
    if c.isdigit():
        new_c = (int(c) - index_key) % 10
        decryption = decryption + new_c