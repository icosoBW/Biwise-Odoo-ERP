# -*- coding: utf-8 -*-
{
    'name': 'ICOSO Customizations',

    'summary': 'Custom fields and methods for ICOSO ERP',

    'description': "This module contains custom fields, views and methods to fit Servipumps operative needs",

    'author': "Biwise",
    'website': "https://biwise.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'purchase', 'iso_document_management', 'product'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/mrp_custom_views.xml',
        'views/purchase_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
