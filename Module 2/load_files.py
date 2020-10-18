import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

print(file_path)

# Чтобы прикрпеить файл, нужно отправить его путь
# element.send_keys(file_path)