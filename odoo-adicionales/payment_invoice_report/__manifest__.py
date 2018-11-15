# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2017-Today Sitaram
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Payment Information In Invoice Report',
    'version': '0.1',
    'category': 'Accounting & Finance',
    'summary': 'This module used to show payment information in invoice report.',
    "license": "AGPL-3",
    'description': """
        This module used to show payment information in invoice report.
""",
    'author': 'Sitaram',
    'depends': ['base','account'],
    'data': [
             'views/inherit_invoice_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'live_test_url': 'https://youtu.be/EYamS25yrwU',
    "images":['static/description/banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
