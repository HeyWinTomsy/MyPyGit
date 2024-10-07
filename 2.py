N=input("Введіть кількість рядків: ")
tr1=0
while tr1==0:
    try:
        if int(N)<0:
            N=int(N)*(-1)
            print(N)
            tr1=1
        else:
            tr1=1
    except ValueError:
        tr=0
        while tr<1:
            if N.isalpha():
                print("Введіть число, ви ввели:",N,"Це  не число")
                N = input("Введіть кількість рядків: ")
                tr=0
            else:
                tr=1
list1=[]
list2=[]
while int(N)>0:
    N2 = str(input("Введіть рядок: "))
    list1.append(N2)
    N=int(N)-1
    C=(N2.count(max(N2)))
    list2.append(C)
P=(list2.index(max(list2)))+1
print("Найбільше повторів у ",P,"му рядку")