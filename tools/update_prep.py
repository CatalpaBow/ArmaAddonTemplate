import os

def prep_update(addon_folder_path):
    fnc_fldr = os.path.join(addon_folder_path,"functions")
    XEH_PREP_hpp_file = os.path.join(addon_folder_path,"XEH_PREP.hpp")
    prep_text_lines = [
        "PREP({});\n".format(os.path.splitext(f)[0].replace("fnc_", ""))
        for f in os.listdir(fnc_fldr)
        if os.path.isfile(os.path.join(fnc_fldr, f)) and os.path.splitext(f)[1] == ".sqf"
    ]
    with open(XEH_PREP_hpp_file,"w") as f:
        f.writelines(prep_text_lines)

# Allow running from root directory and tools directory
root_dir = ".."
if os.path.exists("addons"):
    root_dir = "."
addon_folder_path = os.path.join(os.path.abspath(root_dir),"addons","sandBox")
prep_update(addon_folder_path)