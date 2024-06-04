## Parcel Task:
Create an application that uses parallel processes / multiprocessing via python using a browser environment to visualize the current reading of serial data from the movement of the mouse and when the left mouse’s button is pressed take a picture of a connected webcam. As a final result, to save the current coordinates of the mouse cursor and data-source of the image in sqllite database.


## Minimum Requirements
- Python 3.12
- SQLite3
- OpenCV (`cv2` module)
- NumPy
- FastAPI

## Setting Up a Virtual Environment
### For Windows, Mac, and Linux (Ubuntu)

### 1. Preparing the Virtual Environment

1. **Install Python 3.12**:
   - Ensure that Python 3.12 is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/). 
   - You can check your current version by typing the following command:

    For Windows 10+ users:
    - in Command Prompt type the following command:
    ```
    python --version
    ```
    for Mac/Linux user, in bash type the following command:
    ```
    python3.12 --version
    ```
    If versions is returned, that means that you already have the needed version. 
    
    Note: for some Linux version the pip mondule must be installed additionally. Make sure that you have pip installed, because we will need it on the next step.
    
    To check if pip is installed, enter the following command:
    ```
    python3.12 -m pip --version
    ```
    If version is returned, that means that pip is installed, otherwise use the following command to install it:
    ```
    python3.12 get-pip.py
    ```


2. **Create a Virtual Environment**:
   Open your terminal (Command Prompt on Windows, Terminal on Mac and Linux) and navigate to your project directory.
   
   To create virtual environment, use the following commands:
   
   For Windows 10+ users:
   ```
   python -m venv myenv
   ```

   For Mac/Linux users:
   ```
   python3.13 -m venv myenv
   ```

   To activate the virtual environment, use the following commands:

    For Windows 10+ users:
   ```
   myenv\Scripts\activate
   ```

   For Mac/Linux users:
   ```
   source myenv/bin/activate
   ```

3. **Install the requirements**:
    
    Enter the following command:
    For Winodows 10+ users:
    ```
    python -m pip -r requirements.py
    ```

    For Mac/Linux users:
    ```
    python3.12 -m pip -r requirements.py
    ```

### 1. Running the project
    
    To run the app localy, use the following command:

    ```
    fastapi dev main.py
    ```

    or
    ```
    uvicorn main:app
    ```
    Note: you can add --reload flag if you run the web server, using uvicorn.