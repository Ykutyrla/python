#Фирма ежегодно на протяжении n лет закупала оборудование стоимостью соответственно s1, s2, ..., sn pублей в год
#(эти числа вводятся и обрабатываются последовательно).
#Ежегодно в результате износа и морального старения (амортизации) все имеющееся оборудование уценивается на р%.
#Какова общая стоимость накопленного оборудования за n лет?

a = float(input("Стоимость закупки в первый год\n"))
b = float(input("Стоимость закупки во второй год\n"))
c = float(input("Стоимость закупки в третий год\n"))

p = int(input("Ежегодный процент износа\n"))
A = a*(1-(p/100))
print ("Стоимость накопленного оборудования в первый год "+ str (A)+" рублей")
B = ((A+b)*(1-(p/100)))
print ("Стоимость накопленного оборудования во второй год "+ str (B)+" рублей")
C = ((A+B+c)*(1-(p/100)))
print ("Стоимость накопленного оборудования в третий год "+ str (C)+" рублей")
