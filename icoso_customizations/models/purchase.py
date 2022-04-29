from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    doc_type = fields.Selection(
        [('general', 'General'), ('bars', 'Barras'), ('spring', 'Resorte'), ('casting', 'Fundición')],
        string='Tipo de O.C.', default='general')


class IsoDocument(models.Model):
    _inherit = 'iso.document'

    doc_type = fields.Selection(
        [('general', 'General'), ('bars', 'Barras'), ('spring', 'Resorte'), ('casting', 'Fundición')],
        string='Tipo de doc.', default='general')
