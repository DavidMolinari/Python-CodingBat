def meh(message):
    a = ("abcdefghijklmnopqrstuvwxyz")
    p = ("?,. !:")
    nouveau = [0]*len(message)
    nouvmeh = 0
    for i in range(len(message)):
        for j in range (len(a)):
            if message[i] == a[j]:
                nouveau[i] = a[(j-3)%26]
            else:
                for k in range(len(p)):
                    if message[i] == p[k]:
                        nouveau[i] = p[k]
                    
        print (nouveau[i], end="")
        
        
meh("dx ...uhyrlu !")
