import os

def compile_and_remove(data):
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
