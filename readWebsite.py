import io
import urllib
ecnu = urllib.urlopen("http://www.ecnu.edu.cn")
s= ecnu.read()
print s
output= open(r"E:\pythonFile\txtFiles\ecnu.txt","w")
output.write(s)
output.close()
