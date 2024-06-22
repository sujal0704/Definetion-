import os

def create_file(file_path):
    try:
        with open(file_path, 'x'):  # 'x' mode creates a new file; fails if file exists
            print(f"File created successfully: {file_path}")
    except FileExistsError:
        print(f"File '{file_path}' already exists.")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def write_file(file_path):
    try:
        with open(file_path, 'w') as file:
            new_content = input(f"Enter new content for {file_path}:\n")
            file.write(new_content)
            print(f"Content written to {file_path} successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def append_file(file_path):
    try:
        with open(file_path, 'a') as file:
            additional_content = input(f"Enter content to append to {file_path}:\n")
            file.write(additional_content + "\n")
            print(f"Content appended to {file_path} successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Create file")
        print("2. Read file")
        print("3. Write to file")
        print("4. Append to file")
        print("5. Remove file")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            file_path = input("Enter file path to create: ")
            create_file(file_path)
        elif choice == '2':
            file_path = input("Enter file path to read: ")
            read_file(file_path)
        elif choice == '3':
            file_path = input("Enter file path to write: ")
            write_file(file_path)
        elif choice == '4':
            file_path = input("Enter file path to append: ")
            append_file(file_path)
        elif choice == '5':
            file_path = input("Enter file path to remove: ")
            remove_file(file_path)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
