def calculate_lamb(x, m, a):
    denominator = m * (x**2 + 184**2)**(1/2)
    num = x * (a/10)
    return (num/denominator) * (10 **7)

def main():
    y = ""
    tot = []
    while y != "y":
        x = float(input("dist?"))
        m = float(input("mode?"))
        a = float(input("sep?"))
        tot.append(calculate_lamb(x,m,a))
        y = input("end?")

    print("average lamda is", sum(tot)/len(tot))

main()
