import os
import numpy as np

def remove(num_files):
    """Help remove:
    Removes random .tex files, except the mother file file1.tex. 
    Quantity specified by num_files"""
    
    for i in range(num_files):
        index = int(np.round(np.random.rand()*10))
        if index != 1:
            os.system("rm file%d.tex >/dev/null" % index)
            
    print(".tex files removed")