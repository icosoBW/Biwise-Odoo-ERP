# -*- coding: utf-8 -*-
# from odoo import http


# class ServipumpsCustomizations(http.Controller):
#     @http.route('/servipumps_customizations/servipumps_customizations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/servipumps_customizations/servipumps_customizations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('servipumps_customizations.listing', {
#             'root': '/servipumps_customizations/servipumps_customizations',
#             'objects': http.request.env['servipumps_customizations.servipumps_customizations'].search([]),
#         })

#     @http.route('/servipumps_customizations/servipumps_customizations/objects/<model("servipumps_customizations.servipumps_customizations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('servipumps_customizations.object', {
#             'object': obj
#         })
