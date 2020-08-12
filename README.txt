Welcome to the NCR bulk site hour upload program!

See the Jupyter Notebook for full documentation and step-by-step instructions.
1. Open Command Prompt / Terminal as an Administrator, use the change directory command
    ("cd [filepath]") to navigate to the folder with the upload template and program
2. Type "pip install notebook", then press Enter to allow that library to install
2. Type "jupyter notebook" in the Command Prompt or Terminal, it may take a moment
    to create the connection
3. Open "AO Store Hours Bulk Upload.ipynb" - you can run the program in the window
    by going to Cell > Run All or Run Below (from the "Import libraries" step)
4. Close the Jupyter Notebook from the web browser, File > Close and Halt

To run the program:
1. Open the Command Prompt or Terminal
2. Use the change directory command ("cd [filepath]") to navigate to the folder
    with the upload template and program
3. Type "py site-hours-bulk-import.py"
4. Collect the outputted text file in the directory of the program named "JSON-call"

Tips:
*The filepath of a folder can be "copied as text" on Windows by right-clicking
    on the Folder navigation bar an selecting that option
*The filepath of a file can be "copied as path" on Windows by shift-clicking 
    the file and selecting that option
*Trouble shooting and debugging code is included in the program, but needs to be
    un-commented in the source code; comments are also included in the source code
*To go back to the parent directory, type "cd .."
*from the command line or terminal, navigate to the desired folder location using
    "cd file\path\to\your\folder" (reverse slashes if using terminal) and then typing
    "jupyter notebook" to create a new notebook