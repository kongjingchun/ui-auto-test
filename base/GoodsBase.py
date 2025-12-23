# encoding: utf-8
# @File  : GoodsBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/16/16:24
# @Desc  : 商品页面元素定位基类，提供商品相关页面元素的XPath定位表达式


class GoodsBase:
    """商品页面元素定位基类
    
    提供商品管理页面中各种元素的XPath定位表达式，包括：
    - 商品标题输入框
    - 商品详情输入框
    - 商品数量输入框和增减按钮
    - 商品图片上传按钮
    - 商品单价输入框
    """

    def goods_title(self):
        """
        获取商品标题输入框的XPath定位表达式
        
        Returns:
            str: 商品标题输入框的XPath表达式
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        """
        获取商品详情输入框的XPath定位表达式
        
        Returns:
            str: 商品详情输入框的XPath表达式
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_num(self, plus=True):
        """
        获取商品数量相关元素的XPath定位表达式
        
        Args:
            plus (bool): 如果为True，返回数量增加按钮的XPath；如果为False，返回数量输入框的XPath
                        默认值为True
        
        Returns:
            str: 商品数量增加按钮或输入框的XPath表达式
        """
        if plus:
            # 返回数量增加按钮（加号按钮）的XPath
            return "//div[@class='el-input-number el-input-number--mini']//i[@class='el-icon-plus']/parent::span"
        else:
            # 返回数量输入框的XPath
            return "//div[@class='el-input-number el-input-number--mini']//input[@placeholder='商品数量']"

    def goods_img(self):
        """
        获取商品图片上传按钮的XPath定位表达式
        
        Returns:
            str: 商品图片上传按钮的XPath表达式
        """
        return "//input[@type='file']"

    def goods_price(self):
        """
        获取商品单价输入框的XPath定位表达式
        
        Returns:
            str: 商品单价输入框的XPath表达式
        """
        return "//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        获取商品状态选择框的XPath定位表达式

        Returns:
            str: 商品状态选择框的XPath表达式
        """

        return "//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, button_name):
        """
        获取指定商品状态选项的XPath定位表达式

        Args:
            status (str): 商品状态选项的文本内容

        Returns:
            str: 指定商品状态选项的XPath表达式
        """
        return "//span[text()='" + button_name + "']/parent::li"

    def add_goods_bottom_button(self, button_name):
        """
        新增二手商品底部按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"
