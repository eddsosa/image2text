# Test pipeline of the module image2text
'''
Author: Eduardo Sosa
License: MIT

To use the function image to text use the following syntax.
Note it can use preprocess and a custom configuration.
- Preprocess is used for images that require basic adjustments to increase accuracy.
- Custom configuration is used to make the text identification vias to only numbers and .,|/$% symbols.
- Default is both options true


text = image2text.image2text(file_name, preprocess = True, custom_conf = True)
text = image2text.image2text(file_name)
image2text.image2text(file_name, preprocess = True, custom_conf = True)
image2text.image2text(file_name)
'''

image2text

# Define the input file
file_name = "testImage.pdf"  # Replace with your image or PDF path

# Option 1: Use default settings (preprocess=True, custom_conf=True)
text = image2text.image2text(file_name)
print("Extracted text with default settings:\n")
print(text)

# Option 2: Explicitly set preprocessing and custom OCR configuration
text_custom = image2text.image2text(file_name, preprocess=True, custom_conf=False)
print("\nExtracted text with preprocessing but no custom OCR config:\n")
print(text_custom)