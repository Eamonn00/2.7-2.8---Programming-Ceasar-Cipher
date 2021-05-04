encryption = ""

for c in initial_text:
    if c.isdigit():
        new_c = (int(c) + index_key) % 10
        encryption = encryption + new_c