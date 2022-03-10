# -*- coding: utf-8 -*-
from openerp import fields, models, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends('farming_method', 'other_information', 'label_ids')
    @api.multi
    def _compute_pricetag_coopinfos(self):
        for pt in self:
            tmp = ''
            if pt.other_information:
                tmp = pt.other_information
            if pt.farming_method:
                tmp = pt.farming_method + \
                    (' - ' + tmp if tmp else '')
            lbls = ''
            for lbl in pt.label_ids:
                lbls = lbl.name + (', ' + lbls if lbls else '')
            tmp = lbls + (' - ' + tmp if tmp else '')
            pt.pricetag_coopinfos = tmp

    pricetag_coopinfos = fields.Char(
        compute=_compute_pricetag_coopinfos, string='Coop custom fields')
