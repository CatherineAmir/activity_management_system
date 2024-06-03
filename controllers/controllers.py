# -*- coding: utf-8 -*-
# from odoo import http


# class ActivityManagementSystem(http.Controller):
#     @http.route('/activity_management_system/activity_management_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/activity_management_system/activity_management_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('activity_management_system.listing', {
#             'root': '/activity_management_system/activity_management_system',
#             'objects': http.request.env['activity_management_system.activity_management_system'].search([]),
#         })

#     @http.route('/activity_management_system/activity_management_system/objects/<model("activity_management_system.activity_management_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('activity_management_system.object', {
#             'object': obj
#         })
