import os

def main():

    ip = input("Enter the IP to scan: ")


    print("\nChoose the scan type:")
    print("1. Intense Scan (nmap -T4 -A -v)")
    print("2. Intense Scan all TCP ports (nmap -p1-65535 -T4 -A -v)")
    print("3. Intense Scan plus UDP (nmap -sS -sU -T4 -A -v)")
    print("4. Intense Scan no Ping (nmap -T4 -A -v -Pn)")
    print("5. Quick Scan (nmap -T4 -F)")
    print("6. OS Detection (nmap -O -Pn)")
    print("7. Generic Scan (nmap)")


    choice = input("\nEnter the number of the scan you want to perform: ")


    if choice == "1":
        command = f"nmap -T4 -A -v {ip}"
    elif choice == "2":
        command = f"nmap -p1-65535 -T4 -A -v {ip}"
    elif choice == "3":
        command = f"nmap -sS -sU -T4 -A -v {ip}"
    elif choice == "4":
        command = f"nmap -T4 -A -v -Pn {ip}"
    elif choice == "5":
        command = f"nmap -T4 -F {ip}"
    elif choice == "6":
        command = f"nmap -O -Pn {ip}"
    elif choice == "7":
        command = f"nmap {ip}"
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"\nExecuting the scan: {command}")
    os.system(command)

if __name__ == "__main__":
    main()
