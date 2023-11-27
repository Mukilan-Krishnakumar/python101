# Membership Operations - in, not in
sandy_dir = ["GVM", "Martin", "Ram", "Atlee", "Vetrimaran", "Mani Ratnam"]
if "Atlee" in sandy_dir:
    print("Atlee is awesome")
else:
    print("Atlee sucks")

if "Chris" not in sandy_dir:
    print("Worst Taste")
else:
    print("Best taste")

# Identity Operations - is, is not
copy_dir = sandy_dir

print(copy_dir is not sandy_dir)
