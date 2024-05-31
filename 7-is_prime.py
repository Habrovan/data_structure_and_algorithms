x=int(input("Enter a Number: "))
def is_prime(y):
    if x==2 or x==3 or x==5 or x==7 :
        return True
    elif x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
        return True
    else:
        return False

print(is_prime(x))