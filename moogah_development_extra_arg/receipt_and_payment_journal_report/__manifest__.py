# -*- coding: utf-8 -*-

{
    'name': 'Receipt and Payment Journal Report',
    'version': '10.0.1.0',
    'category': 'Accounting',
    'summary': '',
    'description': """
    
    Receipt and Payment Journal Report
""",
    'author': 'Moogah',
    'website': 'www.moogah.com',
    'images': [],
    'depends': ['account_payment_group',
                'detailed_general_ledger_report',
                'vitt_analytic_tags_account'],
    'data': [
        'views/report_financial.xml',
        'views/payment_journal_report_view.xml',
        'wizard/payment_journal_report_wizard_views.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

