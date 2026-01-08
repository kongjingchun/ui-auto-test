# encoding: utf-8
# @File  : testcase_result.py
# @Author: 孔敬淳
# @Date  : 2025/12/24/19:35
# @Desc  :


from common.process_redis import Process
from common.ding_talk import send_dingtalk_msg_markdown
# from common.qywx import send_qywx_msg_markdown
from common.yaml_config import GetConf
from logs.log import log

# 获取测试结果
total, success, fail, _ = Process().get_result()

failed_testcases_name = ",失败的用例为:"
msg_str = f"测试通过{str(success)}个，失败{str(fail)}个"
# 如果有失败的，就加上失败的用例名称
if int(fail) > 0:
    msg_str += failed_testcases_name
    fail_testcase_names = Process().get_fail_testcase_names()
    for i in range(len(fail_testcase_names)):
        if i == len(fail_testcase_names) - 1:
            failed_testcases_name += fail_testcase_names[i]
        else:
            failed_testcases_name += fail_testcase_names[i] + ","
        msg_str += fail_testcase_names[i] + "\n"
else:
    failed_testcases_name = ""

# 在日志中输出测试执行结果汇总
log.info("=" * 80)
log.info("=" * 80)
log.info("=" * 20 + " 测试执行完成 - 结果汇总 " + "=" * 20)
log.info("=" * 80)
log.info(f"测试用例总数: {total}")
log.info(f"执行成功: {success} 个")
log.info(f"执行失败: {fail} 个")
log.info("=" * 80)

# 输出成功的用例信息
success_testcase_names = Process().get_success_testcase_names()
if success_testcase_names:
    log.info("=" * 20 + " 执行成功的用例 " + "=" * 20)
    for idx, testcase_name in enumerate(success_testcase_names, 1):
        log.info(f"  {idx}. {testcase_name}")
    log.info("=" * 80)
else:
    log.info("=" * 20 + " 执行成功的用例: 无 " + "=" * 20)
    log.info("=" * 80)

# 输出失败的用例信息
fail_testcase_names = Process().get_fail_testcase_names()
if fail_testcase_names:
    log.info("=" * 20 + " 执行失败的用例 " + "=" * 20)
    for idx, testcase_name in enumerate(fail_testcase_names, 1):
        log.info(f"  {idx}. {testcase_name}")
    log.info("=" * 80)
else:
    log.info("=" * 20 + " 执行失败的用例: 无 " + "=" * 20)
    log.info("=" * 80)

log.info("=" * 80)
log.info("=" * 80)

# 插入测试结束时间
Process().write_end_time()
# 更改运行状态为0
Process().modify_running_status(0)

# 项目名称
project_name = "UI_Auto_Test"
# 报告标题
report_title = "UI自动化测试-测试报告"
# jenkins地址
jenkins_url = GetConf().get_jenkins_url()["url"]
# allure测试报告地址
allure_url = jenkins_url + "/job/" + project_name + "/allure/"
# 本地部署时不发送钉钉消息
if not GetConf().is_local_deploy():
    # 发送报告到钉钉
    dingding_webhook = GetConf().get_dingding_webhook()
    send_dingtalk_msg_markdown(
        dingding_webhook,
        allure_url,
        total,
        success,
        fail,
        failed_testcases_name,
        report_title
    )
else:
    print("本地部署环境，不发送钉钉消息")
# 发送报告到企业微信
# qywx_webhook = GetConf().get_qywx_webhook()
# send_qywx_msg_markdown(
#     qywx_webhook, allure_url, report_title, total, success, fail, failed_testcases_name
# )
