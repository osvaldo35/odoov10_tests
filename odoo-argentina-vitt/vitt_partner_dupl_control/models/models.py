# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning

class ResCompany(models.Model):
    _inherit = "res.company"

    main_id_category_ids = fields.Many2many('res.partner.id_category',string="Categorias")


class AccountConfigSettings(models.TransientModel):
    _inherit = 'account.config.settings'

    main_id_category_ids = fields.Many2many(related='company_id.main_id_category_ids')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def write(self,vals):
        for rec in self:
            if rec.customer:
                control_ids = rec.company_id.main_id_category_ids.ids
                number = rec.main_id_number
                if not number and 'main_id_number' in vals.keys():
                    number = vals['main_id_number']
                if rec.main_id_category_id.id in control_ids and number:
                    if self.env['res.partner.id_number'].search([('name', '=', number),('category_id', '=', rec.main_id_category_id.id)]):
                        raise ValidationError(_("NO puede haber 2 contactos con el mismo %s") % (rec.main_id_category_id.name))

        return super(ResPartner, self).write(vals)
