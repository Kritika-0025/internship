
import random
import string

def genpas(l):
    alp = string.digits + string.punctuation + string.ascii_letters  
    pas = ''.join(random.choice(alp) for i in range(l))
    return pas

def main():
    try:
        l = int(input("Enter the length of the password: "))
        if l <= 0:
            print("Length must be a positive number.")
            return
        pas = genpas(l)
        print("Required Password:", pas)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()