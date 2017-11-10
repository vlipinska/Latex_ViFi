import os, time
import compile_tex, generate_tex, remove_tex

path_to_watch = "."
before = dict ([(f, None) for f in os.listdir(path_to_watch)])

while True:
    time.sleep (3)
    
    generate_tex.generate(1)
    remove_tex.remove(1)
    
    after = dict ([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: print("Added: ", ", ".join (added))
    if removed: print("Removed: ", ", ".join (removed))
    before = after

    compile_tex.compile_and_remove()