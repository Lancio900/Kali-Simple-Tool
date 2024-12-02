import os
import sys

def clear_screen():
    os.system('clear')

def menu():
    while True:
        clear_screen()
        
        # Print header with ASCII Art
        print(""" 
        ██╗  ██╗   ███████╗ ████████╗
        ██║ ██╔╝   ██╔════╝ ╚══██╔══╝
        █████╔╝    ███████╗    ██║   
        ██╔═██╗    ╚════██║    ██║   
        ██║  ██╗██╗███████║██╗ ██║██╗
        ╚═╝  ╚═╝╚═╝╚══════╝╚═╝ ╚═╝╚═╝
              Kali Simple Tool
        """)

        print("Welcome to the Security Tool Suite!")
        print("Choose a tool to use:")
        print("1. Nmap")
        print("2. IpGeolocation")
        print("3. Nikto")
        print("4. IpInfo")
        print("5. PhoneInfo")
        print("6. Exit")  # Option to exit the program

        choice = input("\nEnter the number of the tool you want to run: ")

        if choice == "1":
            print("\nRunning Nmap...")
            try:
                os.system(r"python ~/Desktop/Malware/Kali\ Simple\ Tool/Nmap/nmap.py")
            except Exception as e:
                print(f"Error running Nmap: {e}")
            input("Press Enter to continue: ")
        
        elif choice == "2":
            print("\nRunning IpGeolocation...")
            try:
                os.system(r"python ~/Desktop/Malware/Kali\ Simple\ Tool/IpGeo/IpGeocalitation.py")
            except Exception as e:
                print(f"Error running IpGeolocation: {e}")
            input("Press Enter to continue: ")

        elif choice == "3":
            print("\nRunning Nikto...")
            try:
                os.system(r"python ~/Desktop/Malware/Kali\ Simple\ Tool/Nikto/Nikto.py")
            except Exception as e:
                print(f"Error running Nikto: {e}")
            input("Press Enter to continue: ")

        elif choice == "4":
            print("\nRunning IpInfo...")
            try:
                os.system(r"python ~/Desktop/Malware/Kali\ Simple\ Tool/IpInfo/IPInfo.py")
            except Exception as e:
                print(f"Error running IpInfo: {e}")
            input("Press Enter to continue: ")

        elif choice == "5":
            print("\nRunning PhoneInfo...")
            try:
                os.system(r"python ~/Desktop/Malware/Kali\ Simple\ Tool/PhoneInfo/PhoneInfo.py")
            except Exception as e:
                print(f"Error running PhoneInfo: {e}")
            input("Press Enter to continue: ")

        elif choice == "6":
            print("\nExiting the program. Goodbye!")
            sys.exit(0)  # Exit the program

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue: ")

if __name__ == "__main__":
    menu()
