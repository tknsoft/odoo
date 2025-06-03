# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2025-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Gayathri V (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models


class ResPartner(models.Model):
    """
       This class inherits the 'res.partner' model to represent patients and
       physicians in the system.
    """
    _inherit = 'res.partner'
    _description = "Patient"

    is_patient = fields.Boolean(string='Is Patient',
                                help="Patient Identification")
    is_physician = fields.Boolean(string='Is Physician',
                                  help="Physician Identification")
    speciality_id = fields.Many2one('physician.speciality',
                                 string='Speciality',
                                 help="Speciality of  the physician")
    hospital_id = fields.Many2one('res.partner', string='Hospital',
                               help="Name of the hospital")
