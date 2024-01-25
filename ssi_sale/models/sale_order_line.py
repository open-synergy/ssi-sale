from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _compute_invoice_status(self):
        super()._compute_invoice_status()
        for line in self.filtered(lambda l: l.state == 'done'):
            line.invoice_status = 'invoiced'
