import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-sale",
    description="Meta package for open-synergy-ssi-sale Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_sale',
        'odoo14-addon-ssi_sale_order_state_change_constrain',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
