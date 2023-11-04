eps = 1.0
i=0
while (1.0 + eps) != 1.0:
    eps /= 2.0
    print(eps)
    i+=1
    print(i)

print(eps)

print(1.0+1*(10**(-16)))