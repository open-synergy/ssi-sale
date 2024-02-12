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
    capture_ok = fields.Boolean(
        string="Can Capture Transaction",
        compute="_compute_policy",
        default=False,
    )
    void_ok = fields.Boolean(
        string="Can Void Transaction",
        compute="_compute_policy",
        default=False,
    )
    invoice_ok = fields.Boolean(
        string="Can Create Invoice",
        compute="_compute_policy",
        default=False,
    )
    email_ok = fields.Boolean(
        string="Can Send by Email",
        compute="_compute_policy",
        compute_sudo=True,
    )
    proforma_ok = fields.Boolean(
        string="Can Send PRO-FORMA Invoice",
        compute="_compute_policy",
        compute_sudo=True,
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
    done_ok = fields.Boolean(
        string="Can Lock",
        compute="_compute_policy",
        compute_sudo=True,
    )
    unlock_ok = fields.Boolean(
        string="Can Unlock",
        compute="_compute_policy",
        compute_sudo=True,
    )

    @api.model
    def _get_policy_field(self):
        res = super(SaleOrder, self)._get_policy_field()
        policy_field = [
            "capture_ok",
            "void_ok",
            "invoice_ok",
            "email_ok",
            "proforma_ok",
            "confirm_ok",
            "cancel_ok",
            "draft_ok",
            "done_ok",
            "unlock_ok",
        ]
        res += policy_field
        return res
