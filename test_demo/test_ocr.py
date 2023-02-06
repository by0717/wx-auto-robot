import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np


reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
result = reader.readtext('images/pannel_3.jpg', detail=0)
print(result)