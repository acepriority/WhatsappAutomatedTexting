# WhatsappAutomatedTexting
This code demonstrates a Python script that uses Selenium to send automated WhatsApp messages at a scheduled time. The script opens the WhatsApp Web interface, logs in, searches for a contact or group, and sends a predefined message.

## Prerequisites

- Python 3.x
- Selenium library
- Chrome web driver

## Setup

1. Install Selenium library using pip:

   ```
   pip install selenium
   ```

2. Download the Chrome web driver that matches your Chrome browser version. Ensure that the driver executable is compatible with your operating system.

   - Download link: https://sites.google.com/a/chromium.org/chromedriver/downloads

3. Replace the `driver_path` variable with the path to your Chrome driver executable.

4. Set the `target` variable to the name of the contact or group you want to send the message to.

5. Modify the `message` variable to contain the desired message text.

## Usage

1. Run the script:

   ```
   python whatsappmessages.py
   ```

2. The script will open a Chrome browser window with the WhatsApp Web interface.

3. Scan the QR code with your WhatsApp mobile app to log in to WhatsApp Web.

4. Press Enter in the console to continue the script execution.

5. The script will search for the specified contact or group, send the message, and then close the browser.

## Scheduling

The script uses the `schedule` library to schedule the message sending at a specific time. By default, it is set to send the message every day at 08:00. You can modify the schedule by changing the `.at("06:00")` parameter to your preferred time.

## Note

Make sure to use this script responsibly and comply with WhatsApp's terms of service. Automated messaging on WhatsApp may be subject to restrictions, so ensure that your usage aligns with the applicable guidelines and regulations.

For optimal execution, keep your computer powered on and connected to the internet at the scheduled time.

## Disclaimer

This script is for educational purposes only. Use it responsibly and at your own risk. The author is not responsible for any misuse or damage caused by this script.
