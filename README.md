# texture_relinker_assignment2
Assignment 2 - Find missing textures 

 

In the attachment you will find a Maya scene and textures. The scene contains a shader with some textures assigned. However, the textures paths in the file nodes point at the wrong location on disk. 

 

Write a tool to find and re-link all the missing textures in the scene. 

## Overview

The Texture Relinker Tool is designed to find and re-link missing textures in a Maya scene. It identifies file nodes with missing textures, prompts the user to select directories containing the correct textures, and updates the file paths accordingly.

## Features

- Identifies missing textures in the scene.
- Prompts the user to select directories containing the correct textures.
- Updates the file nodes with the correct paths if the textures are found.
- Provides a simple and user-friendly UI to facilitate the relinking process.

## Installation

1. **Download the Scripts:**
   - `texture_relinker.py`
   - `texture_relinker_ui.py`

2. **Place the Scripts:**
   - Save both scripts in the same directory. Preferably, place them in your Maya scripts directory:
     - **Windows:** `C:\Users\<YourUsername>\Documents\maya\scripts`
     - **macOS:** `/Users/<YourUsername>/Library/Preferences/Autodesk/maya/scripts`
     - **Linux:** `/home/<YourUsername>/maya/scripts`

## Usage

1. **Open Maya:**
   - Launch Autodesk Maya.

2. **Load the UI Script:**
   - Open the Script Editor in Maya: `Windows > General Editors > Script Editor`.
   - Load the UI script by selecting `File > Load Script...` and choosing `texture_relinker_ui.py`.

3. **Run the UI Script:**
   - In the Script Editor, select all the code in `texture_relinker_ui.py` and press the `Execute` button (or press `Ctrl+Enter`). This will open the Texture Relinker UI.

4. **Use the Tool:**
   - Click the "Find and Relink Textures" button to open a dialog to select multiple directories containing your missing textures.
   - The script will then find and re-link the textures, updating the paths in the Maya scene.

## Example Workflow

1. Open your Maya scene with missing textures.
2. Load and run the `texture_relinker_ui.py` script to open the Texture Relinker UI.
3. Click the "Find and Relink Textures" button.
4. Select the directories where your textures are located.
5. The tool will automatically find and re-link the missing textures.
