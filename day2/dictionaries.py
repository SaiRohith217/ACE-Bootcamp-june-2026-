def print_menu():
    print("\nBasic Dictionary Program")
    print("1. Show dictionary")
    print("2. Add / update entry")
    print("3. Get value by key")
    print("4. Remove entry")
    print("5. Show keys")
    print("6. Show values")
    print("7. Show items")
    print("8. Exit")


def main():
    phonebook = {
        "Alice": "555-1234",
        "Bob": "555-5678",
        "Carol": "555-8765"
    }

    while True:
        print_menu()
        choice = input("Choose an option (1-8): ")

        if choice == "1":
            print("\nCurrent dictionary:", phonebook)
        elif choice == "2":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Added/updated {name} -> {number}")
        elif choice == "3":
            name = input("Enter name to look up: ")
            value = phonebook.get(name)
            if value:
                print(f"{name}'s phone number is {value}")
            else:
                print(f"{name} not found in the dictionary.")
        elif choice == "4":
            name = input("Enter name to remove: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Removed {name} from the dictionary.")
            else:
                print(f"{name} not found in the dictionary.")
        elif choice == "5":
            print("Keys:", list(phonebook.keys()))
        elif choice == "6":
            print("Values:", list(phonebook.values()))
        elif choice == "7":
            print("Items:", list(phonebook.items()))
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 8.")


if __name__ == "__main__":
    main()
