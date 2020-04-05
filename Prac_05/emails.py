def main():
    converting_email_to_name= {}
    email= input("Email:")
    while email != "":
        name = get_name(email)
        confirm = input("Is your name {}? (Y/n)". format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name:")
        converting_email_to_name[email] = name
        email = input("Email:")
    for email, name in converting_email_to_name.items():
        print("{} ({})".format(name,email))

def get_name(email):

      prefix = email.split('@')[0]
      parts = prefix.split('.')
      name = " ".join(parts).title()
      return name

main()
