kiro = 0
kiro_yuzde = 0
clara = 0
clara_yuzde = 0
toplam = 0
sayac = 0
while True:
    x = float(input())
    toplam += 1
    if (x == 0):
        kiro += 1
    else:
        clara += 1

    kiro_yuzde = float(100 * kiro) / toplam
    clara_yuzde = float(100 * clara) / toplam

    print("kiro yuzde : ", kiro_yuzde,"\n")
    print("clara yuzde : ", clara_yuzde,"\n")
    sayac+=1
    print(sayac)
    