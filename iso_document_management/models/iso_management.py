from odoo import models, fields, api, _


class IsoDocument(models.Model):
    _name = 'iso.document'
    _description = 'ISO documents'

    name = fields.Char('Nombre')
    iso_process_num = fields.Integer('No. Proceso')
    process = fields.Char('Proceso')
    sequence = fields.Integer('Número')
    code = fields.Char('Codigo')
    date_revised = fields.Date('Fecha de revisión')
    date_created = fields.Date('Fecha de elaboración')
    revision = fields.Float('Número de revisión')
    responsible = fields.Many2one('hr.job', 'Responsable')
    document_url = fields.Char('Ubicación')
    created_by = fields.Many2one('res.partner', 'Elaborado por')
    model = fields.Many2one('ir.model', 'Modelo relacionado')


class MRPBOM(models.Model):
    _inherit = 'mrp.bom'

    iso_process_num = fields.Char('Número de proceso', compute='_compute_iso_process_num')
    iso_document_name = fields.Char('Documento ISO', compute='_compute_iso_document_name')
    iso_document_code = fields.Char('Código ISO', compute='_compute_iso_document_code')
    iso_document_date_revised = fields.Char('Fecha de revisión', compute='_compute_iso_document_date_revised')
    iso_document_revision = fields.Char('Número de revisión', compute='_compute_iso_document_revision')

    def _compute_iso_process_num(self):
        for bom in self:
            iso_process_num = self.env['iso.document'].search([('model', '=', 'mrp.bom')]).iso_process_num
            bom.iso_process_num = iso_process_num

    def _compute_iso_document_name(self):
        for bom in self:
            document_name = self.env['iso.document'].search([('model', '=', 'mrp.bom')]).name
            bom.iso_document_name = document_name

    def _compute_iso_document_code(self):
        for bom in self:
            document_code = self.env['iso.document'].search([('model', '=', 'mrp.bom')]).code
            bom.iso_document_code = document_code

    def _compute_iso_document_date_revised(self):
        for bom in self:
            document_date_revised = self.env['iso.document'].search([('model', '=', 'mrp.bom')]).date_revised
            bom.iso_document_date_revised = document_date_revised

    def _compute_iso_document_revision(self):
        for bom in self:
            document_revision = self.env['iso.document'].search([('model', '=', 'mrp.bom')]).revision
            bom.iso_document_revision = document_revision


