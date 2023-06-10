from dataStatic import *
from io import BytesIO
from PIL import Image
import easyocr
import base64
import numpy as np
import re


class tesseract_call:
    result = {'status': '', 'result': None}
    img64 = None

    def __init__(self, img_patch):
        self.img64 = img_patch

    def set_data(self):
        img_split = str(self.img64).split(',')[1]
        img_bytes = base64.b64decode(img_split)
        img = Image.open(BytesIO(img_bytes))

        # Save img byte to img png
        # img.save('image_process.png', 'PNG')

        reander = easyocr.Reader(['en'])
        result = reander.readtext(np.array(img))
        # result = reander.readtext('image_process.png')
        # font = cv2.FONT_HERSHEY_SIMPLEX

        # spacer = 100
        text_list = []
        count_score = 0
        confidence_percentage_list = 0
        for detection in result:
            text = detection[1]  # text
            text_list.append(text)
            score = detection[2]  # confidence
            confidence_percentage_list += round(score * 100, 1)  # convert to %
            count_score += 1

        confidence_percentage_list /= count_score

        # Remove Image
        # os.remove("image_process.png")

        text_str = ''.join(text_list).replace(' ', '')  # Join And Remove Spaces => ' '
        number_only = re.findall(r'\d+', text_str)  # Find Number Only

        return set_result(STATUS_SUCCESS, {'texts': ''.join(number_only), 'confidences': confidence_percentage_list})
