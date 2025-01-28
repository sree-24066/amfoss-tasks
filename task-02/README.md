>> Downloaded the png file from the website canva

>>then installed pytesseract and Pillow using the following commands:

sudo apt install tesseract-ocr 

sudo apt install python3-pip 

pip install pytesseract 

pip install pillow 

#(Python-tesseract is an optical character recognition (OCR) tool for python.It will recognize and “read” the text embedded in images.)

#(Pillow is an open source library specifically designed for image processing using  Python)

>>code explanation:

image_path = '/home/sreekanth/Downloads/canva4.png'  (located the image path)

img = Image.open(image_path)                         (uing the open in the module PIl opens the image and hold in img)

text = pt.image_to_string(img)                       (this will converts the text found in the image to string)

answer = eval(text)                                  ( eval() is a function that will evaluate the string as python expression)

print(answer)

>>conlusion:

the text inside the image was 8+8 and successfully got the answer 16

in this task learned how to use Optical Character Recognition (OCR) to extract text from images.
Understood that pytesseract is a wrapper for Tesseract-OCR and it requires the OCR engine to run
also Understood Pillow as the important library for any task related to image processing
