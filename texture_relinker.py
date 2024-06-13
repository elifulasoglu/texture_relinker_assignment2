import maya.cmds as cmds
import os


def find_and_relink_textures(directories):
    # Get all file nodes in the scene
    file_nodes = cmds.ls(type='file')

    # Dictionary to store old paths and new paths
    missing_files = {}

    # Check each file node
    for file_node in file_nodes:
        # Get the current file path
        file_path = cmds.getAttr(file_node + '.fileTextureName')

        # Check if the file exists
        if not os.path.isfile(file_path):
            print(f"Missing texture: {file_path}")
            # Store the missing file path
            missing_files[file_node] = file_path

    if not missing_files:
        print("No missing textures found.")
        return

    # Relink the missing textures
    for file_node, old_path in missing_files.items():
        # Extract the file name
        file_name = os.path.basename(old_path)
        found = False

        for directory in directories:
            # Create a new path with the correct directory
            new_path = os.path.join(directory, file_name)

            # Check if the new path exists
            if os.path.isfile(new_path):
                # Update the file node with the new path
                cmds.setAttr(file_node + '.fileTextureName', new_path, type='string')
                print(f"Updated {file_node} to {new_path}")
                found = True
                break

        if not found:
            print(f"File {file_name} not found in the selected directories.")

    print("Texture relinking complete.")
