# encoding: utf-8
# @File  : find_img.py
# @Author: kongjingchun
# @Date  : 2025/12/18/20:49
# @Desc  : 图像匹配工具类，用于在源图像中查找目标图像
import aircv as ac

from common.tools import get_project_path, sep


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
        # 读取源图像和目标图像
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        # 执行模板匹配
        match_result = ac.find_template(img_src, img_sch)
        # 返回置信度值，如果结果为空则返回None
        return match_result.get('confidence') if match_result else None


if __name__ == '__main__':
    # 测试图像匹配功能
    find_img = FindImg()
    result = find_img.get_confidence(
        get_project_path() + sep(['img', 'source_img', '123.png'],add_sep_before=True),
        get_project_path() + sep(['img', 'assert_img', '123.png'], add_sep_before=True)

    )
    # result = find_img.get_confidence(
    #     "D:\code\\trading_system_autotest\img\source_img\123.png",
    #     "D:\code\\trading_system_autotest\img\source_img\123.png"
    # )
    print(result)
