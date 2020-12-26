
def frequency(m,n):
    part = ((9.81 * m) / ((6.5) / (154/100)))**(1/2)
    freq = (n / (2* (84/100))) * part
    return freq

print(frequency(200,1))
print(frequency(200,2))
print(frequency(200,3))
print(frequency(200,4))