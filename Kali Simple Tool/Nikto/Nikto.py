import os

def main():

    url = input("Enter the URL or IP to scan (e.g., http://192.168.1.1 or http://example.com): ")


    print("\nChoose the type of scan:")
    print("1. Basic scan (nikto -h <host>)")
    print("2. Full report scan (nikto -h <host> -o report.txt -Format htm)")
    print("3. SSL testing scan (nikto -h <host> -ssl)")
    print("4. Advanced vulnerability test scan (nikto -h <host> -Tuning 3)")
    print("5. Quiet mode scan (nikto -h <host> -quiet)")
    print("6. Specific vulnerability test scan (nikto -h <host> -Plugins <plugin>)")
    print("7. Basic scan without reporting")

    choice = input("\nEnter the number of the scan you want to perform: ")


    if choice == "1":
        command = f"nikto -h {url}"
    elif choice == "2":
        command = f"nikto -h {url} -o report.txt -Format htm"
    elif choice == "3":
        command = f"nikto -h {url} -ssl"
    elif choice == "4":
        command = f"nikto -h {url} -Tuning 3"
    elif choice == "5":
        command = f"nikto -h {url} -quiet"
    elif choice == "6":
        plugin = input("Enter the specific plugin for the scan (e.g., xss, sqlmap): ")
        command = f"nikto -h {url} -Plugins {plugin}"
    elif choice == "7":
        command = f"nikto -h {url} -no-report"
    else:
        print("Invalid choice. Exiting.")
        return


    print(f"\nExecuting the scan: {command}")
    os.system(command)

if __name__ == "__main__":
    main()
