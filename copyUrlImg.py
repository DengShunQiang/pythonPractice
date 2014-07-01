import urllib
class website():
    name=""
    imgHref=""
    def __init__(self,name,imgHref):
        self.imgHref=imgHref
        self.name=name
class webPicture():
    name=""
    src=""
    def __init__(self,name,src):
        self.name=name
        self.src=src
def copy_picture():
    p1=webPicture()
    p1.name="http://img.baidu.com/img/image/224-90.jpg"
    urllib.urlretrieve(p1.name,"E:\pythonFile\txtFiles\p1.jpg")