class PurchaseRequest(models.Model):
    _inherit = 'purchase.request'

    iso_process_num = fields.Char('Número de proceso', compute='_compute_iso_process_num')
    iso_document_name = fields.Char('Documento ISO', compute='_compute_iso_document_name')
    iso_document_code = fields.Char('Código ISO', compute='_compute_iso_document_code')
    iso_document_date_revised = fields.Char('Fecha de revisión', compute='_compute_iso_document_date_revised')
    iso_document_revision = fields.Char('Número de revisión', compute='_compute_iso_document_revision')

    def _compute_iso_process_num(self):
        for request in self:
            iso_process_num = self.env['iso.document'].search([('model', '=', 'purchase.request')]).iso_process_num
            request.iso_process_num = iso_process_num

    def _compute_iso_document_name(self):
        for request in self:
            document_name = self.env['iso.document'].search([('model', '=', 'purchase.request')]).name
            request.iso_document_name = document_name

    def _compute_iso_document_code(self):
        for request in self:
            document_code = self.env['iso.document'].search([('model', '=', 'purchase.request')]).code
            request.iso_document_code = document_code

    def _compute_iso_document_date_revised(self):
        for request in self:
            document_date_revised = self.env['iso.document'].search([('model', '=', 'purchase.request')]).date_revised
            request.iso_document_date_revised = document_date_revised

    def _compute_iso_document_revision(self):
        for request in self:
            document_revision = self.env['iso.document'].search([('model', '=', 'purchase.request')]).revision
            request.iso_document_revision = document_revision


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    iso_process_num = fields.Char('Número de proceso', compute='_compute_iso_process_num')
    iso_document_name = fields.Char('Documento ISO', compute='_compute_iso_document_name')
    iso_document_code = fields.Char('Código ISO', compute='_compute_iso_document_code')
    iso_document_date_revised = fields.Char('Fecha de revisión', compute='_compute_iso_document_date_revised')
    iso_document_revision = fields.Char('Número de revisión', compute='_compute_iso_document_revision')

    def _compute_iso_process_num(self):
        for picking in self:
            iso_process_num = self.env['iso.document'].search([('model', '=', 'stock.picking')]).iso_process_num
            picking.iso_process_num = iso_process_num

    def _compute_iso_document_name(self):
        for picking in self:
            document_name = self.env['iso.document'].search([('model', '=', 'stock.picking')]).name
            picking.iso_document_name = document_name

    def _compute_iso_document_code(self):
        for picking in self:
            document_code = self.env['iso.document'].search([('model', '=', 'stock.picking')]).code
            picking.iso_document_code = document_code

    def _compute_iso_document_date_revised(self):
        for picking in self:
            document_date_revised = self.env['iso.document'].search([('model', '=', 'stock.picking')]).date_revised
            picking.iso_document_date_revised = document_date_revised

    def _compute_iso_document_revision(self):
        for picking in self:
            document_revision = self.env['iso.document'].search([('model', '=', 'stock.picking')]).revision
            picking.iso_document_revision = document_revision


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    iso_process_num = fields.Char('Documento ISO', compute='_compute_iso_process_num')
    iso_document_name = fields.Char('Documento ISO', compute='_compute_iso_document_name')
    iso_document_code = fields.Char('Código ISO', compute='_compute_iso_document_code')
    iso_document_date_revised = fields.Char('Fecha de revisión', compute='_compute_iso_document_date_revised')
    iso_document_revision = fields.Char('Número de revisión', compute='_compute_iso_document_revision')

    def _compute_iso_process_num(self):
        for purchase in self:
            iso_process_num = self.env['iso.document'].search([('model', '=', 'purchase.order')]).iso_process_num
            purchase.iso_process_num = iso_process_num

    def _compute_iso_document_name(self):
        for purchase in self:
            document_name = self.env['iso.document'].search([('model', '=', 'purchase.order')]).name
            purchase.iso_document_name = document_name

    def _compute_iso_document_code(self):
        for purchase in self:
            document_code = self.env['iso.document'].search([('model', '=', 'purchase.order')]).code
            purchase.iso_document_code = document_code

    def _compute_iso_document_date_revised(self):
        for purchase in self:
            document_date_revised = self.env['iso.document'].search([('model', '=', 'purchase.order')]).date_revised
            purchase.iso_document_date_revised = document_date_revised

    def _compute_iso_document_revision(self):
        for purchase in self:
            document_revision = self.env['iso.document'].search([('model', '=', 'purchase.order')]).revision
            purchase.iso_document_revision = document_revision


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    iso_process_num = fields.Char('Número de proceso', compute='_compute_iso_process_num')
    iso_document_name = fields.Char('Documento ISO', compute='_compute_iso_document_name')
    iso_document_code = fields.Char('Código ISO', compute='_compute_iso_document_code')
    iso_document_date_revised = fields.Char('Fecha de revisión', compute='_compute_iso_document_date_revised')
    iso_document_revision = fields.Char('Número de revisión', compute='_compute_iso_document_revision')

    def _compute_iso_process_num(self):
        for order in self:
            iso_process_num = self.env['iso.document'].search([('model', '=', 'mrp.production')]).iso_process_num
            order.iso_process_num = iso_process_num

    def _compute_iso_document_name(self):
        for order in self:
            document_name = self.env['iso.document'].search([('model', '=', 'mrp.production')]).name
            order.iso_document_name = document_name

    def _compute_iso_document_code(self):
        for order in self:
            document_code = self.env['iso.document'].search([('model', '=', 'mrp.production')]).code
            order.iso_document_code = document_code

    def _compute_iso_document_date_revised(self):
        for order in self:
            document_date_revised = self.env['iso.document'].search([('model', '=', 'mrp.production')]).date_revised
            order.iso_document_date_revised = document_date_revised

    def _compute_iso_document_revision(self):
        for order in self:
            document_revisi