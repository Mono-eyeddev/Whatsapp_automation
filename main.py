#CLI gui for end-user 
from instant import send_instant
from spam import spam_mode
from schedule_send import schedule_message
from bulk_send import send_bulk

def main():
    while True:
        print("\n==========================")
        print("WhatsApp Auto Suite")
        print("==========================")
        print("1. Send instant message")
        print("2. Send unlimited messages")
        print("3. Schedule a message")
        print("4. Send to multiple contacts")
        print("5. Exit")
        choice = input("Select option: ")
#The other functions are declared in their seperate file 
        if choice == "1":
            send_instant()
        elif choice == "2":
            spam_mode()
        elif choice == "3":
            schedule_message()
        elif choice == "4":
            send_bulk()
        elif choice == "5":
            print("Amigo out! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
