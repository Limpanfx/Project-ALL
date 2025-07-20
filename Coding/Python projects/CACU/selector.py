import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, 'Images', 'Logo.png')
    os.startfile(image_path)

def list_files(folder_name):
    files = [f for f in os.listdir(folder_name) if f.endswith('.txt')]

    for idx, f in enumerate(files, start=1):
        print(f"{idx}. {f[:-4]}")

    try:
        choice = int(input("\nSelect a number to view contents: "))
        if 1 <= choice <= len(files):
            filename = files[choice - 1]
            with open(os.path.join(folder_name, filename), 'r', encoding='utf-8') as file:
                clear()
                print(f"--- {filename[:-4]} ---\n")
                print(file.read())
                reload()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("Select an option:")
    print("1. Files")
    print("2. Entity Backgrounds")
    print("3. Personal information")
    choice = input("Enter 1, 2 or 3: ")
    clear()

    if choice == '1':
        list_files("Files")
    elif choice == '2':
        list_files("Entity Backgrounds")
    elif choice == '3':
        logo()
        list_files("Personal information")
    else:
        print("Invalid choice.")
        reload()

def reload():
    input("\nPress Enter to reload the menu: ")
    clear()
    main()

clear()
main()
