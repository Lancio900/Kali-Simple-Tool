import requests

def menu():

    Ip_Victim = input("Enter IP Address: ")

    get_ip_location(Ip_Victim)  

def get_ip_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'fail':
        print(f"Error: Unable to retrieve data for IP {ip_address}.")
    else:
        print("\nIP Geolocation Information:")
        print("----------------------------")
        print(f"IP Address: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Country Code: {data['countryCode']}")
        print(f"Region: {data['region']} ({data['regionName']})")
        print(f"City: {data['city']}")
        print(f"ZIP Code: {data['zip']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ISP: {data['isp']}")
        print(f"Organization: {data['org']}")
        print(f"ASN: {data['as']}")
        print("----------------------------")

menu()
