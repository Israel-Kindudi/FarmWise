def remove_null_bytes(filename):
    with open(filename, 'rb') as file:
        content = file.read()

    cleaned_content = content.replace(b'\x00', b'')

    with open(filename, 'wb') as file:
        file.write(cleaned_content)

# Replace 'your_file.py' with the path to your problematic file
remove_null_bytes(f"__init__.py")
