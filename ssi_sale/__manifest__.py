# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Sale",
    "version": "14.0.1.2.0",
    "category": "Sale",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "sale_management",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "data/sale_order_type.xml",
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
