# encoding: utf-8
# @File  : ding_talk.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/18:55
# @Desc  : 钉钉机器人消息发送工具
import requests
import json

from common.tools import get_every_wallpaper
from common.yaml_config import GetConf


def send_ding_talk(url, message, at_all=False):
    """
    发送钉钉机器人消息
    
    Args:
        url: 钉钉机器人webhook地址
        message: 要发送的消息内容
        at_all: 是否@所有人，默认为False
        
    Returns:
        bool: 发送成功返回True，失败返回False
    """
    # 构造钉钉消息格式
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        },
        "at": {
            "isAtAll": at_all
        }
    }

    try:
        # 发送POST请求到钉钉机器人webhook
        response = requests.post(url, headers=headers, data=json.dumps(data))
        result = response.json()

        # 检查返回结果
        if result.get("errcode") == 0:
            print(f"钉钉消息发送成功: {message}")
            return True
        else:
            print(f"钉钉消息发送失败: {result.get('errmsg')}")
            return False

    except Exception as e:
        print(f"钉钉消息发送异常: {str(e)}")
        return False


def send_dingtalk_msg_markdown(
        ding_webhook,
        allure_url,
        total_count,
        success_count,
        fail_count,
        failed_testcases_name,
        report_title
):
    """
    发送markdown格式的消息到钉钉
    :param ding_webhook: 钉钉群的webhook
    :param allure_url: allure地址
    :param total_count: 总数
    :param success_count: 成功个数
    :param fail_count: 失败个数
    :param failed_testcases_name: 失败的用例名称
    :param report_title: 报告标题
    :return:
    """
    # 获取壁纸
    wallpaper_url = get_every_wallpaper()
    headers = {"Content-Type": "application/json ;charset=utf-8"}
    if fail_count == 0:
        failed_testcases_name = ""
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": report_title,
            "text": "#### "
                    + report_title
                    + " \n >用例总数：{}个 \n > \n >测试结果：\n > 通过{}个 , 失败{}个{} \n>   ![每日壁纸]({})\n> ###### 点击查看测试报告 \n>  [Allure测试报告]({})".format(
                total_count,
                success_count,
                fail_count,
                failed_testcases_name,
                wallpaper_url,
                allure_url,
            ),
        },
    }
    res = requests.post(url=ding_webhook, json=data, headers=headers)
    print("发送钉钉消息，返回结果:", res.text)


if __name__ == '__main__':
    # 测试发送钉钉消息
    test_url = GetConf().get_dingding_webhook()
    test_message = "这是一条测试消息"
    # 不@所有人
    send_ding_talk(test_url, test_message)
    # @所有人
    send_ding_talk(test_url, "紧急通知：测试执行完成！", at_all=True)
