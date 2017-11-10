import os

def compile_and_remove():
    
    print("Compiling .tex files...")
    os.system("echo *.tex|xargs -n1 pdflatex >/dev/null")
    print("Done.")

    print("Moving .pdf files...")
    os.system("rm ./pdfs/*.pdf ")
    print(".pdf's removed")
    os.system("mv *.pdf ./pdfs")
    print("Done.")

    print("Removing auxiliary files...")
    os.system("rm *.log *.aux")
    print("Done.")
