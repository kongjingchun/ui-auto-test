#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动本地 HTTP 服务器查看 Allure 报告
"""
import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8080
REPORT_DIR = Path(__file__).parent / "UIreport" / "report"


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(REPORT_DIR), **kwargs)


def main():
    if not REPORT_DIR.exists():
        print(f"错误：报告目录不存在: {REPORT_DIR}")
        print("请先运行: allure generate UIreport -o UIreport/report")
        return

    os.chdir(REPORT_DIR)

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print(f"Allure 报告服务器已启动")
        print(f"访问地址: {url}")
        print("按 Ctrl+C 停止服务器")
        print("")

        # 自动打开浏览器
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"无法自动打开浏览器: {e}")
            print(f"请手动访问: {url}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")


if __name__ == "__main__":
    main()
