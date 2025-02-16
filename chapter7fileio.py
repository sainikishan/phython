# file I/o
# file input and output
# text file :txt,.docx,logetc.
# binaryfiles:mp4,mav,png,jprg etc
f=open(
    file="demo.txt",
    mode='r'
)
data=f.read()
print(data)
f.close()