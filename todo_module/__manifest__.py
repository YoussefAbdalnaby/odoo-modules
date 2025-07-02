{
    'name': 'Simple TODO List',
    'version': '17.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Simple TODO list management',
    'description': """
Simple TODO List Module
=======================
A basic TODO list application with tasks and categories.

Features:
* Task management with categories
* Simple views for easy task tracking
* Basic workflow for task completion
    """,
    'author': 'youssef',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/task_views.xml',
        'views/category_views.xml',
        'views/menu_views.xml',
        'wizard/todo_wizard_views.xml',
        'report/todo_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
