def einstein_mass (m) :
    c = 300000000
    E = int(m)*int(c**2)
    return E

def main ():
    user_input = input ("m: ")
    mass = einstein_mass(user_input)
    print ("E:",mass)

main()
