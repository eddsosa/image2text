## Making a textfile from an image file (pdf or image)

It uses 

Tesseract and OCR are used to recognice text from images.
 - First tramsform PDF into images, one each page.
 - Preprocess images if necesary. Preset on default.
 - Vias to numeric characters. Preset on default.
 - Extract text into a string and save it into a text file.


To use the function image to text use the following syntax.
Note it can use preprocess and a custom configuration.
- Preprocess is used for images that require basic adjustments to increase accuracy.
- Custom configuration is used to make the text identification vias to only numbers and $, / | symbols.
- Default is both options true

~~~py
text = image2text.image2text(file_name, preprocess = True, custom_conf = True)
text = image2text.image2text(file_name)
image2text.image2text(file_name, preprocess = True, custom_conf = True)
image2text.image2text(file_name)
~~~

image2text: Modular OCR Pipeline for Images and PDFs
image2text is a Python-based tool for extracting text from images and PDF files using Tesseract OCR. It supports preprocessing for improved accuracy and is designed with reproducibility and modularity in mind—ideal for scientific workflows, diagnostics, and document parsing.

🚀 Features
✅ Supports both image files and multi-page PDFs

🧼 Optional preprocessing: grayscale, denoising, thresholding, dilation

🔍 Configurable OCR engine and page segmentation modes

📄 Saves extracted text to a structured output file

📊 Ready for benchmarking and parameter sweeps

📦 Installation
bash
pip install -r requirements.txt
Dependencies:

pdf2image

pytesseract

opencv-python

numpy

Pillow

matplotlib

Make sure Tesseract OCR is installed and accessible in your system path.

🧪 Usage
python
from image2text import image2text

text = image2text("sample.pdf")
You’ll be prompted to:

Preprocess images (yes/no)

Use custom OCR configuration (yes/no)

Extracted text is saved to output.txt.

⚙️ Preprocessing Pipeline
text
RGB → Grayscale → Resize → Dilation → Bilateral Filter → Adaptive Threshold → Morphological Cleaning
You can modify parameters like:

resize_factor

adaptiveThreshold block size and constant

bilateralFilter kernel size and sigma values

📁 File Support
Supports:

Images: .jpg, .png, .tif, .bmp, .webp, etc.

PDFs: multi-page conversion via pdf2image

🧠 Custom OCR Configuration
Enable whitelist for numeric and symbolic OCR:

text
--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789.,|/$%
📜 License
This project is licensed under the MIT License. See LICENSE for details.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to modify.

🧭 Roadmap
[ ] CLI support via argparse

[ ] OCR confidence logging

[ ] Structured output (JSON/CSV)

[ ] Skew correction and contrast enhancement modules