files handling*

fp=open("C:\\Users\\Chetan\\OneDrive\\Desktop\\files.txt")
#fp.write('hello')
print(fp.read())
print(fp.read(3))
print(fp.tell())
print(fp.seek(23))
print(fp.tell())
print(fp.read())
fp.close()

fp=open("C:\\Users\\Chetan\\OneDrive\\Desktop\\files.txt",'a+')
fp.write("\nmy first file\n")
fp.write("This file contains three lines")
print(fp.read())


