一、项目结构说明
#项目根目录结构
xc-autotest-ui/
├──base/  # 基础类目录（PageObject基类）
│  ├──ai_major/  # AI专业建设系统基础类
│  │  ├──MajorAIModel/  # AI模型相关
│  │  │  ├──MajorAIModelBase.py  # AI模型基础类
│  │  │  └──MajorGraphModelBase.py  # 专业图谱模型基础类
│  │  ├──MajorManageBase.py  # 专业管理基础类
│  │  ├──MajorPortalManageBase.py  # 专业门户管理基础类
│  │  └──TrainingProgramManage/  # 培养方案管理
│  │     ├──TrainingProgramManageBase.py  # 培养方案管理基础类
│  │     └──TrainingProgramRevisionBase.py  # 培养方案修订基础类
│  ├──cms/  # CMS系统基础类
│  │  └──CmsUserManageBase.py  # CMS用户管理基础类
│  ├──dean_manage/  # 教务管理基础类
│  │  ├──UserManageBase.py  # 用户管理基础类
│  │  ├──RoleManageBase.py  # 角色管理基础类
│  │  ├──CourseManageBase.py  # 课程管理基础类
│  │  └──AdminClassManageBase.py  # 行政班管理基础类
│  ├──department_manage/  # 院系管理基础类
│  │  └──DeptListManageBase.py  # 院系列表管理基础类
│  ├──teacher_workbench/  # 教师工作台基础类
│  │  ├──__init__.py  # 教师工作台基础类模块
│  │  ├──course_construction/  # 课程建设基础类
│  │  │  ├──__init__.py  # 课程建设基础类模块
│  │  │  └──AIVerticalModelBase.py  # AI垂直模型基础类
│  │  └──my_teaching_courses/  # 我教的课基础类
│  │     ├──__init__.py  # 我教的课基础类模块
│  │     └──MyTeachingCoursesBase.py  # 我教的课基础类
│  ├──login/  # 登录相关基础类
│  │  └──LoginBase.py  # 登录基础类
│  ├──LeftMenuBase.py  # 左侧菜单基础类
│  ├──TopMenuBase.py  # 顶部菜单基础类
│  └──ObjectMap.py  # 对象映射工具类
│
├──page/  # 页面对象目录（PageObject实现类）
│  ├──ai_major/  # AI专业建设系统页面
│  │  ├──MajorAIModel/  # AI模型相关页面
│  │  │  ├──MajorAIModelPage.py  # AI模型页面
│  │  │  └──MajorGraphModelPage.py  # 专业图谱模型页面
│  │  ├──MajorManagePage.py  # 专业管理页面
│  │  ├──MajorPortalManagePage.py  # 专业门户管理页面
│  │  ├──TrainingProgramManage/  # 培养方案管理页面
│  │  │  └──TrainingProgramManagePage.py  # 培养方案管理页面
│  │  └──TrainingProgramRevisionPage.py  # 培养方案修订页面
│  ├──cms/  # CMS系统页面
│  │  └──CmsUserManagePage.py  # CMS用户管理页面
│  ├──dean_manage/  # 教务管理页面
│  │  ├──UserManagePage.py  # 用户管理页面
│  │  ├──RoleManagePage.py  # 角色管理页面
│  │  ├──CourseManagePage.py  # 课程管理页面
│  │  └──AdminClassManagePage.py  # 行政班管理页面
│  ├──department_manage/  # 院系管理页面
│  │  └──DeptListManagePage.py  # 院系列表管理页面
│  ├──teacher_workbench/  # 教师工作台页面
│  │  ├──__init__.py  # 教师工作台页面对象模块
│  │  ├──course_construction/  # 课程建设页面
│  │  │  ├──__init__.py  # 课程建设页面对象模块
│  │  │  └──AIVerticalModelPage.py  # AI垂直模型页面
│  │  └──my_teaching_courses/  # 我教的课页面
│  │     ├──__init__.py  # 我教的课页面对象模块
│  │     └──MyTeachingCoursesPage.py  # 我教的课页面
│  ├──login/  # 登录相关页面
│  │  └──LoginPage.py  # 登录页面
│  ├──LeftMenuPage.py  # 左侧菜单页面
│  └──TopMenuPage.py  # 顶部菜单页面
│
├──testcases/  # 测试用例目录
│  ├──conftest.py  # pytest配置文件（fixture定义）
│  ├──helpers/  # 测试辅助工具目录
│  │  ├──__init__.py  # 测试辅助工具模块
│  │  └──test_context_helper.py  # 测试上下文辅助工具类（封装登录、切换身份、切换学校等公共操作）
│  └──testgqkt/  # 测试用例集合
│     ├──test_001_user.py  # 用户管理测试用例
│     ├──test_002_dept.py  # 院系管理测试用例
│     ├──test_003_major.py  # 专业管理测试用例
│     ├──test_004_admin_class.py  # 行政班管理测试用例
│     ├──test_005_course.py  # 课程管理测试用例
│     ├──test_006_training_program.py  # 培养方案管理测试用例
│     ├──test_007_major_portal.py  # 专业门户管理测试用例
│     ├──test_008_ai_model.py  # AI模型测试用例
│     ├──test_009_my_teaching_courses.py  # 我教的课测试用例
│     └──test_999_delete_data.py  # 数据清理测试用例
│
├──common/  # 公共工具目录
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
│  ├──driver_config.py  # WebDriver驱动配置
│  └──environment.yaml  # 环境配置文件
│
├──driver_files/  # 浏览器驱动文件目录
│  └──chromedriver  # Chrome浏览器驱动（Windows需为chromedriver.exe）
│
├──logs/  # 日志目录
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
├──UIreport/  # UI测试报告输出目录
│
├──requirements.txt  # Python依赖包列表
├──pytest.ini  # pytest配置文件
├──pyproject.toml  # 项目配置文件
├──setup.cfg  # 安装配置文件
├──testcase_result.py  # 测试用例结果处理
└──README.txt  # 项目说明文档

二、测试Linux准备工作
    依赖：
        Python      3.13.5
        pip         25.3
        git
    步骤：
        
        