#!/usr/bin/python3
import subprocess
import sys

name=str()
if len(sys.argv)<=1:
    name=input("type in the name of your file:")
else:
    name=sys.argv[1]
if name.endswith('.pdf_t'):
   print("no  suffix please!")
   quit()
subprocess.call(["mkdir",'-p','tmp'])
subprocess.call(['cp',name+'.pdf','tmp/'])
subprocess.call(['cp',name+'.pdf_t','tmp/'])

commands="s!asdf!"+name+"!"
f=open('tmp/gen'+name+'.tex','w')
subprocess.call(['sed',commands,'template.tex'],stdout=f)
f.close()
subprocess.call(['pdflatex','-output-directory','tmp','tmp/gen'+name+'.tex'])
subprocess.call(['mv','tmp/gen'+name+'.pdf',name+'fig.pdf'])
subprocess.call(['rm','-r','tmp'])
subprocess.call(['pdfcrop',name+'fig.pdf',name+'crop.pdf'])
