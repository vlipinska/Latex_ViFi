import os  

print("Compiling .tex files...")
os.system("pdflatex *.tex")
print("Done.")

print("Movind .pdf files...")
os.system("mv *.pdf ./pdfs")
print("Done.")

print("Removing auxiliary files...")
os.system("rm *.log *.aux")
print("Done.")