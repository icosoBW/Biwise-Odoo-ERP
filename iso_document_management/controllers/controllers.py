# -*- coding: utf-8 -*-
# from odoo import http


# class IsoDocumentManagement(http.Controller):
#     @http.route('/iso_document_management/iso_document_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iso_document_management/iso_document_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iso_document_management.listing', {
#             'root': '/iso_document_management/iso_document_management',
#             'objects': http.request.env['iso_document_management.iso_document_management'].search([]),
#         })

#     @http.route('/iso_document_management/iso_document_management/objects/<model("iso_document_management.iso_document_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iso_document_management.object', {
#             'object': obj
#         })
