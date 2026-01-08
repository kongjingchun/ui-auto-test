# Linux 本地化部署指南

## 环境要求

### 系统要求
- Linux 操作系统（推荐 Ubuntu 20.04+ 或 CentOS 7+）

### 软件版本要求
- **Python**: >= 3.8（推荐 3.8 - 3.11）
- **pip**: 最新版本
- **Chrome**: 143.0.7499.192
- **ChromeDriver**: 143.0.7499.192（与 Chrome 版本完全匹配）

## 安装步骤

### 1. 安装 Python

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip

# 验证安装
python3 --version
pip3 --version
```

### 2. 安装 Chrome 143（指定版本）

#### 方法一：下载指定版本安装包

```bash
# Ubuntu/Debian - 下载 Chrome 143.0.7499.192
# 从 Chrome 版本历史存储库下载
wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_143.0.7499.192-1_amd64.deb
sudo dpkg -i google-chrome-stable_143.0.7499.192-1_amd64.deb
sudo apt-get install -f

# CentOS/RHEL - 下载 Chrome 143.0.7499.192
wget https://dl.google.com/linux/chrome/rpm/stable/x86_64/google-chrome-stable-143.0.7499.192-1.x86_64.rpm
sudo rpm -ivh google-chrome-stable-143.0.7499.192-1.x86_64.rpm
```

#### 方法二：使用版本号安装（如果可用）

```bash
# Ubuntu/Debian
# 添加 Google Chrome 仓库
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list

# 安装指定版本（需要先查看可用版本）
sudo apt update
apt-cache madison google-chrome-stable
sudo apt install google-chrome-stable=143.0.7499.192-1

# CentOS/RHEL
# 添加 Google Chrome 仓库
cat << EOF | sudo tee /etc/yum.repos.d/google-chrome.repo
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub
EOF

# 安装指定版本
sudo yum install google-chrome-stable-143.0.7499.192-1.x86_64
```

#### 验证安装

```bash
# 验证 Chrome 版本是否为 143.0.7499.192
google-chrome --version
# 应显示: Google Chrome 143.0.7499.192
```

### 3. 安装 ChromeDriver 143（与 Chrome 版本匹配）

```bash
# 方法一：从 Chrome for Testing 下载（推荐）
# 下载 ChromeDriver 143.0.7499.192
wget https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.192/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# 方法二：使用旧版存储库（备选）
# wget https://chromedriver.storage.googleapis.com/143.0.7499.192/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip
# sudo mv chromedriver /usr/local/bin/
# sudo chmod +x /usr/local/bin/chromedriver

# 验证安装
chromedriver --version
# 应显示: ChromeDriver 143.0.7499.192
```

**重要提示**: 
- ChromeDriver 版本必须与 Chrome 浏览器版本完全一致（143.0.7499.192）
- 如果使用项目自带的 `driver_files/chromedriver_linux`，请确保其版本为 143.0.7499.192

### 4. 安装项目依赖

```bash
# 进入项目目录
cd XuetangUI

# 安装 Python 依赖
pip3 install -r requirements.txt
```

### 5. 配置驱动路径

确保 `driver_files/chromedriver_linux` 文件存在且具有执行权限：

```bash
chmod +x driver_files/chromedriver_linux
```

### 6. 配置环境

根据实际环境修改 `config/environment.yaml` 配置文件。

**重要提示**：
- 在 `config/environment.yaml` 中设置 `部署环境.是否本地部署: True` 时，测试执行过程中和测试结束后**不会发送钉钉消息**
- 设置为 `False` 时，会在测试执行过程中和测试结束后发送钉钉消息通知

## 验证安装

```bash
# 运行测试用例验证环境
pytest testcases/ -v
```

## 运行测试用例并生成测试报告

### 生成 Allure 测试报告数据

```bash
# 运行测试用例并生成 Allure 报告数据（单进程运行）
pytest testcases/ --alluredir=UIreport -v -n 0
```

**参数说明**：
- `--alluredir=UIreport`: 指定 Allure 报告数据输出目录为 `UIreport`
- `-v`: 详细输出模式
- `-n 0`: 禁用并行执行（单进程运行）

### 生成测试报告

```bash
# 安装 Allure 命令行工具（如果未安装）
# Ubuntu/Debian
sudo apt install allure

# CentOS/RHEL
# 需要从 GitHub 下载或使用其他方式安装
```

#### 方法1：生成本地报告文件

```bash
# 生成静态 HTML 报告
# 格式：allure generate 测试报告数据地址 -o 报告存放地址
allure generate UIreport -o UIreport/report

# 然后在浏览器中打开 UIreport/report/index.html
```

#### 方法2：动态查看报告

```bash
# 生成并自动打开 Allure 报告（临时服务器）
allure serve UIreport
```

## 查看测试执行结果

### 测试执行过程中的日志

测试执行过程中，每个用例的执行状态都会实时记录到日志文件中：

- **用例开始执行**：`开始执行测试用例: {用例名称}`
- **用例执行成功**：`测试用例执行成功: {用例名称}`
- **用例执行失败**：`测试用例执行失败: {用例名称}`

日志文件保存在 `logs/all_logs/` 目录下，文件名格式为时间戳（如：`202512241930.log`）。

### 查看最终测试结果统计

测试执行完毕后，可以通过以下方式查看最终统计结果：

```bash
# 方式1：查看日志文件（推荐）
# 日志文件位于 logs/all_logs/ 目录，按时间戳命名
ls -lt logs/all_logs/ | head -5
cat logs/all_logs/最新日志文件名.log | grep -E "(执行成功|执行失败|测试通过|测试失败)"

# 方式2：运行结果统计脚本（如果配置了）
python testcase_result.py
```

**日志输出示例**：

```
================================================================================
==================== 开始执行测试用例: 测试用例名称 ====================
================================================================================
... 测试执行过程 ...
================================================================================
==================== 测试用例执行成功: 测试用例名称 ====================
================================================================================
```

**最终统计信息**（在日志末尾或通过 `testcase_result.py` 查看）：

```
测试通过X个，失败Y个
失败的用例为:
  用例名称1
  用例名称2
  ...
```

### 查看详细日志

```bash
# 查看最新的日志文件
tail -f logs/all_logs/最新日志文件名.log

# 或者查看所有日志中的成功/失败信息
grep -E "执行成功|执行失败" logs/all_logs/*.log
```

## 常见问题

1. **ChromeDriver 版本不匹配**: 确保 ChromeDriver 版本与 Chrome 143 完全匹配
2. **权限问题**: 确保 chromedriver 文件具有执行权限
3. **依赖安装失败**: 使用 `pip3 install --upgrade pip` 升级 pip 后重试
