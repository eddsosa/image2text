# image2text is a project to use images or images from pdf files to extract its text content.


import matplotlib.pyplot as plt
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2
import pytesseract
from PIL import Image 


# Convert the PDF to a list of PIL Image objects
# You can adjust the dpi for better quality, e.g., 300 or 600
def image2text(file_name, preprocess = True, custom_conf = True) -> str:
    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", 
                        ".svg", ".webp", ".avif", ".heic", ".heif", ".raw", ".cr2", 
                        ".nef", ".orf", ".sr2", ".pdf", ".eps", ".ai", ".psd", ".xcf")
    if file_name.lower().endswith(".pdf"):
        images = convert_from_path(file_name, dpi=300)
    elif file_name.lower().endswith(image_extensions):
        img = cv2.imread(file_name)
        images = [Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))]

    images

    fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(12,6))
    
    ax1.set_title('Raw image sample')
    ax1.imshow(images[0])
    ax1.axis('off')

    print("List of images:")
    for i, img in enumerate(images):
        print(f" - Image {i} type:", type(img))
    
    extracted_text = ""
    
    if preprocess is True:
        # Assuming `images` is a list of OpenCV-loaded images
        processed_images = [preprocess_for_ocr(img) for img in images]
        ax2.set_title('Processed image sample')
        ax2.imshow(processed_images[0], cmap='gray')
        ax2.axis('off')
        
        extracted_text = process_image2text(processed_images, custom_conf)
    elif preprocess is False:
        print("Okay, I will continuew without preprocess.")
        extracted_text = process_image2text(images, custom_conf)
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    return extracted_text


def preprocess_for_ocr(image, resize_factor=1):
    # Convert PIL to NumPy array
    img = np.array(image)

    # Convert RGB to BGR for OpenCV
    if img.ndim == 3 and img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize to improve OCR accuracy
    if resize_factor != 1:
        gray = cv2.resize(gray, None, fx=resize_factor, fy=resize_factor, interpolation=cv2.INTER_LINEAR)

    kernel_d = np.ones((3, 3), np.uint8)
    gray = cv2.dilate(gray, kernel_d, iterations=1)

    # Apply bilateral filter to reduce noise while keeping edges sharp
    filtered = cv2.bilateralFilter(gray, 9, 75, 75)
    # filtered = cv2.bilateralFilter(gray, 9, 75, 75)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 31, 2)
        #    thresh = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #                            cv2.THRESH_BINARY, 31, 2)

    # Optional: Morphological operations to clean up small artifacts
    kernel = np.ones((3, 3), np.uint8)
    #     kernel = np.ones((1, 1), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Convert back to PIL Image
    pil_result = Image.fromarray(cleaned)

    return pil_result

def process_image2text(images, custom_conf = True)->str:
    extracted_text=""
    if custom_conf is True:
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789.,|/$%'
    elif custom_conf is False:
        custom_config =None
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        

    for i, image in enumerate(images):
        # Use Tesseract to extract text from each image
        text = pytesseract.image_to_string(image, config=custom_config)
        extracted_text += f"--- Page {i+1} ---\n{text}\n\n"

    print("This is the content that will be written to the file." + "\n" + extracted_text)
    
    # Specify the filename
    filename = "output.txt"

    # Open the file in write mode ('w') and write the string
    # The 'with' statement ensures the file is automatically closed
    with open(filename, 'w') as file:
        file.write(extracted_text)

    print(f"String successfully saved to '{filename}'")
    return extracted_text