# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2015 Camptocamp SA
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

from openerp import models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def generate_shipping_labels(self, package_ids=None):
        _super = super(StockPicking, self)
        labels = _super.generate_shipping_labels(package_ids=package_ids)
        zpl_printer = self.env.user.zpl_label_printer_id
        if zpl_printer:
            for label in labels:
                content = label['file']
                file_type = label['file_type']
                if file_type == 'zpl2':
                    zpl_printer.print_raw(content)
        return labels

    label_types = ('colissimo', 'so_colissimo', 'postlogistics')

    @api.multi
    def do_transfer(self):
        result = super(StockPicking, self).do_transfer()
        for picking in self:
            if picking.carrier_id.type in self.label_types:
                labels = self.env['shipping.label'].search(
                    [('res_id', '=', picking.id),
                     ('res_model', '=', 'stock.picking'),
                     ]
                )
                if not labels:
                    self.generate_labels()
        return result
