# file I/o
# file input and output
# text file :txt,.docx,logetc.
# binaryfiles:mp4,mav,png,jprg etc
f=open(
    file="demo.txt",
    mode='r'
)
line1=f.readline(3)
print(line1)
f.close()
# write  a file
f=open(
    file="demo.txt",
    mode='a'
)
f.write(" i am deceoperl")
f.close()