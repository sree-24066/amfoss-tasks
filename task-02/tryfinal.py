import pytesseract as pt
from PIL import Image
image_path='/home/sreekanth/Downloads/canva4.png'
img=Image.open(image_path)
text=pt.image_to_string(img)
answer=eval(text)
print(answer)