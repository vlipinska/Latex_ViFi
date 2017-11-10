import os, time

path_to_watch = "."
before = dict ([(f, None) for f in os.listdir(path_to_watch)])

while 1:
    time.sleep (10)
    after = dict ([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: print("Added: ", ", ".join (added))
    if removed: print("Removed: ", ", ".join (removed))
    before = after

    print("Compiling .tex files...")
    os.system("pdflatex *.tex")
    print("Done.")

    print("Movind .pdf files...")
    os.system("mv *.pdf ./pdfs")
    print("Done.")

    print("Removing auxiliary files...")
    os.system("rm *.log *.aux")
    print("Done.")

