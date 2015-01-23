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
import cups
import logging
import os

from tempfile import mkstemp

from openerp import models, api, _
from openerp.exceptions import Warning
from openerp.tools.config import config

_logger = logging.getLogger(__name__)
CUPS_HOST = config.get('cups_host', 'localhost')
CUPS_PORT = int(config.get('cups_port', 631))  # config.get returns a string


class PrintingPrinter(models.Model):
    _inherit = 'printing.printer'

    @api.multi
    def print_raw(self, content):
        self.ensure_one()
        fd, file_name = mkstemp()
        try:
            os.write(fd, content)
        finally:
            os.close(fd)

        try:
            _logger.debug('Starting to connect to CUPS on %s:%s',
                          CUPS_HOST, CUPS_PORT)
            connection = cups.Connection(CUPS_HOST, CUPS_PORT)
            _logger.debug('Connection to CUPS successful')
        except:
            raise Warning(
                _("Failed to connect to the CUPS server on %s:%s. "
                  "Check that the CUPS server is running and that "
                  "you can reach it from the Odoo server.")
                % (CUPS_HOST, CUPS_PORT))

        _logger.debug('Sending job to CUPS printer %s on %s',
                      self.system_name, CUPS_HOST)
        connection.printFile(self.system_name,
                             file_name,
                             file_name,
                             options={'raw': 'True'})
        _logger.info("Printing job: '%s' on %s", file_name, CUPS_HOST)
        return True
