一、大致结构命名
# 项目根目录（大致）
project_root/
├──organization/  # 机构管理
│  ├──organization_portal.py  # 机构门户管理
│  └──__init__.py
├──dean_manage/  # 教务管理
│  ├──UserManage.py  # 用户管理
│  ├──role.py  # 角色管理
│  ├──course.py  # 课程管理
│  ├──admin_class.py  # 行政班管理
│  ├──semester.py  # 学期管理
│  └──__init__.py
├──data_center/  # 数据中心
│  ├──platform_statistics.py  # 平台访问统计
│  └──__init__.py
├──major/  # AI专业建设系统
│  ├──major_manage.py  # 专业管理
│  ├──major_dashboard.py  # 专业大屏管理
│  ├──major_portal.py  # 专业门户管理
│  ├──training_program.py  # 培养方案管理
│  ├──quality_control.py  # 专业质量管控∏
│  ├──exhibition_center.py  # 专业建设展示中心
│  ├──major_settings.py  # 专业设置
│  └──__init__.py
├──questionnaire/  # 问卷管理
│  ├──category.py  # 问卷分类
│  ├──tag.py  # 问卷标签
│  ├──questionnaire_list.py  # 问卷列表
│  ├──my_questionnaire.py  # 我的问卷
│  └──__init__.py
├──department_manage/  # 院系管理
│  ├──DepListManage.py  # 院系列表管理
│  ├──department_info.py  # 院系信息设置
│  ├──department_user.py  # 院系用户管理
│  ├──department_portal.py  # 院系门户管理
│  └──__init__.py
└──base_page.py  # PageObject公共基类

二、测试Linux准备工作
    依赖：
        Python      3.13.5
        pip         25.3
        git
    步骤：
        
        