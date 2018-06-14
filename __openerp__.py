# -*- coding: utf-8 -*-
{
    'name': "Purchase Report Custom",

    'summary': """
        Add the fields price, UoM and total in the purchase quotation""",

    'description': """
        Add the fields price, UoM and total in the purchase quotation
    """,

    'author': "Wildy Estephan",
    'website': "http://www.wildyestephan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}