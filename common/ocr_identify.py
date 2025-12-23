# encoding: utf-8
# @File  : ocr_identify.py
# @Author: 孔敬淳
# @Date  : 2025/12/22/11:46
# @Desc  : OCR图像识别工具类，用于识别图片中的文字内容
import ddddocr


class OCRIdentify:
    """OCR图像识别类，封装ddddocr库进行文字识别"""
    
    def __init__(self):
        """初始化OCR识别器"""
        self.ocr = ddddocr.DdddOcr()
    def identify(self, image):
        """识别图片中的文字内容
        
        :param image: 图片文件路径
        :return: 识别出的文字内容
        """
        # 以二进制模式读取图片文件
        with open(image, 'rb') as f:
            image_bytes = f.read()
        # 调用OCR识别引擎进行文字识别
        res = self.ocr.classification(image_bytes)
        return res