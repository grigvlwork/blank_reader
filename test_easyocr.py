import os.path

# import easyocr
import pytesseract
from PIL import Image

# def easyocr_recognition(path_img):
#     return easyocr.Reader(["ru"]).readtext(path_img, detail=0, paragraph=True, text_threshold=0.8)

# print(easyocr_recognition('./image_to_process/3_cr.png'))
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def teseract_recognition(path_img):
    return pytesseract.image_to_string(Image.open(path_img), lang='rus', config=r'--oem 3 --psm 6')

print(teseract_recognition('./image_to_process/3_cr.png'))