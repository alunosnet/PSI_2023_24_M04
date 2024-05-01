email=input("Email:")
password=input("Password:")

temNumeros=False
temMinuscula=False
temMaiusculas=False

for c in password:
    if c>="0" and c<="9":
        temNumeros=True
    if c>="a" and c<="z":
        temMinuscula=True
    if c>="A" and c<="Z":
        temMaiusculas=True

if temNumeros==False or temMinuscula==False or temMaiusculas==False:
    print("Password não é segura porque deve ter letras minusculas, maiuscula e números")

if len(password)<8:
    print("Password não é segura porque não tem 8 letras")

if password in email:
    print("Password não é segura porque faz parte do email")