from odoo import fields, models


class MrpRoutingWorkcenter(models.Model):
    """ BOM Operations Inherit"""
    _inherit = 'mrp.routing.workcenter'

    time_cycle_hours = fields.Float(
        'Duración (Horas)', default=1,
        help="Time in hours:"
             "- In manual mode, time used"
             "- In automatic mode, supposed first time when there aren't any work orders yet")

    time_cycle_manual = fields.Float(
        'Manual Duration', default=60,
        help="Time in minutes:"
             "- In manual mode, time used"
             "- In automatic mode, supposed first time when there aren't any work orders yet",
        compute="_convert_time_cycle")

    def _convert_time_cycle(self):
        for operation in self:
            time_cycle_manual = operation.time_cycle_hours * 60
            operation.time_cycle_manual = time_cycle_manual
