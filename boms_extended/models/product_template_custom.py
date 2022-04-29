from odoo import _, models, fields, api
from odoo.osv import expression

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_bom = fields.Boolean('Es un BOM')

