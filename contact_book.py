contacts = {"Ana": ["06 11 22 33 44", "ana@mail.com"] }

name = input("name: ")
phone = input("phone: ")
email = input("email: ")
contacts[name] = [phone, email]

search = input("search: ")
if search in contacts:
  phone, email = contacts[search]
  print(f"{search}: {phone} / {email}")
else:
  print(f"{search} not found")

print(len(contacts), "contacts")