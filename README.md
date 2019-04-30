# Purpose

A python script to automatically transform 'pdf+pdf_t' files exported from Xfig to a single well-cropped pdf file

# Usage

Make sure the `pdflatex` and `pdfcrop` commands can be excuted. If not, install them.

Suppose the exported files from Xfig are frame.pdf and frame.pdf_t  

Move them to the same folder as templatex.tex and gen.py

Excute
```
./gen.py frame
```
You will see a file named `genframe.pdf`(not cropped) and a file named `framecrop.pdf`

Feel free to change the file names in the python script. 
