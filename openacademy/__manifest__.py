# -*- coding: utf-8 -*-
{
    'name': "OpenAcademy",
    'summary': "Course and Session Management System",
    'description': """
        OpenAcademy Module
        ==================
        Manage educational courses and training sessions with:
        * Course creation and management
        * Session scheduling and tracking
        * Student enrollment and attendance
    """,
    'author': "Youssef Abdalnaby",
    'version': '1.0.0',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course.xml',
        'views/session.xml',
        'views/menu_views.xml',
        'wizard/wizard.xml',
        'reports/session_report.xml',
    ],
    'installable': True,
    'application': True,
}