def last_first_nocase(name):
	name=name.lower().split()
	return (name[1], name[0])


names = ["Mike Passel","alice Passel","danielle Clayton"]
new_names = sorted(names,key=last_first_nocase)
print new_names


# Github
# cd to documents
# git clone https://github.com/fexlneb/pythontraining.git