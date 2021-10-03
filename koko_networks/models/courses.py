# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Courses(models.Model):
    _name = 'koko_networks.courses'
    _description = "Courses"
    
    name = fields.Char("Name", required=True)
    instructor = fields.Many2one("res.partner", "Instructor", domain="[('instructor','=',True)]" ,required=True)
    room = fields.Many2one("koko_networks.rooms", required=True)
    attendees = fields.Many2many("koko_networks.attendees", relation="attendees_course_rel", string="Courses")
    lessons = fields.Many2many("koko_networks.lessons", relation="course_lesson_rel", string="Lessons")

    @api.constrains('attendees','room')
    def _constraint_total_attendees(self):
        for record in self:
            capacity = record.room and record.room.capacity or 0
            total_attendees = len(record.attendees)
            if total_attendees > capacity:
                raise ValidationError(_("Total Attendees cannot exceed the room capacity of %s"%(capacity)))
    
