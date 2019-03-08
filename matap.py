import PyPDF2 as pyp
import urllib.request as req
from os import listdir
from os import system

if __name__ == "__main__":


    courses = [ "67504" ,  "67521", "67596", "80177" ]

    for course in courses :
        url = "http://sites.huji.ac.il/exams/" + course + "_{0}_{1}_{2}_1.pdf"
        system("mkdir {0}".format(course))
        for i in range(2000 , 2019):
            for k in range(1, 3):
                for j in range(1 , 3):
                    try :
                        req.urlretrieve(url.format(i , k , j) , "./" + course + "/{0}-{1}-{2}.pdf".format(i, k , j))
                        print("Downlond : ~ {0}-{1}-{2}-{3} ~".format(course, i, k , j))
                    except :
                        pass

    for hist in courses:
        out = "./{0}/tests-{0}.pdf".format(hist)
        filewriter =  pyp.PdfFileWriter( )
        for _path in listdir(hist):
            if ".py" not in _path:
                with open("./"+ hist + "/" +_path , "rb") as _file:
                    filereader =  pyp.PdfFileReader( _file )
                    try :
                        filewriter.appendPagesFromReader(filereader)
                        with open(out , "wb+" ) as _out:
                            filewriter.write(_out)
                        print("Merge : " + str(_path))
                    except :
                        pass
