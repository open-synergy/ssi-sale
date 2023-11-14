# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import logging


def migrate(cr, version):
    if not version:
        return
    logger = logging.getLogger(__name__)
    logger.info("Updating sale_order...")
    cr.execute(
        """
    UPDATE
        sale_order so
    SET
        type_id = t.id
    FROM
        sale_order_type t
    WHERE
        t.code = 'T0001'
        AND so.type_id IS NULL;
    """
    )
    logger.info("Successfully updated sale_order tables")
