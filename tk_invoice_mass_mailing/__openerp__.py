# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Kévin Goris
#    Copyright (c) 2015 Taktik S.A. (http://www.taktik.be)
#    All Rights Reserved
#
#    WARNING: This program as such is intended to be used by professional
#    programmers who take the whole responsibility of assessing all potential
#    consequences resulting from its eventual inadequacies and bugs.
#    End users who are looking for a ready-to-use solution with commercial
#    guarantees and support are strongly advised to contact a Free Software
#    Service Company.
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
{
    "name": "Taktik Invoice Mass Mailing",
    "version": "1.0",
    "author": "Taktik S.A.",
    "category": "Taktik",
    "website": "http://www.taktik.be",
    "depends": [
        'account',
        'base'
    ],
    "description": """
Taktik Base Addons
===============
This module is a one click install to load all libraries developed for Taktik Project by Taktik S.A.
        """,
    "data": [
        "wizard/tk_invoice_emailer_wizard.xml",
        "view/tk_account_invoice.xml",
    ],
    "demo": [],
    "test": [],
    "active": False,
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
