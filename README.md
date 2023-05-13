# cbseResults2023
 This is a selenium based Python Script to get Score Cards of your Entire School(ofc 12th students)
# Step-by-Step Guide: Setting up and Running this Python Script on Windows
- Install Python:
    Visit the official Python website at https://www.python.org/.
    Click on the "Downloads" tab.
    Choose the latest stable version of Python for Windows.
    Download the installer that corresponds to your system architecture (32-bit or 64-bit).
    Run the installer and follow the on-screen instructions.
    During the installation process, make sure to select the option to add Python to your system's PATH.

- Verify Python Installation:
    Open the Command Prompt by pressing Win + R and typing cmd, then hit Enter.
    Type python --version and press Enter.
    The installed Python version should be displayed in the Command Prompt window, indicating a successful installation.

- Install Required Dependencies:
    Navigate to the directory where you have stored your Python script using the cd command in Command Prompt.
    If your script relies on any external libraries or modules, you may need to install them using pip, the Python package installer.
    To install a package, use the command pip install selenium in the Command Prompt.

- Configure the Script:

    Open the Python script using a text editor of your choice.(Use VSCode if you are beginner)
    Look for any configurable variables or settings within the script that I have commented.(Like Roll Numbers and School Numbers)
    Adjust those variables according to your requirements. For example, you may need to specify the file path to driver,etc
- Step-by-Step Guide: Installing Visual Studio Code (VSCode) and Setting it up for Python Development

    Download Visual Studio Code:
        Visit the official Visual Studio Code website at https://code.visualstudio.com/.
        Click on the "Download" button to download the installer for Windows.
        Run the installer and follow the on-screen instructions.
        Choose the desired installation options and complete the installation process.

    Install Python Extension in VSCode:
        Open Visual Studio Code after installation.
        Click on the Extensions icon on the left sidebar or press Ctrl + Shift + X.
        In the Extensions view, search for "Python" in the search bar.
        Click on the "Python" extension offered by Microsoft and click on the "Install" button.
        Wait for the installation to complete, and then click on the "Reload" button to activate the extension.

    Install Code Runner Extension:
        In Visual Studio Code, click on the Extensions icon on the left sidebar or press Ctrl + Shift + X.
        In the Extensions view, search for "Code Runner" in the search bar.
        Click on the "Code Runner" extension offered by Jun Han and click on the "Install" button.
        Wait for the installation to complete, and then click on the "Reload" button to activate the extension.

    Set Up Python Interpreter:
        Open your Python script file or create a new Python file in Visual Studio Code.
        Click on the bottom-left corner of the VSCode window where it says "Select Interpreter" or click on the Python version displayed in the bottom status bar.
        Choose the desired Python interpreter from the list provided.
        If the interpreter is not listed, click on "Enter interpreter path" and provide the path to your Python executable.

    Configure Code Runner for Python:
        Press Ctrl + , to open the User Settings in Visual Studio Code.
        Search for "code-runner.executorMap" in the search bar within the settings.
        Under "User Settings", click on "Edit in settings.json" to modify the settings.
        In the "code-runner.executorMap" section, add the following line:

        css

        "code-runner.executorMap": {
           "python": "python -u",
        }

        Save the settings.

    Run the Python Script:
        Open your Python script in Visual Studio Code.
        Right-click within the editor or use the shortcut Ctrl + Alt + N to run the script using Code Runner.
        Observe the output in the integrated terminal.

Note: Make sure you have installed Python on your system (as explained in the previous guide) before proceeding with setting up Visual Studio Code for Python development.

By following these steps, you should be able to set up Visual Studio Code for Python development, install the necessary extensions, and execute your Python script using Code Runner.