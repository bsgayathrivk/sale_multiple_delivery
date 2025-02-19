# -*- coding: utf-8 -*-
{
    'name': "sale_order_delivery",

    'summary': """
        Automates sale order confirmation with multiple deliveries for each product,
         ensuring identical products are grouped in a single delivery""",

    'description': """
        Long description of module's purpose
    """,

    'author': "gayathri shankar",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/multiple_delivery_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
