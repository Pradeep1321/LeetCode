def defangIPaddr(address):
    return address.replace('.','[.]')

address1 = "1.1.1.1"
print(defangIPaddr(address1))

