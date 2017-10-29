import xlrd
from numpy import *

def condidate(m,A):
    j=m
    c=A[m]
    count=1
    while j<len(A)-1 and count>0:
        j=j+1
        if A[j]==c:
            count=count+1
        else:
            count=count-1
    if j==len(A)-1:
        return c
    else:
        return condidate(j+1,A)

def majority(A):


    c=condidate(0,A)
    count=0
    for i in range(0,len(A)-1):
        if A[i]==c:
            count=count+1
    if count>len(A)/2:
        return c
    else:
        return None

def dataget(exlname,sheetname):
    ori = xlrd.open_workbook(exlname)
    table = ori.sheet_by_name(sheetname)
    data=[]
    for i in range(0, table.nrows):
        data.append(table.row_values(i))
    return data

if __name__ == '__main__':
    data=dataget('majority data.xlsx','Sheet1')
    result=majority(data)
    print(result)
