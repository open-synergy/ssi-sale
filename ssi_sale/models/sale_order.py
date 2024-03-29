# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = [
        "sale.order",
        "mixin.policy",
        "mixin.many2one_configurator",
        "mixin.sequence",
    ]
    _document_number_field = "name"

    def _compute_policy(self):
        _super = super(SaleOrder, self)
        _super._compute_policy()

    @api.depends(
        "type_id",
    )
    def _compute_allowed_pricelist_ids(self):
        for record in self:
            result = False
            if record.type_id:
                result = record._m2o_configurator_get_filter(
                    object_name="product.pricelist",
                    method_selection=record.type_id.pricelist_selection_method,
                    manual_recordset=record.type_id.pricelist_ids,
                    domain=record.type_id.pricelist_domain,
                    python_code=record.type_id.pricelist_python_code,
                )
            record.allowed_pricelist_ids = result

    allowed_pricelist_ids = fields.Many2many(
        comodel_name="product.pricelist",
        string="Allowed Pricelists",
        compute="_compute_allowed_pricelist_ids",
        store=False,
        compute_sudo=True,
    )
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
        compute_sudo=True,
    )
    void_ok = fields.Boolean(
        string="Can Void Transaction",
        compute="_compute_policy",
        compute_sudo=True,
    )
    invoice_ok = fields.Boolean(
        string="Can Create Invoice",
        compute="_compute_policy",
        compute_sudo=True,
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
        compute_sudo=True,
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
    manual_number_ok = fields.Boolean(
        string="Can Input Manual Document Number",
        compute="_compute_policy",
        compute_sudo=True,
    )

    def action_confirm(self):
        _super = super(SaleOrder, self)
        for record in self:
            record._create_sequence()
        res = _super.action_confirm()
        return res

    @api.model
    def default_get(self, fields):
        _super = super(SaleOrder, self)
        res = _super.default_get(fields)

        res["name"] = "/"

        return res

    @api.model
    def create(self, vals):
        vals["name"] = "/"
        _super = super(SaleOrder, self)
        res = _super.create(vals)
        return res

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
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.onchange(
        "type_id",
        "partner_id",
    )
    def onchange_pricelist_id(self):
        if self.user_has_groups("product.group_product_pricelist"):
            self.pricelist_id = False
            if self.type_id and self.partner_id:
                if (
                    self.partner_id.property_product_pricelist.id
                    in self.allowed_pricelist_ids.ids
                ):
                    self.pricelist_id = self.partner_id.property_product_pricelist.id

    def name_get(self):
        result = []
        for record in self:
            if getattr(record, self._document_number_field) == "/":
                name = "*" + str(record.id)
            else:
                name = record.name
            result.append((record.id, name))
        return result
