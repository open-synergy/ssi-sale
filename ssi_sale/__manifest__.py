# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Sale",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "sale",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/sale_order_type.xml",
        "views/sale_order_views.xml",
        "views/sale_order_type_views.xml",
    ],
    "demo": [],
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
}
