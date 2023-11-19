data=input()
while data!="":
    if len(data)!=8:
        print("Error: Enter 8 bits")
    else:
        parity=0
        for bit in data:
            parity^=int(bit)
        if parity==0:
            print("The parity bit should be 0")
        else:
            print("The parity bit should be 1")
    data=input()