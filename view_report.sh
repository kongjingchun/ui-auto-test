#!/bin/bash
# 查看 Allure 报告的脚本

cd "$(dirname "$0")"

echo "正在启动 Allure 报告服务器..."
echo "报告将在浏览器中自动打开"
echo "按 Ctrl+C 停止服务器"
echo ""

allure serve UIreport
