import os, zipfile, re, time

def change_file_extension(file_path, new_extension):

    if not new_extension.startswith('.'):
        new_extension = '.' + new_extension

    base = os.path.splitext(file_path)[0]

    new_file_path = base + new_extension

    os.rename(file_path, new_file_path)

    return new_file_path

def unzip_file_to_current_folder(zip_file_path):

    current_folder = os.getcwd()

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(current_folder)

def toggle_ironman_value(file_path, indent_level=1):

    indent_pattern = r'\s' * indent_level
    pattern = re.compile(rf'^{indent_pattern}ironman=(yes|no)$')

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        match = pattern.match(line)
        if match:
            current_value = match.group(1)
            new_value = 'no' if current_value == 'yes' else 'yes'
            modified_line = line.replace(current_value, new_value)
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

def create_zip_with_two_files(file1, file2, zip_name='ironman.zip'):

    with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:

        zipf.write(file1, os.path.basename(file1))
        zipf.write(file2, os.path.basename(file2))

    os.remove(file1)
    os.remove(file2)

new_file = change_file_extension('ironman.sav', '.zip')
unzip_file_to_current_folder('ironman.zip')

file_path_1 = 'gamestate'
file_path_2 = 'meta'

toggle_ironman_value(file_path_1, indent_level=1)
toggle_ironman_value(file_path_2, indent_level=0)

create_zip_with_two_files(file_path_1, file_path_2)

new_file = change_file_extension('ironman.zip', '.sav')

print('finish')
time.sleep(5)