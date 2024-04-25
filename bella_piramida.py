
def draw_piramida():
    h = 0
    while h < 1:
        try:
            h = int(input("Inserisci altezza di piramide: "))
        except:
            print("Inserisci solo numero ")


    s = input("inserisci simbol: ")
    l = len(s)
    for i in range(h):
        print(" "*(h-1-i)*l + (s + (" ")*l)*(1+i))
    
draw_piramida()