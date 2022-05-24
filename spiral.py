def printM(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print('%7d' % a[i][j], end = '')
        print()

def Matr(n,m):
    a = [0] * n
    for i in range(n):
        a[i] = [0]* m
    return a

def Menu(n,m):
    try:
        n = int(n)
        m = int(m)
        if n > 0 and m > 0:
            a =  Matr(n,m)
            return Spiral(a,n,m)
        else:
            print('Вводимые значения должны быть целыми числами строго больше нуля')
            n = int(input('Введите кол-во строк(n):'))
            m = int(input('Введите кол-во столбцов (m):'))
            return Menu(n,m)
    except (TypeError,ValueError):
        print('Вводимые значения должны быть целыми числами строго больше нуля')
        n = input('Введите кол-во строк(n):')
        m = input('Введите кол-во столбцов (m):')
        return Menu(n,m)
        
def Spiral(a,n1,m1,lv = 1,fInd = 0):
    flag = False
    if m1 < 1 or n1 < 1:
        return a
    else:
        j1 = 0
        for j in range(fInd ,m1 + fInd):
            a[fInd][j] = j1 + lv
            j1+=1
            
        for g in range(fInd + 1,n1 + fInd):
            a[g][m1 - 1 +fInd] = g + a[fInd][j] - fInd

        if n1 != 1:
            for v in range((m1) - 2 + fInd ,-1 + fInd, -1):
                a[n1 - 1 + fInd][v] =  (m1) - (v + 1 - fInd) + a[g][m1 - 1 + fInd]
        else:
            return a
        
        if m1 != 1: 
            for q in range(n1 - 2 + fInd,0 + fInd, -1):
                a[q][fInd] =(n1) - (q + 1) + a[n1 - 1 + fInd][v] + fInd
                flag = True
            if flag:
                lvv = a[q][fInd]
            else:
                return a
            
        else:
            return a
        m1 -= 2
        n1 -= 2
        fInd += 1
        return Spiral(a,n1,m1,lvv + 1,fInd)
            
n = input('Введите кол-во строк(n):')
m = input('Введите кол-во столбцов (m):')
printM(Menu(n,m))
   
    
