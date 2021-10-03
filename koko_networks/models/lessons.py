# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Lessons(models.Model):
    _name = 'koko_networks.lessons'
    _description = "Lessons"

    name = fields.Char("Name", required=True)
    room = fields.Many2one("koko_networks.rooms", "Room", required=True)
    courses = fields.Many2many("koko_networks.courses", relation="course_lesson_rel", string="Courses")
    attendees = fields.Many2many("koko_networks.attendees", relation="attendees_lesson_rel",string="Lessons")

    
