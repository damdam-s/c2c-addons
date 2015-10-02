# -*- coding: utf-8 -*-
##############################################################################
#
#    Author Vincent Renaville. Copyright 2013 Camptocamp SA
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
    "name": "L10n_ch accounting profile",
    "description": """Install all modules required for accounting in Switzerland
    """,
    "version": "1.0",
    "author": "Camptocamp",
    "category": "Accounting & Finance",
    "website": "http://www.camptocamp.com",
    "depends": [
        'common_accounting_profile',
        'l10n_ch',
        'l10n_ch_bank',
        'l10n_ch_base_bank',
        'l10n_ch_dta',
        'l10n_ch_payment_slip',
        'l10n_ch_zip',
        'l10n_multilang',
        'payment_term_rounding',
        'l10n_ch_dta_base_transaction_id',
        'l10n_ch_payment_slip_base_transaction_id',
        'l10n_ch_payment_slip_account_statement_base_completion'
        ],
    "data": [],
    "active": False,
    "installable": True
}
