from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = "product.product"

    description = fields.Html('Description', translate=True)

