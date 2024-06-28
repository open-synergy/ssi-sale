from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _compute_invoice_status(self):
        super()._compute_invoice_status()
        for line in self.filtered(lambda l: l.state == "done"):
            line.invoice_status = "invoiced"

    @api.depends(
        "product_type",
        "product_uom_qty",
        "qty_delivered",
        "state",
        "move_ids",
        "product_uom",
    )
    def _compute_qty_to_deliver(self):
        """Compute the visibility of the inventory widget."""
        for line in self:
            line.qty_to_deliver = line.product_uom_qty - line.qty_delivered
            if (
                line.state in ("confirm", "draft", "sent", "sale")
                and line.product_type == "product"
                and line.product_uom
                and line.qty_to_deliver > 0
            ):
                if line.state == "sale" and not line.move_ids:
                    line.display_qty_widget = False
                else:
                    line.display_qty_widget = True
            else:
                line.display_qty_widget = False
