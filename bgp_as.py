asn = int(input("Ingrese el número de AS BGP: "))

if 64512 <= asn <= 65534:
    print(f"AS {asn}: Privado")

elif 4200000000 <= asn <= 4294967294:
    print(f"AS {asn}: Privado")

elif 1 <= asn <= 4294967294:
    print(f"AS {asn}: Público")

else:
    print("Número de AS inválido.")
