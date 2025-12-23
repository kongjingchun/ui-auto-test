# encoding: utf-8
# @File  : find_img.py
# @Author: 孔敬淳
# @Date  : 2025/12/18/20:49
# @Desc  : 图像匹配工具类，用于在源图像中查找目标图像
import aircv as ac
import cv2

from common.report_add_img import add_img_path_2_report
from common.tools import get_project_path, sep, get_now_time_str


class FindImg:
    """图像匹配工具类"""

    def img_imread(self, img_path):
        """
        读取图像文件
        :param img_path: 图像文件路径
        :return: 图像对象
        """
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        在源图像中查找目标图像，返回匹配置信度
        :param source_path: 源图像路径（大图）
        :param search_path: 目标图像路径（小图）
        :return: 匹配置信度值，如果未找到匹配则返回None
        """
        # 步骤1: 读取源图像（被查找的大图）
        img_src = self.img_imread(source_path)
        # 步骤2: 读取目标图像（要查找的小图）
        img_sch = self.img_imread(search_path)
        # 步骤3: 使用模板匹配算法在源图像中查找目标图像，返回匹配结果（包含位置、置信度等信息）
        result = ac.find_template(img_src, img_sch)
        # 步骤4: 在源图像上绘制蓝色矩形框标记匹配位置
        # rectangle参数说明: 图像对象, 矩形左上角坐标, 矩形右下角坐标, 颜色, 线宽像素
        cv2.rectangle(
            img_src, result["rectangle"][0], result["rectangle"][3], color=(0, 0, 255), thickness=3
        )
        # 步骤5: 构建差异图片的保存路径（项目路径/img/diff_img/时间戳-对比的图.png）
        diff_img_path = get_project_path() + sep(["img", "diff_img", get_now_time_str() + "-对比的图.png"],
                                                 add_sep_before=True)
        # 步骤6: 将标记后的图像编码为PNG格式并保存到文件（使用tofile支持中文路径）
        cv2.imencode(".png", img_src)[1].tofile(diff_img_path)
        # 步骤7: 将对比图添加到测试报告中
        add_img_path_2_report(diff_img_path, "查找到的图")
        # 步骤8: 返回匹配置信度（0-1之间的浮点数，值越大表示匹配度越高）
        return result["confidence"]


if __name__ == '__main__':
    # 测试图像匹配功能
    find_img = FindImg()
    result = find_img.get_confidence(
        get_project_path() + sep(['img', 'source_img', '123.png'], add_sep_before=True),
        get_project_path() + sep(['img', 'assert_img', '123.png'], add_sep_before=True)
    )
    print(result)
