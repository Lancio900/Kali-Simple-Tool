from ipwhois import IPWhois

def menu():
    
    ip = input("Enter the IP address: ")
    ipwhois = IPWhois(ip)
    result = ipwhois.lookup_rdap()

    print("\nIP Info:")
    print("----------------------------")
    
    
    print(f"ASN Information:")
    print(f"  ASN Registry: {result.get('asn_registry', 'N/A')}")
    print(f"  ASN: {result.get('asn', 'N/A')}")
    print(f"  ASN Description: {result.get('asn_description', 'N/A')}")
    print(f"  ASN Date: {result.get('asn_date', 'N/A')}")
    print()

    
    print(f"Network Information:")
    network_info = result.get('network', {})
    print(f"  Network Name: {network_info.get('name', 'N/A')}")
    print(f"  Start Address: {network_info.get('start_address', 'N/A')}")
    print(f"  End Address: {network_info.get('end_address', 'N/A')}")
    print(f"  CIDR: {network_info.get('cidr', 'N/A')}")
    print(f"  Network Type: {network_info.get('type', 'N/A')}")
    print()


    print(f"Additional Information:")
    print(f"  Query IP: {result.get('query', 'N/A')}")
    print(f"  IP Version: {network_info.get('ip_version', 'N/A')}")
    print()


    entities = result.get('entities', [])
    if entities:
        print(f"Entities Associated with IP:")
        for entity in entities:
            print(f"  Entity: {entity}")
    else:
        print("No entity information available.")
    print()

    print(f"More Info Links:")
    for link in result.get('links', []):
        print(f"  - {link}")

menu()
