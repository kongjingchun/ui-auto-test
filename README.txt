一、项目结构说明
#项目根目录结构
XuetangUI/
├──base/  # 基础类目录（PageObject基类）
│  ├──__init__.py  # 基础类模块初始化文件
│  └──BasePage.py  # 基础页面类（Page Object Model基类）
│
├──page/  # 页面对象目录（PageObject实现类）
│  ├──__init__.py  # 页面对象模块初始化文件
│  ├──ai_major/  # AI专业建设系统页面
│  │  ├──__init__.py  # AI专业建设系统模块初始化文件
│  │  ├──MajorAIModel/  # AI模型相关页面
│  │  │  ├──__init__.py  # AI模型模块初始化文件
│  │  │  ├──MajorAIModelPage.py  # AI模型页面
│  │  │  └──MajorGraphModelPage.py  # 专业图谱模型页面
│  │  ├──MajorManagePage.py  # 专业管理页面
│  │  ├──MajorPortalManagePage.py  # 专业门户管理页面
│  │  ├──TrainingProgramManage/  # 培养方案管理页面
│  │  │  ├──__init__.py  # 培养方案管理模块初始化文件
│  │  │  └──TrainingProgramManagePage.py  # 培养方案管理页面
│  │  └──TrainingProgramRevisionPage.py  # 培养方案修订页面
│  ├──cms/  # CMS系统页面
│  │  ├──__init__.py  # CMS系统模块初始化文件
│  │  └──CmsUserManagePage.py  # CMS用户管理页面
│  ├──dean_manage/  # 教务管理页面
│  │  ├──__init__.py  # 教务管理模块初始化文件
│  │  ├──UserManagePage.py  # 用户管理页面
│  │  ├──RoleManagePage.py  # 角色管理页面
│  │  ├──CourseManagePage.py  # 课程管理页面
│  │  └──AdminClassManagePage.py  # 行政班管理页面
│  ├──department_manage/  # 院系管理页面
│  │  ├──__init__.py  # 院系管理模块初始化文件
│  │  └──DeptListManagePage.py  # 院系列表管理页面
│  ├──teacher_workbench/  # 教师工作台页面
│  │  ├──__init__.py  # 教师工作台页面对象模块初始化文件
│  │  ├──course_construction/  # 课程建设页面
│  │  │  ├──__init__.py  # 课程建设页面对象模块初始化文件
│  │  │  └──AIVerticalModelPage.py  # AI垂直模型页面
│  │  ├──CourseWorkbenchPage.py  # 课程工作台页面
│  │  └──MyTeachingCoursesPage.py  # 我教的课页面
│  ├──login/  # 登录相关页面
│  │  ├──__init__.py  # 登录模块初始化文件
│  │  └──LoginPage.py  # 登录页面
│  ├──LeftMenuPage.py  # 左侧菜单页面
│  └──TopMenuPage.py  # 顶部菜单页面
│
├──testcases/  # 测试用例目录
│  ├──__init__.py  # 测试用例模块初始化文件
│  ├──conftest.py  # pytest配置文件（fixture定义）
│  ├──helpers/  # 测试辅助工具目录
│  │  ├──__init__.py  # 测试辅助工具模块初始化文件
│  │  └──test_context_helper.py  # 测试上下文辅助工具类（封装登录、切换身份、切换学校等公共操作）
│  ├──testgqkt/  # 测试用例集合
│  │  ├──__init__.py  # 测试用例集合模块初始化文件
│  │  ├──test_001_user.py  # 用户管理测试用例
│  │  ├──test_002_dept.py  # 院系管理测试用例
│  │  ├──test_003_major.py  # 专业管理测试用例
│  │  ├──test_004_admin_class.py  # 行政班管理测试用例
│  │  ├──test_005_course.py  # 课程管理测试用例
│  │  ├──test_006_training_program.py  # 培养方案管理测试用例
│  │  ├──test_007_major_portal.py  # 专业门户管理测试用例
│  │  ├──test_008_ai_model.py  # AI模型测试用例
│  │  └──test_009_my_teaching_courses.py  # 我教的课测试用例
│  └──test_999_delete_data.py  # 数据清理测试用例
│
├──common/  # 公共工具目录
│  ├──__init__.py  # 公共工具模块初始化文件
│  ├──tools.py  # 通用工具函数
│  ├──yaml_config.py  # YAML配置文件读取
│  ├──mysql_operate.py  # MySQL数据库操作
│  ├──redis_operation.py  # Redis操作
│  ├──process_redis.py  # Redis进程处理
│  ├──ding_talk.py  # 钉钉通知
│  ├──ocr_identify.py  # OCR识别
│  ├──find_img.py  # 图片查找
│  ├──process_file.py  # 文件处理
│  └──report_add_img.py  # 报告图片添加
│
├──config/  # 配置文件目录
│  ├──__init__.py  # 配置文件模块初始化文件
│  ├──driver_config.py  # WebDriver驱动配置
│  └──environment.yaml  # 环境配置文件
│
├──driver_files/  # 浏览器驱动文件目录
│  ├──chromedriver  # Chrome浏览器驱动（macOS/Linux）
│  ├──chromedriver_linux  # Chrome浏览器驱动（Linux）
│  └──chromedriver.exe  # Chrome浏览器驱动（Windows）
│
├──logs/  # 日志目录
│  ├──__init__.py  # 日志模块初始化文件
│  ├──all_logs/  # 所有日志文件
│  ├──log.py  # 日志配置
│  ├──failed_testcases.json  # 失败测试用例记录
│  └──test_process.json  # 测试过程记录
│
├──img/  # 图片资源目录
│
├──assets/  # 资源文件目录
│  └──style.css  # 样式文件
│
├──UIreport/  # UI测试报告输出目录（Allure报告）
│
├──requirements.txt  # Python依赖包列表
├──pytest.ini  # pytest配置文件
├──pyproject.toml  # 项目配置文件
├──setup.cfg  # 安装配置文件
├──pyrightconfig.json  # Pyright类型检查配置文件
├──testcase_result.py  # 测试用例结果处理
├──Dockerfile  # Docker镜像构建文件
├──LINUX_DEPLOY.md  # Linux部署说明文档
└──README.txt  # 项目说明文档

二、测试Linux准备工作
    依赖：
        Python      3.13.5
        pip         25.3
        git
    步骤：
        
        