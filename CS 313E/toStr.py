def toStr(n, base):

    convString = "0123456789ABCDEF"

    if n < base:
        return (convString[n])
    else:
        return (toStr(n//base,base) + convString[n%base])

def main():

    print(toStr(1011,2))

main()
