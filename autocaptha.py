import pyautogui
import cv2
import requests
import io
import time


def do_captcha():
    print("5 seconds till it screenshots...")
    time.sleep(5)

    screenshot = pyautogui.screenshot()
    img_byte_arr = io.BytesIO()
    screenshot.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    coordinates = ai_prediction(img_byte_arr)

    if not coordinates:
        print("No matching targets")
        return

    for cords in coordinates:
        print(f"Clicking valid target at {cords}")
        pyautogui.moveTo(cords[0], cords[1])
        pyautogui.click()


API_URL = "https://3623e70dd3d7c7c6-8-231-48-199.serveousercontent.com/predict"


def ai_prediction(image_buffer):
    files = {'file': ('captcha.png', image_buffer, 'image/png')}
    headers = {"bypass-tunnel-reminder": "true"}

    try:
        response = requests.post(API_URL, files=files, headers=headers)
        response.raise_for_status()

        data = response.json()
        captcha_text = data["prompt"]
        boxes_list = data["boxes"]

        print(f"OCR Detected Screen Text: '{captcha_text}'")
    except Exception as e:
        print(f"api failed: {e}")
        return []

    target_label = None
    if "traffic light" in captcha_text:
        target_label = "traffic light"
    elif "car" in captcha_text or "vehicle" in captcha_text:
        target_label = "car"
    elif "bus" in captcha_text:
        target_label = "bus"
    elif "fire hydrant" in captcha_text:
        target_label = "fire hydrant"

    print(f"Targeting class: {target_label}")

    predictions = []
    for item in boxes_list:
        label = item["label"]
        cx, cy, w, h = item["coords"]

        if target_label and label == target_label:
            predictions.append((int(cx), int(cy)))
        elif target_label is None:
            pass

    return predictions


do_captcha()