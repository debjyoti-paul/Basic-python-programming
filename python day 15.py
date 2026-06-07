import os
def list_files_recusive(path):
    for item in os.listdir(path):
        print(item)  #print the name of the file , folders , etc.
        full_path=os.path.join(path, item)
        print(full_path)#print the path(location)
        if os.path.isfile(full_path):
            print("file:" , full_path)
        if os.path.isdir(full_path):
            print("directory:" , full_path)    
            list_files_recusive(full_path)
    print(os.listdir(path))  #print the valus or names of the file and folders in list
#list_files_recusive("C:/Users/MSCLAB-142/Downloads/deb")    #wriiten the path in the bracket

list_files_recusive("C:/Users/SHRIBASH PAUL/Downloads/college/documents")

#output
#PS C:\Users\MSCLAB-142> & C:/Users/MSCLAB-142/anaconda3/python.exe "c:/Users/MSCLAB-142/python day 15.py"
#New folder
#C:/Users/MSCLAB-142/Downloads/deb\New folder
#directory: C:/Users/MSCLAB-142/Downloads/deb\New folder
#insssss.xlsx
#C:/Users/MSCLAB-142/Downloads/deb\New folder\insssss.xlsx
#file: C:/Users/MSCLAB-142/Downloads/deb\New folder\insssss.xlsx
#New Microsoft Access Database ins.accdb
#C:/Users/MSCLAB-142/Downloads/deb\New folder\New Microsoft Access Database ins.accdb
#file: C:/Users/MSCLAB-142/Downloads/deb\New folder\New Microsoft Access Database ins.accdb
#New Microsoft Publisher Document ins.pub
#C:/Users/MSCLAB-142/Downloads/deb\New folder\New Microsoft Publisher Document ins.pub
#file: C:/Users/MSCLAB-142/Downloads/deb\New folder\New Microsoft Publisher Document ins.pub
#['insssss.xlsx', 'New Microsoft Access Database ins.accdb', 'New Microsoft Publisher Document ins.pub']
#New Microsoft Access Database.accdb
#C:/Users/MSCLAB-142/Downloads/deb\New Microsoft Access Database.accdb
#file: C:/Users/MSCLAB-142/Downloads/deb\New Microsoft Access Database.accdb
#New Microsoft Excel Worksheet.xlsx
#C:/Users/MSCLAB-142/Downloads/deb\New Microsoft Excel Worksheet.xlsx
#file: C:/Users/MSCLAB-142/Downloads/deb\New Microsoft Excel Worksheet.xlsx
#New Microsoft Word Document.docx
#C:/Users/MSCLAB-142/Downloads/deb\New Microsoft Word Document.docx
#file: C:/Users/MSCLAB-142/Downloads/deb\New Microsoft Word Document.docx
#New Text Document.txt
#C:/Users/MSCLAB-142/Downloads/deb\New Text Document.txt
#file: C:/Users/MSCLAB-142/Downloads/deb\New Text Document.txt
#['New folder', 'New Microsoft Access Database.accdb', 'New Microsoft Excel Worksheet.xlsx',
# 'New Microsoft Word Document.docx', 'New Text Document.txt']  



#head recursion
def head(n):
    if n==0:
        return
    head(n-1)
    print(n)

head(10)#o/p: 1 2 3 4 5 6 7 8 9 10 in new lines


def tail(n):
    if n==0:
        return
    print(n)
    tail(n-1)
    
tail(10)#o/p: 10 9 8 7 6 5 4 3 2 1 in new lines

#python donot have tail call optimisation

def fac_head(n):
    if n==0:
        return 0
    else:
        prod=fac_head(n-1)
        return n* prod
print(fac_head(5))


def fac_tail(n , acc=1):
    if n == 0 or n == 1:
        return acc
    return fac_tail(n - 1, acc * n)
print(fac_tail(6))#check this program

def sum(n):
    if n==0:
        return 0
    else:
        fn1=sum(n-1)
        return n+fn1
print(sum(6))
    
#do head and tail rec of sum , fibo ,fact etc

