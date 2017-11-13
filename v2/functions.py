import os
import numpy as np

def generate(num_files):
    """Help for generate:
    Creates new .tex files by copying a 'mother file' file1.tex. 
    Quantity specified by num_files.
    """
    
    for i in range(num_files):
        if i != 1:
            index = int(np.round(np.random.rand()*10))
            os.system("cp file1.tex file%d.tex" % index)
            
    print(".tex files generated")


def remove(num_files):
    """Help remove:
    Removes random .tex files, except the mother file file1.tex. 
    Quantity specified by num_files"""
    
    for i in range(num_files):
        index = int(np.round(np.random.rand()*10))
        if index != 1:
            os.system("rm file%d.tex >/dev/null" % index)
            
    print(".tex files removed")    


def compile_and_move(data):
    """Help for compile_and_remove
    
    Compiles all the .tex files in the current folder.
    Puts the output .pdf files in a ./pdfs folder/
    Removes all the .aux and .log files
    
    Inputs: none
    
    Outputs: compiled pdf files"""
    
    created_files = data["created"]
    
    print("Compiling .tex files...")
    for name in created_files:
        os.system("pdflatex %s > /dev/null" %name)
    #os.system("echo *.tex|xargs -n1 pdflatex >/dev/null")
    print("Done.")

    print("Moving .pdf files...")
    os.system("rm ./pdfs/*.pdf ")
    print(".pdf's removed")
    os.system("mv *.pdf ./pdfs")
    print("Done.")

    print("Removing auxiliary files...")
    os.system("rm *.log *.aux")
    print("Done.")