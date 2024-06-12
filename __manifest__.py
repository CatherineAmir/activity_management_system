# -*- coding: utf-8 -*-
{
    'name': "activity_management_system",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_sale','appointment','calendar'],

    # always loaded
    'data': [

        # 'security/ir.model.access.csv',
        'views/product.xml',
        # 'views/slot_configuration.xml',
        # 'views/slots.xml',
        # 'views/reservation.xml',
        'templates/ecommerce_template.xml',
        'views/appointment.xml',
        'views/reservation_event.xml',
        'templates/main_appointment_template.xml',
        'templates/portal_my_appointments.xml',
        'templates/footer.xml',
        'templates/remove_e_commerce_footer.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
