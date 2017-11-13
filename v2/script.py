import change_in_dirs
import functions

a = change_in_dirs.compute_dir_index()

functions.generate(2)
functions.remove(2)

b = change_in_dirs.compute_dir_index()

data = change_in_dirs.compute_diff(b,a)
print(data)
created_files = data["created"]
print(created_files)

functions.compile_and_move(data)
