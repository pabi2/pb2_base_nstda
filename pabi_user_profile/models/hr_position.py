# -*- coding: utf-8 -*-
from openerp import fields, models


class hr_position(models.Model):
    _name = 'hr.position'
    _description = "Master employee's Position"

    name = fields.Char(
        string='Name',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )