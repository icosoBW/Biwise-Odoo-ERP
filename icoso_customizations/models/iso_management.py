from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _compute_iso_process_num(self):
        for purchase in self:
            purchase_doc_type = purchase.doc_type
            iso_process_num = self.env['iso.document'].search(
                [('model', '=', 'purchase.order'), ('doc_type', '=', purchase_doc_type)]).process_num
            purchase.iso_process_num = iso_process_num

    def _compute_iso_document_name(self):
        for purchase in self:
            purchase_doc_type = purchase.doc_type
            if purchase_doc_type == 'general' or '':
                document_name = 'Orden de compra'
                purchase.iso_document_name = document_name
            else:
                document_name = self.env['iso.document'].search(
                    [('model', '=', 'purchase.order'), ('doc_type', '=', purchase_doc_type)]).name
                purchase.iso_document_name = document_name

    def _compute_iso_document_code(self):
        for purchase in self:
            purchase_doc_type = purchase.doc_type
            document_code = self.env['iso.document'].search(
                [('model', '=', 'purchase.order'), ('doc_type', '=', purchase_doc_type)]).code
            purchase.iso_document_code = document_code

    def _compute_iso_document_date_revised(self):
        for purchase in self:
            purchase_doc_type = purchase.doc_type
            document_date_revised = self.env['iso.document'].search(
                [('model', '=', 'purchase.order'), ('doc_type', '=', purchase_doc_type)]).date_revised
            purchase.iso_document_date_revised = document_date_revised

    def _compute_iso_document_revision(self):
        for purchase in self:
            purchase_doc_type = purchase.doc_type
            document_revision = self.env['iso.document'].search(
                [('model', '=', 'purchase.order'), ('doc_type', '=', purchase_doc_type)]).revision
            purchase.iso_document_revision = document_revision

