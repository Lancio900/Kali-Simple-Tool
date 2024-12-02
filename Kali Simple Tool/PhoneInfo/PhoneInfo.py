import phonenumbers
from phonenumbers import geocoder, carrier

def localize_phone_number(phone_number):
    try:

        parsed_number = phonenumbers.parse(phone_number)
        

        country = geocoder.region_code_for_number(parsed_number)
        print(f"Country: {country}")


        phone_carrier = carrier.name_for_number(parsed_number, "en")
        print(f"Carrier: {phone_carrier}")


        international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print(f"International Format: {international_format}")


        region = geocoder.description_for_number(parsed_number, "en")
        print(f"Region: {region}")


        if phonenumbers.is_valid_number(parsed_number):
            print(f"Is this a valid number? Yes")
        else:
            print(f"Is this a valid number? No")

        if phonenumbers.is_possible_number(parsed_number):
            print(f"Is this a possible number? Yes")
        else:
            print(f"Is this a possible number? No")


        number_type = phonenumbers.number_type(parsed_number)
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f"Is this a mobile number? Yes")
        else:
            print(f"Is this a mobile number? No")

    except phonenumbers.phonenumberutil.NumberParseException:
        print("Error: Invalid phone number format")


phone_number = input("Enter a phone number (with country code, e.g., +1 202-555-0186): ")
localize_phone_number(phone_number)
