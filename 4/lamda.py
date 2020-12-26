def calc(L, n):
    unconverted =(2*(L/100))/n
    return unconverted
waves=[]

def main():
    start = True
    while start:
        L = float(input("l"))
        n = float(input("n"))
        stop = input("stop")
        waves.append(calc(L,n))
        if stop == "y":
            break
    print(waves)
    print("avg:", (sum(waves)/len(waves)))

main()