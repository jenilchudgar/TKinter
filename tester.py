import pyautogui
import webbrowser

states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
]
pyautogui.sleep(2)
print("Start!")
for state in states:
    state = state.lower().split(" ")[0]
    webbrowser.open_new_tab(f'https://d-maps.com/m/asia/india/{state}/{state}06.gif')
    pyautogui.hotkey('ctrl','s')
    pyautogui.hotkey('ctrl','a')
    pyautogui.sleep(1)
    pyautogui.press('backspace')
    pyautogui.sleep(1)
    pyautogui.click(x=925, y=692)
    pyautogui.write(state+".png")
    pyautogui.press('enter')
    pyautogui.sleep(3)