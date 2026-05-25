import os

folder_name = "DecodeLabs_Automation"
file_name = "welcome_message.txt"
file_path = os.path.join(folder_name, file_name)

print("Starting automation task...")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print("Folder created.")
else:
    print("Folder already exists.")

welcome_text = "Welcome to DecodeLabs!"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(welcome_text)
    print("Data written to file.")

print("Reading file content:")
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

print("Task completed.")