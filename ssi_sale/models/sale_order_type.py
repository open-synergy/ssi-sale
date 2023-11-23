# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class SaleOrderType(models.Model):
    _name = "sale_order_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Sale Order Type"
    _field_name_string = "Sale Order Type"
