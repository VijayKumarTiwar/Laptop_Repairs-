import os

def replace_in_file(file_path, search_text, replace_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if search_text in content:
            new_content = content.replace(search_text, replace_text)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except:
        pass
    return False

root_dir = 'd:\\Projects\\Laptop'
extensions = ['.html', '.css', '.py', '.js']

replacements = [
    ('Tiwari', 'Tiwari'),
    ('tiwari', 'tiwari'),
    ('Tiwari', 'Tiwari'),
    ('tiwari', 'tiwari')
]

for root, dirs, files in os.walk(root_dir):
    # Skip directories
    if '.git' in dirs:
        dirs.remove('.git')
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')
        
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            file_path = os.path.join(root, file)
            for search_text, replace_text in replacements:
                replace_in_file(file_path, search_text, replace_text)

print("Optimized revert complete.")
