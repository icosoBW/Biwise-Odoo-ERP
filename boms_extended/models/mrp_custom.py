from odoo import _, models, fields, api
from odoo.tools import float_round
import json


class MRPBOM(models.Model):
    """ BOM Inherit """
    _inherit = 'mrp.bom'

    bom_level = fields.Selection(string='Nivel de BOM',
                                 selection=[('lvl1', 'Nivel 1'), ('lvl2', 'Nivel 2'), ('lvl3', 'Nivel 3'),
                                            ('lvl4', 'Nivel 4')])
    product_description = fields.Html('Descripción del producto', compute="_compute_product_description")

    def _compute_product_description(self):
        self.product_description = self.env['product.product'].search([('id', '=', self.product_id.id)]).description

    @api.model
    def _bom_find_domain(self, product_tmpl=None, product=None, picking_type=None, company_id=False, bom_type=False,
                         service=None, ):
        if product:
            if not product_tmpl:
                product_tmpl = product.product_tmpl_id
            domain = ['|', ('product_id', '=', product.id), '&', ('product_id', '=', False),
                      ('product_tmpl_id', '=', product_tmpl.id)]
        elif product_tmpl:
            domain = [('product_tmpl_id', '=', product_tmpl.id)]
        else:
            # neither product nor template, makes no sense to search
            raise UserError(_('You should provide either a product or a product template to search a BoM'))
        if picking_type:
            domain += ['|', ('picking_type_id', '=', picking_type.id), ('picking_type_id', '=', False)]
        if company_id or self.env.context.get('company_id'):
            domain = domain + ['|', ('company_id', '=', False),
                               ('company_id', '=', company_id or self.env.context.get('company_id'))]
        if bom_type:
            domain += [('type', '=', bom_type)]
        # order to prioritize bom with product_id over the one without
        return domain

    @api.model
    def _bom_find(self, product_tmpl=None, product=None, picking_type=None, company_id=False, bom_type=False,
                  service=None):
        """ Finds BoM for particular product, picking, company  and service order"""
        if product and product.type == 'service' or product_tmpl and product_tmpl.type == 'service':
            return self.env['mrp.bom']
        domain = self._bom_find_domain(product_tmpl=product_tmpl, product=product, picking_type=picking_type,
                                       company_id=company_id, bom_type=bom_type, service=service)
        if domain is False:
            return self.env['mrp.bom']
        return self.search(domain, order='sequence, product_id', limit=1)


class MRPBomLine(models.Model):
    """ BOM Lines Inherit"""
    _inherit = 'mrp.bom.line'

    child_bom_id = fields.Many2one(
        'mrp.bom', 'Sub BoM')
    item_num = fields.Float('# de componente')
    material = fields.Text('Material')
    diameter = fields.Float('Diámetro')
    length = fields.Float('Longitud')
    weight = fields.Float('Peso')
    component_type = fields.Selection(string="Perfil",
                                      selection=[('cylinder', 'Barra redonda'), ('hex_prism', 'Barra hexagonal'),
                                                 ('casting', 'Fundición'), ('manuf', 'Pieza'),
                                                 ('purchase', 'Comercial')])


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    product_description = fields.Html('Descripción del producto', compute="_compute_product_description")

    def _compute_product_description(self):
        self.product_description = self.env['product.product'].search([('id', '=', self.product_id.id)]).description

    def _get_move_raw_values(self, product_id, product_uom_qty, product_uom, operation_id=False, bom_line=False):
        source_location = self.location_src_id
        data = {
            'sequence': bom_line.sequence if bom_line else 10,
            'name': self.name,
            'date': self.date_planned_start,
            'date_deadline': self.date_planned_start,
            'bom_line_id': bom_line.id if bom_line else False,
            'picking_type_id': self.picking_type_id.id,
            'product_id': product_id.id,
            # custom fields (bom_extended)
            'material': bom_line.material,
            'diameter': bom_line.diameter,
            'length': bom_line.length,
            'weight': bom_line.weight,
            # 'component_type': bom_line.component_type,
            #
            'product_uom_qty': product_uom_qty,
            'product_uom': product_uom.id,
            'location_id': source_location.id,
            'location_dest_id': self.product_id.with_company(self.company_id).property_stock_production.id,
            'raw_material_production_id': self.id,
            'company_id': self.company_id.id,
            'operation_id': operation_id,
            'price_unit': product_id.standard_price,
            'procure_method': 'make_to_stock',
            'origin': self.name,
            'state': 'draft',
            'warehouse_id': source_location.get_warehouse().id,
            'group_id': self.procurement_group_id.id,
            'propagate_cancel': self.propagate_cancel,
        }
        return data


class MrpProduction(models.Model):
    """ Manufacturing Orders Inherit """
    _inherit = 'stock.move'

    item_num = fields.Float('# de componente')
    material = fields.Float('Material')
    diameter = fields.Float('Diámetro')
    length = fields.Float('Longitud')
    weight = fields.Float('Peso')
    component_type = fields.Selection(string="Perfil",
                                      selection=[('cylinder', 'Barra redonda'), ('hex_prism', 'Barra hexagonal'),
                                                 ('casting', 'Fundición'), ('manuf', 'Pieza'),
                                                 ('purchase', 'Comercial')])
