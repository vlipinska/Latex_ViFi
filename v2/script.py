import dir_change
import generate_tex, remove_tex, compile_chosen

a = dir_change.compute_dir_index()

generate_tex.generate(2)
remove_tex.remove(2)

b = dir_change.compute_dir_index()

data = dir_change.compute_diff(b,a)
print(data)
created_files = data["created"]
print(created_files)

compile_chosen.compile_and_remove(data)
