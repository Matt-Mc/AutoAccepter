import pyautogui 
import time

def main():
    while True:
        try:
            print("Searching for the Accept Button")
            acceptButton = pyautogui.locateCenterOnScreen('img/LeagueAccept.png', grayscale=True, confidence=0.4)
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