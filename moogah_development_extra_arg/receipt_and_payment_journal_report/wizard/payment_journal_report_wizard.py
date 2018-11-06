# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import models, fields
import calendar


class PaymentJournalReportWizard(models.TransientModel):
    _name = 'payment.journal.report.wizard'
    _description = 'Wizard that show the payment journal report'

    start_date = fields.Date('Start Date', default=lambda s: datetime.today().replace(day=1), required=True)
    end_date = fields.Date('End Date', default=lambda s: datetime.today().replace(
                                        day=calendar.monthrange(datetime.today().year, datetime.today().month)[1]),
                           required=True)
    payment_no = fields.Char('Payment No')
    journal_ids = fields.Many2many('account.journal', string='Journals',
                                   domain=[('type','in',['bank','cash']),
                                           ('outbound_payment_method_ids.code','in',
                                            ['manual','delivered_third_check','issue_check','withholding']),
                                           ('outbound_payment_method_ids.payment_type','=','outbound')])
    partner_id = fields.Many2one('res.partner', 'Supplier', domain=[('supplier','=', True)])
    analytic_tag_id = fields.Many2one('account.analytic.tag', string='Analytic Tag (From Supplier)')
    reference = fields.Char('Reference')
    draft = fields.Boolean('Draft')
    confirmed = fields.Boolean('Confirmed', default=True)
    posted = fields.Boolean('Posted', default=True)
    detail_level = fields.Selection([('per_supplier', 'Per Supplier'),('overview', 'Overview')],
                                    'Detail Level', required=True, default='overview')

