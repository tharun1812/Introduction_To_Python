contacts = {}

while True:
  choice = input("1 add, 2 search, 3 list:")
  if choice == "1":
    name = input("name: ")
    phone = input("phone: ")
    if name not in contacts:
      contacts[name] = []
    contacts[name].append(phone)
  elif choice == "2":
    name = input("Name:")
    print(contacts.get(name, "Not found"))  
  elif choice == "3":
    for name in sorted(contacts):
      print(f"{name:<5}", ", ".join(contacts[name]))
  else:
    break