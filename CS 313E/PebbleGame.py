def playAlice(n):
    if n == 0:
        print("Alice wins!")
    else:
        playBob(n-1)

def playBob(n):
    if n == 0:
        print("Bob wins!")
    elif (n % 2 == 1):
        playAlice(n-1)
    else:
        playAlice(n-2)

def main():

    for i in range(20):
        print ("If i is", i+1)
        playAlice(i+1)

main()

#mutual recursion
