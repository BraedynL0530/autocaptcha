# AutoCaptcha

A proof-of-concept automated CAPTCHA solver that uses computer vision and OCR to detect and solve image-based CAPTCHAs. not very good but fun

## Overview

AutoCaptcha is an experimental project that combines object detection (YOLOv11) and optical character recognition (Tesseract) to automatically identify and click on CAPTCHA elements. The system consists of a backend API service and a client automation script.

## Features

- **Object Detection**: Uses YOLOv11 to detect CAPTCHA elements in screenshots
- **OCR Processing**: Leverages Tesseract for text recognition from CAPTCHA prompts
- **Automated Clicking**: Automatically locates and clicks on the correct CAPTCHA targets
- **FastAPI Backend**: Provides a REST API endpoint for processing CAPTCHA images
- **PyAutoGUI Integration**: Handles screenshot capture and automated mouse/click operations

## Project Structure

```
autocaptcha/
├── SuperCoolCaptchaBot.ipynb   # Jupyter notebook with server setup and inference code
├── autocaptha.py               # Main client script for CAPTCHA automation
├── cordTester.py               # Utility script for coordinate testing
└── README.md                   # This file
```

## Components

### SuperCoolCaptchaBot.ipynb
A Jupyter notebook that sets up and runs the FastAPI backend server. It:
- Installs required dependencies (YOLOv11, FastAPI, Tesseract OCR)
- Loads the YOLOv11 model for object detection
- Provides a `/predict` endpoint that accepts image uploads
- Processes images to extract CAPTCHA text and bounding boxes
- Uses SSH tunneling via serveo.net for remote access

**Key endpoint:**
- `POST /predict`: Accepts an image file and returns detected boxes and OCR text

### autocaptha.py
The client-side automation script that:
- Takes a screenshot of a specific screen region (hardcoded coordinates)
- Sends the image to the backend API
- Receives detected CAPTCHA elements and prompt text
- Matches detected objects to the prompt text
- Automatically clicks on the correct CAPTCHA targets

### cordTester.py
A simple utility script for testing and debugging:
- Polls and prints current mouse cursor coordinates
- Useful for calibrating the screenshot region in `autocaptha.py`

## Dependencies

**Python packages:**
- `ultralytics` - YOLOv11 for object detection
- `fastapi` - Web framework for the backend API
- `uvicorn` - ASGI server
- `opencv-python` - Image processing
- `pytesseract` - OCR interface
- `pyautogui` - Screenshot and mouse automation
- `requests` - HTTP client
- `nest_asyncio` - Async support in Jupyter

**System packages:**
- `tesseract-ocr` - OCR engine

## Installation & Setup

1. **Install Python dependencies:**
   ```bash
   pip install ultralytics fastapi uvicorn python-multipart pytesseract nest_asyncio pyautogui requests
   ```

2. **Install Tesseract OCR:**
   - **Ubuntu/Debian:** `apt-get install -y tesseract-ocr`
   - **macOS:** `brew install tesseract`
   - **Windows:** Download from [GitHub Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki)

3. **Set up the backend:**
   - Run the Jupyter notebook `SuperCoolCaptchaBot.ipynb` in Google Colab or a local Jupyter environment
   - The notebook will start the FastAPI server and expose it via SSH tunneling

4. **Update the API URL:**
   - Get the public URL from the `serveo.net` tunnel
   - Update `API_URL` in `autocaptha.py` with the actual endpoint

5. **Calibrate coordinates:**
   - Run `cordTester.py` to find your CAPTCHA region coordinates
   - Update the hardcoded coordinates in `autocaptha.py` (line 11: `region=(88, 202, 392, 569)`)

6. **Run the client:**
   ```bash
   python autocaptha.py
   ```

## How It Works

1. **Backend Server** (from notebook):
   - Accepts image uploads via `/predict` endpoint
   - Uses YOLOv11 to detect CAPTCHA elements and extract bounding boxes
   - Processes the header area with Tesseract to extract the CAPTCHA prompt
   - Returns JSON with detected boxes and OCR text

2. **Client Script**:
   - Captures a screenshot of the CAPTCHA area
   - Sends to the backend API
   - Parses the response to find boxes matching the prompt
   - Moves the mouse and clicks on each matching target

3. **Matching Logic**:
   - Compares detected object labels against the OCR'd CAPTCHA text
   - Clicks on all objects whose label appears in the prompt

## Notes & Limitations

- **Hardcoded Coordinates**: Screenshot region and object coordinates are hardcoded and need calibration per screen/resolution
- **Model Specific**: Trained/configured for specific CAPTCHA types
- **API Dependency**: Client requires the backend server to be running and accessible
- **No Persistence**: No caching or learning between runs
- **For Research Only**: This is an experimental proof-of-concept

## Disclaimer

This project is for educational and research purposes only. Bypassing CAPTCHAs may violate the terms of service of websites and applicable laws. Use responsibly and only on systems/services you own or have explicit permission to test.

## Language Composition

- **Jupyter Notebook**: 63.8%
- **Python**: 36.2%

## License

No license specified. Use at your own discretion.

---

**Repository**: https://github.com/BraedynL0530/autocaptcha
