# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api, _
from lxml import etree


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = [
        "sale.order",
        "mixin.policy",
    ]

    def _compute_policy(self):
        _super = super(SaleOrder, self)
        _super._compute_policy()

    type_id = fields.Many2one(
        comodel_name="sale_order_type",
        string="Type",
        required=True,
        readonly=True,
        states={
            "draft": [("readonly", False)],
        },
    )
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        default=False,
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
        compute_sudo=True,
    )
    draft_ok = fields.Boolean(
        string="Can Set to Quotation",
        compute="_compute_policy",
        compute_sudo=True,
    )

    @api.model
    def _get_policy_field(self):
        res = super(SaleOrder, self)._get_policy_field()
        policy_field = [
            "confirm_ok",
            "cancel_ok",
            "draft_ok",
        ]
        res += policy_field
        return res
