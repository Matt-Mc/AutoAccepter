import pyautogui 
import time
import os

def main():
    imgFolder = 'img'
    imgFiles = [f for f in os.listdir(imgFolder) if f.endswith('.png')]
   
    while True:
        try:
            for image in imgFiles:
                print(f"Searching for the Accept Button in {image}")
                acceptButton = pyautogui.locateCenterOnScreen(os.path.join(imgFolder, image), grayscale=True, confidence=0.4)
                print(acceptButton)
        except Exception as e:
            acceptButton = None
        if acceptButton:
            print("Accept Button found")
            pyautogui.click(acceptButton)
            break
        
        time.sleep(1)



if __name__ == "__main__":
    main()