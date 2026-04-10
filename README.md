# 👁️ AI Vision Desktop App

A simple Python-based AI that detects and describes objects in images using YOLO.

## 🚀 Easy Start Guide (No Git Required)

1. **Download:** Click the green **Code** button on GitHub and select **Download ZIP**.
2. **Extract:** Right-click the downloaded zip and "Extract All".
3. **Open:** Open the extracted folder in **VS Code**.
4. **Setup:**
   * Install the **Python Extension** in VS Code.
   * Open the VS Code Terminal and run: `pip install ultralytics pillow`
5. **Run:** Open `main.py` and click the **Play** button!

## 🛠️ Requirements
* Python 3.10 or newer (Make sure to check "Add to PATH" during installation!)
* Visual Studio Code


# Detailed Instructions:

Step 1: Install Python (The Foundation)
Open your browser and go to python.org/downloads.

Click the large yellow button that says "Windows".

Locate the downloaded .exe file in your Downloads folder and double-click it.

# CRITICAL: At the bottom of the installer window, check the box that says "Add Python to PATH". If you miss this, the project will not run.

Click "Install Now".

Once finished, click "Disable path length limit" (if the option appears) and then "Close".

Step 2: Install Visual Studio Code (The Editor)
Go to code.visualstudio.com.

Click "Download for Windows".

Run the installer and click "Next" through the agreements.

Tip: On the "Select Additional Tasks" screen, check "Add 'Open with Code' action to Windows Explorer context menu". This makes opening projects much easier later.

Click "Install" and then "Finish".

Step 3: Download Your Project
Go to "https://github.com/Ahil-Mohammad/YOLO/" GitHub page in your browser.

Click the green "<> Code" button.

Select "Download ZIP".

Go to your Downloads folder. Right-click the ZIP file and select "Extract All...".

Choose your Desktop as the destination so it’s easy to find, then click "Extract".

Step 4: Setting Up the Workspace in VS Code
Open Visual Studio Code.

Go to File > Open Folder... and select the folder you just extracted on your Desktop.

Trusting the Files: A pop-up will appear asking if you trust the authors.

Check the box "Trust the authors of all files in the parent folder".

Click "Yes, I trust the authors".

Install the Python Extension:

Click the Extensions icon on the left sidebar (looks like four squares).

Search for "Python" and find the one by Microsoft.

Click the blue "Install" button.

Step 5: Installing the AI Dependencies
In VS Code, go to the top menu and select Terminal > New Terminal. A black window appears at the bottom.

Type exactly this and press Enter:

pip install ultralytics pillow

Wait for the text to stop moving. If you see "Successfully installed," you are ready.

Step 6: Running the AI
On the left side of VS Code, click your script file (main.py).

Click the Play button (▷) in the top-right corner of the editor window.

The First Run: The terminal will show a progress bar. This is the computer downloading the YOLO model (the "AI Brain"). It only happens once.

The application window will pop up! You can now upload an image and see the results.
