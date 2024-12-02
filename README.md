# Kali Simple Tool

## Description

Kali Simple Tool is a command-line-based security tool suite that allows users to run multiple security tools on their target IP addresses or URLs. It provides a menu-based interface to run the following tools:

- **Nmap**: A network scanner for discovering devices and services on a network, used for vulnerability assessment.
- **IpGeolocation**: Retrieve geographical information about an IP address.
- **Nikto**: A web scanner that detects security issues in web servers.
- **IpInfo**: Provides detailed information about a given IP address.
- **PhoneInfo**: Gathers details about phone numbers including their carrier and location.

The tool is designed to be simple to use, with clear prompts for the user and the ability to run different types of scans or gather information from multiple sources.

## Requirements

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Required Modules**: The following Python modules are required to run the scripts:
  - `os` (Standard library, no installation needed)
  
Ensure that each Python script (e.g., `nmap.py`, `IpGeocalitation.py`, etc.) is placed in the appropriate directories as described in the code.

## Installation

To install and use the Kali Simple Tool:

1. Clone the repository or download the files to your local machine:
    ```bash
    git clone https://github.com/Lancio900/Kali-Simple-Tool.git
    ```

2. Navigate to the folder containing the script:
    ```bash
    cd Kali-Simple-Tool
    ```

3. Make sure you have Python 3 installed. If not, install it via the official Python website or package manager.

4. The tool works directly from the command line. Run the script:
    ```bash
    python3 Kali\ Simple\ Tool.py
    ```

## Usage

1. Once the program starts, you will be presented with a menu displaying the available tools.
2. Choose a tool by entering the corresponding number (e.g., `1` for Nmap, `2` for IpGeolocation).
3. Follow the on-screen prompts to input the necessary information (IP address, scan type, etc.).
4. After the tool runs, you can either continue running other tools or exit the program.

## Tools Available

- **Nmap**: Perform various types of network scans including:
  - Intense Scan
  - Intense Scan for all TCP ports
  - Intense Scan with UDP
  - OS Detection
  - Quick Scan
  
- **IpGeolocation**: Get the geolocation information of an IP address.

- **Nikto**: Perform a comprehensive web server security scan.

- **IpInfo**: Get detailed information about an IP address such as its geographical location, organization, and more.

- **PhoneInfo**: Gather information about phone numbers.

## Example Usage

```bash
$ python3 Kali\ Simple\ Tool.py

Welcome to the Security Tool Suite!
Choose a tool to use:
1. Nmap
2. IpGeolocation
3. Nikto
4. IpInfo
5. PhoneInfo
6. Exit

Enter the number of the tool you want to run: 1

Running Nmap...
Enter the IP to scan: 8.8.8.8

Choose the scan type:
1. Intense Scan (nmap -T4 -A -v)
2. Intense Scan all TCP ports (nmap -p1-65535 -T4 -A -v)
3. Intense Scan plus UDP (nmap -sS -sU -T4 -A -v)
4. Intense Scan no Ping (nmap -T4 -A -v -Pn)
5. Quick Scan (nmap -T4 -F)
6. OS Detection (nmap -O -Pn)
7. Generic Scan (nmap)

Enter the number of the scan you want to perform: 5
