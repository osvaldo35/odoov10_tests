# coding=utf-8
{
    'name': 'MercadoPago Payment Acquirer',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: MercadoPago Implementation',
    'version': '1.0',
    'description': """MercadoPago Payment Acquirer""",
    'depends': ['payment', 'website', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_views.xml',
        'views/payment_mecradopago_templates.xml',
        'views/res_partner_modifications.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
}
