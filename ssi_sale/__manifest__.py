# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale",
    "version": "14.0.5.5.0",
    "category": "Sale",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "sale_management",
        "ssi_policy_mixin",
        "ssi_master_data_mixin",
        "ssi_sequence_mixin",
        "ssi_m2o_configurator_mixin",
        "ssi_multiple_approval_mixin",
        "sale_stock",
        "sale_order_price_recalculation",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "data/sale_order_type.xml",
        "data/approval_template_data.xml",
        "data/policy_template_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "views/sale_order_views.xml",
        "views/sale_order_type_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_template_views.xml",
        "views/crm_tag_views.xml",
        "views/product_attribute_views.xml",
        "views/mail_activity_type_views.xml",
        "views/crm_team_views.xml",
    ],
    "demo": [],
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
}
