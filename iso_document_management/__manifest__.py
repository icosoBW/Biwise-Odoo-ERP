# -*- coding: utf-8 -*-
{
    "name": "ISO Document Management System",

    'summary': 'Document Management System for ISO standards',

    'description': """
        This module adds support to document version management
        for ISO9001 quality management system or any other ISO
        standards.""",

    'author': "Biwise",
    'website': "http://biwise.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'purchase', 'purchase_request', 'mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/iso_views.xml',

        'templates/purchase_report_templates.xml',
        'templates/purchase_request_templates.xml',
        #'templates/sale_report_templates.xml',
        'templates/mrp_bom_report_templates.xml',
        'templates/mrp_production_report_templates.xml',
        'templates/stock_report_templates.xml',
        #'templates/invoice_report_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
