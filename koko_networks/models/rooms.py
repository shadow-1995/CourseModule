# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Rooms(models.Model):
    _name = 'koko_networks.rooms'
    _description = 'Rooms'

    name = fields.Char("Name", required=True)
    capacity = fields.Integer("Capacity", required=True)

    