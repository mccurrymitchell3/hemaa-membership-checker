import requests

# This is where we will check membership status.

# Make API call to TidyHQ Contact Method.
parameters = {
    "access_token": "ea4ebfc417277907d48d16d361b15a184c1d88513d9d7f3b04475266458eeab7"
}
contacts = requests.get("https://api.tidyhq.com/v1/contacts", params=parameters)
for contact in contacts.json():
    email = contact['email_address']
    contactId = contact['id']
    print(email, contactId)
    print("NEXT: ")