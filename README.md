# Connectivity Checker and QR Code Generator

This Python script allows you to check the connectivity to `https://google.com` and optionally generate a QR code for the URL.

## Prerequisites

Before running the script, make sure you have Python installed on your system. The script uses the following Python libraries:

- `qrcode`: To generate QR codes
- `urllib`: To check connectivity and retrieve HTTP response codes

You can install the required libraries using pip:

```bash
pip install qrcode
```

## How to Use

1. Clone this repository or download the `main.py` script to your local machine.

2. Run the script using Python:

3. The script will check the connectivity to `https://google.com` and display the HTTP response code along with its status.

4. Optionally, you can choose to generate a QR code for the URL. Enter 'Y' or 'y' when prompted. The generated QR code will be saved as `image.jpg` in the current working directory.

## Sample Output

```
Checking connectivity:
The response code was 200 OK
Make QR code? (Y/N): Y
QR code generated and saved as "image.jpg".
```

## License

This project is licensed under the MIT License
