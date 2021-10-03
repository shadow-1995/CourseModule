# -*- coding: utf-8 -*-
{
    'name': "Koko Networks - Courses",

    'summary': """
        Course Module
        """,

    'description': """

    """,

    'author': "Sunil Chauhan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/rooms.xml',
        'views/lessons.xml',
        'views/courses.xml',
        'views/partners.xml',
        'views/attendees.xml',
    
        'views/menuitems.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
