# encoding: utf-8
# @File  : OrderBase.py
# @Author: 孔敬淳
# @Date  : 2025/12/17/16:55
# @Desc  :

class OrderBase:
    @staticmethod
    def order_tab(tab_name):
        """
        订单tab按钮
        :param tab_name:全部、待付款、待发货、运输中、待确认、待评价
        :return:
        """
        return "//div[@role='tab' and text()='" + tab_name + "']"

    @staticmethod
    def order_operate(order_title, operate_name):
        """
        订单操作按钮
        :param order_title: 商品名称
        :param operate_name: 去支付、
        :return:
        """
        return "//div[text() = '" + order_title + "']/ancestor::tr//span[text()='" + operate_name + "']/parent::button"

    @staticmethod
    def order_operate_confirm():
        """
        订单操作确认按钮
        :return:
        """
        return "//div[contains(@style,'index')]//span[text()='确 定']/parent::button"

    @staticmethod
    def logistics():
        """
        物流公司
        :return:
        """
        return "//div[contains(@style,'index')]//input[@placeholder='请选择']/parent::div"

    @staticmethod
    def logistics_select(logistics_name):
        """
        物流公司选择框
        :param logistics_name:
        :return:
        """
        return "//span[text()='" + logistics_name + "']/parent::li"

    @staticmethod
    def logistics_tracking_number():
        """
        物流单号输入框
        :return:
        """
        return "//label[text()='物流单号']/following-sibling::div//input"

    @staticmethod
    def evaluation(num):
        """
        评价星级
        :param num:
        :return:
        """
        return "//span[text()='请给卖家评价']/following-sibling::div/span[" + str(num) + "]/i"

    @staticmethod
    def submit_evaluation():
        """
        提交评价
        :return:
        """
        return "//div[@aria-label='评价']//span[text()='确 定']"
