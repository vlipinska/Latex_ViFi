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
