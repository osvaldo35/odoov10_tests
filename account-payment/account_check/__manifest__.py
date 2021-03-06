# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account Check Management',
    'version': '10.0.1.6.6',
    'category': 'Accounting',
    'summary': 'Accounting, Payment, Check, Third, Issue',
    'author': 'Bacgroup, OpenERP Team de Localizacion Argentina',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        # 'account',
        # for bank and cash menu and also for better usability
        'account_payment_fix',
    ],
    'data': [
        'data/account_payment_method_data.xml',
        # TODO delete or enable, we should create it on chart installation
        # if we create it from here accounts will be created, so we let
        # this work to chart installation
        # 'data/account_journal_data.xml',
        'views/account_payment_view.xml',
        'views/account_check_view.xml',
        'views/account_journal_dashboard_view.xml',
        'views/account_journal_view.xml',
        'views/account_checkbook_view.xml',
        #'views/res_company_view.xml',
        'views/res_config.xml',
        'views/account_chart_template_view.xml',
        'wizard/check_operation_wizard_views.xml',
        'wizard/change_check_wizard_views.xml',
        'security/ir.model.access.csv',
        'security/account_check_security.xml',
        'views/product_template.xml',
    ],
    'demo': [
        # 'data/demo_data.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
