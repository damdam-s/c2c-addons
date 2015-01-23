# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2014 Camptocamp SA
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

{'name': 'Delivery Labels Direct Print',
 'version': '1.0',
 'author': 'Camptocamp',
 'maintainer': 'Camptocamp',
 'license': 'AGPL-3',
 'category': 'Specific',
 'depends': ['stock',
             'base_delivery_carrier_label',
             'base_report_to_printer',
             'delivery_carrier_label_postlogistics',
             'delivery_carrier_label_colissimo',
             ],
 'website': 'http://www.camptocamp.com',
 'data': ['view/res_users_view.xml',
          ],
 'test': [],
 'qweb': [],
 'installable': True,
 'auto_install': False,
 }
