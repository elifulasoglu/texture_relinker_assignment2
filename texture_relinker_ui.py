import maya.cmds as cmds
import os
import sys
import inspect

# Determine the directory containing this script
current_script_path = inspect.getfile(inspect.currentframe())
script_dir = os.path.dirname(os.path.abspath(current_script_path))

if script_dir not in sys.path:
    sys.path.append(script_dir)

import texture_relinker

def show_ui():
    if cmds.window("textureRelinkerWin", exists=True):
        cmds.deleteUI("textureRelinkerWin")

    window = cmds.window("textureRelinkerWin", title="Texture Relinker", widthHeight=(300, 100))
    cmds.columnLayout(adjustableColumn=True)

    cmds.button(label="Find and Relink Textures", command=find_and_relink_textures)

    cmds.showWindow(window)

def find_and_relink_textures(*args):
    # Debug output to ensure function is being called
    print("Find and Relink Textures button clicked")

    # Use fileDialog2 to select directories
    directories = cmds.fileDialog2(dialogStyle=2, fileMode=3, okCaption="Select Folder",
                                   caption="Select Correct Texture Folders", multipleSelection=True)

    # Debug output to see what directories were selected
    print(f"Directories selected: {directories}")

    if directories:
        texture_relinker.find_and_relink_textures(directories)
    else:
        cmds.warning("No directories selected.")

show_ui()

show_ui()
