# **README.md**

## **About the Project**
This project is a personal voice assistant named **MAX**. It listens for the activation keyword **"MAX"**, plays a starting sound, processes voice commands, and performs specific tasks based on the given instructions. Tasks include opening applications, taking screenshots, fetching information, and more.

---

## **How It Works**
1. The assistant waits for the keyword **"MAX"**.
2. Once the keyword is detected:
   - A sound effect plays to indicate it is active.
   - It listens for your voice command.
3. The assistant processes the command and executes tasks such as:
   - Opening applications (e.g., YouTube, Chrome).
   - Fetching the date or time.
   - Playing music.
   - Locking the screen or minimizing windows.
   - Searching for information using **WolframAlpha**.
4. After the task is complete, an end sound plays to indicate the process is done.

---

## **Installation Instructions**
### **Required Modules**
Install the following Python libraries before running the project:
- **PyInstaller**: `pip install pyinstaller`
- **SpeechRecognition**: `pip install SpeechRecognition`
- **PyAudio**: Install from a compatible `.whl` file ([download here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)) and use:
  ```bash
  pip install path_to_pyaudio_whl_file
  ```
- **Pyttsx3**: `pip install pyttsx3`
- **PyAutoGUI**: `pip install pyautogui`
- **Playsound**: `pip install playsound`
- **WolframAlpha**: `pip install wolframalpha`

### **Project Files**
Ensure the following files are in the same directory:
- **`Main.py`**: The main assistant script.
- **`Voicy_Siri sound effect.mp3`**: The activation sound.
- **`end_sound.mp3`**: The completion sound.
- **`sound.mp3`**: Any additional sound effects.

---

## **How to Run**
### **Run with Python**
1. Open a terminal or command prompt.
2. Navigate to the directory containing the project files:
   ```bash
   cd path_to_project_directory
   ```
3. Run the assistant:
   ```bash
   python Main.py
   ```

### **Run as an EXE**
1. Navigate to the `dist` folder created during EXE generation.
2. Double-click `main.exe` to start the assistant.

---

## **Troubleshooting**
1. **PyAudio Not Found**:
   - Install PyAudio using a `.whl` file for your Python version:
     ```bash
     pip install path_to_pyaudio_whl_file
     ```

2. **Sound Files Not Found**:
   - Ensure all `.mp3` files are in the same folder as `Main.py` or use the correct file paths.

3. **EXE Not Working**:
   - Ensure the project was bundled correctly with PyInstaller:
     ```bash
     pyinstaller --onefile --add-data "Voicy_Siri sound effect.mp3;." --add-data "end_sound.mp3;." --add-data "sound.mp3;." Main.py
     ```

4. **Command Not Recognized**:
   - Speak clearly and ensure the microphone is properly configured.

5. **Module Not Found**:
   - Check that all required modules are installed using `pip`.

---

## **Key Features**
- **Voice Activation**: Detects the keyword **"MAX"** to start listening.
- **Task Execution**: Handles tasks such as:
  - Opening applications.
  - Fetching the date/time.
  - Taking screenshots.
  - Searching for information online.
  - Playing music.

- **Auditory Feedback**: Plays sounds to indicate when it is listening and when a task is complete.

---

## **Future Enhancements**
- Add support for additional commands.
- Improve voice recognition accuracy.
- Enable customizable activation keywords. 

---

## **Author**
Developed by RAVI .  
Feel free to report issues or contribute to the project!
