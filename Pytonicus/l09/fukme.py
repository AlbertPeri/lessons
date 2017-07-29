import os
for file in os.listdir(path="."):
	print(file)
	new_file = file[:file.rfind(".")] + ".loh"
	if file != os.path.basename(__file__):
		os.rename(file, new_file)