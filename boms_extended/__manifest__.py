# -*- coding: utf-8 -*-
{
    'name': 'BOMs extended',

    'summary': 'This module extends mrp and mrp.bom modules to add attributes to complex products',

    'description': "This module contains extra fields for BOM and BOM line views",

    'author': "Biwise",
    'website': "https://biwise.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'mrp', 'web_domain_field'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/mrp_custom_views.xml',
        'views/mrp_custom_menu.xml',
        'views/product_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
