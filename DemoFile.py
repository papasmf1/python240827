# DemoFile.py 

#쓰기 
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close()

#읽기(raw string notation)
f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
result = f.read() 
print(result)
f.close() 


