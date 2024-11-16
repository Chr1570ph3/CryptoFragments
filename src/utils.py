import os
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def save_to_file(filename, data):
    """Save data into file."""
    with open(filename, 'wb') as f:
        f.write(data)

def load_from_file(filename):
    """Load data from file."""
    with open(filename, 'rb') as f:
        return f.read()


def export_to_qrcode(data, filename, output_dir="output"):
    """
    Export the given data to a QR code image file.

    :param data: The data to encode in the QR code.
    :param filename: The name of the output QR code file.
    :param output_dir: The directory where the QR code will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Save the QR code as an image
    img = qr.make_image(fill_color="black", back_color="white")
    output_path = os.path.join(output_dir, filename)
    img.save(output_path)
    print(f"QR Code saved: {output_path}")

# Function to decode QR code from an image file
def decode_qrcode(file_path):
    """
    Decode a QR code from an image file.

    :param file_path: The path to the QR code image file.
    :return: The data encoded in the QR code as bytes.
    """
    img = Image.open(file_path)
    decoded_objects = decode(img)
    if not decoded_objects:
        raise ValueError(f"No QR code found in file: {file_path}")
    return decoded_objects[0].data

