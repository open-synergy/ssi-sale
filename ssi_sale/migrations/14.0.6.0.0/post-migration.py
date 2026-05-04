# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging

_logger = logging.getLogger(__name__)

_POLICY_UPDATES = [
    (
        "sale_order_policy_template_detail_restart_approval",
        "result = False\nif document.approval_template_id:\n    result = True",
    ),
]


def migrate(cr, version):
    if not version:
        return
    _logger.info("Updating ssi_sale policy template additional_python_code...")
    for xml_name, new_code in _POLICY_UPDATES:
        cr.execute(
            """
            UPDATE policy_template_detail ptd
            SET additional_python_code = %s
            FROM ir_model_data imd
            WHERE imd.model = 'policy.template_detail'
              AND imd.module = 'ssi_sale'
              AND imd.name = %s
              AND ptd.id = imd.res_id
            """,
            (new_code, xml_name),
        )
        _logger.info(
            "Updated policy_template_detail '%s' (%s row(s))",
            xml_name,
            cr.rowcount,
        )
    _logger.info("Done updating ssi_sale policy template additional_python_code.")
