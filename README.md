# cbseResults2023
 This is a selenium based Python Script to get Score Cards of your Entire School(ofc 12th students)

## You need to clone this Repository in order to use it
### Step-by-Step Guide: Cloning a GitHub Repository on Windows
Install Git:

    Visit the official Git website at https://git-scm.com/.
    Download the Git installer for Windows.
    Run the installer and follow the on-screen instructions.
    Choose the desired installation options and complete the installation process.

Open Git Bash:

    After Git installation, search for "Git Bash" in the Start menu and open it.

Navigate to the Desired Directory:

    Use the cd command in Git Bash to navigate to the directory where you want to clone the repository.
    For example, to navigate to the "Documents" directory, use the command: cd Documents

Clone the Repository:

    In your web browser, go to the GitHub repository you want to clone.
    Click on the "Code" button and copy the repository URL.
    In Git Bash, use the command git clone https://github.com/vasujain275/cbseResults2023.git to clone the repository.
        

## Step-by-Step Guide: Setting up and Running this Python Script on Windows
Install Python:

    Visit the official Python website at https://www.python.org/.
    Click on the "Downloads" tab.
    Choose the latest stable version of Python for Windows.
    Download the installer that corresponds to your system architecture (32-bit or 64-bit).
    Run the installer and follow the on-screen instructions.
    During the installation process, make sure to select the option to add Python to your system's PATH.

Verify Python Installation:

    Open the Command Prompt by pressing Win + R and typing cmd, then hit Enter.
    Type python --version and press Enter.
    The installed Python version should be displayed in the Command Prompt window, indicating a successful installation.

Install Required Dependencies:

    Navigate to the directory where you have stored your Python script using the cd command in Command Prompt.
    If your script relies on any external libraries or modules, you may need to install them using pip, the Python package installer.
    To install a package, use the command pip install selenium in the Command Prompt.

Configure the Script:

    Open the Python script using a text editor of your choice.(Use VSCode if you are beginner)
    Look for any configurable variables or settings within the script that I have commented.(Like Roll Numbers and School Numbers)
    Adjust those variables according to your requirements. For example, you may need to specify the file path to driver,etc

### Step-by-Step Guide: Installing Visual Studio Code (VSCode) and Setting it up for Python Development

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

Run the Python Script:

        Open your Python script in Visual Studio Code.
        Right-click within the editor or use the shortcut Ctrl + Alt + N to run the script using Code Runner.
        Observe the output in the integrated terminal.

Note: Make sure you have installed Python on your system (as explained in the previous guide) before proceeding with setting up Visual Studio Code for Python development.

By following these steps, you should be able to set up Visual Studio Code for Python development, install the necessary extensions, and execute your Python script using Code Runner.

## Installing Chromium Driver and Checking Chrome Version

This guide provides step-by-step instructions for installing the Chromium Driver and checking the Chrome version on your system to ensure compatibility. Please follow these steps:

Determine Chrome Version:

    Launch Google Chrome on your Windows PC.
    Click the three-dot menu icon at the top right corner of the browser window.
    Select "Help" from the dropdown menu, then click on "About Google Chrome".
    A new tab will open, displaying the Chrome version number. Note this version number for later reference.

Download Chromium Driver:

    Open your preferred web browser and visit the official Chromium Driver website at https://sites.google.com/a/chromium.org/chromedriver/downloads.
    Locate the version of the Chromium Driver that matches your Chrome version from the list of available downloads.
    Click on the download link associated with the appropriate driver version for your system.

Extract the Chromium Driver:

    Once the download is complete, extract the downloaded ZIP file to Drivers subfolder of this project.

Please Confirm Chrome and Chromium Driver Compatibility!

## In order to tailor the roll number settings in the code to your specific requirements, please follow the steps outlined below:

Locate the "rolls" Variable:

        Search for the variable named "rolls" within the code.

Estimate the Roll Number Range:

        Make an informed estimate of your school's roll numbers starting point which is generally situated approximately 50-100 places before or after your own roll number.

Adjust the School Number:

        Locate the section in the code that pertains to the school number.
        Update the existing school number with the correct school number applicable to your institution.

Modify the Roll Number Values:

        Within the "rolls" variable, you will find two values that need to be changed.(Look in for loop)
        The first value corresponds to the beginning value of the roll numbers used in your school.
        The second value represents the expected end value of the roll numbers.
        Update these two values accordingly to match your school's roll number range.

Save the Report Cards:

        Prior to running the script, ensure that a folder named "Results" already exists in the same directory as the script.
        Once the script has completed its execution, all the generated report cards will be automatically saved in the "Results" folder, organized based on roll numbers.