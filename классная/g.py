#Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определи,
# может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести YES,
# если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
x=int(input())
y=int(input())
x1=int(input())
y1=int(input())
if x+1==x1 and y+1==y1:
    print("yes")
elif x-1==x1 and y-1==y1:
    print("yes")
elif x==x1 and y+1==y1:
    print("yes")
elif x==x1 and y-1==y1:
    print("yes")
elif x+1==x1 and y==y1:
    print("yes")
elif x-1==x1 and y==y1:
    print("yes")
elif x+1==x1 and y-1==y1:
    print("yes")
elif x-1==x1 and y+1==y1:
    print ("yes")
 else: print("no")