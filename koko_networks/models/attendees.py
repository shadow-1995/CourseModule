# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Attendees(models.Model):
    _name = 'koko_networks.attendees'
    _description = "Attendees"

    name = fields.Char("Name", required=True)
    partner_id = fields.Many2one("res.partner", "Attendee", required=True)
    courses = fields.Many2many("koko_networks.courses", relation="attendees_course_rel", string="Attendees", required=True)
    lessons = fields.Many2many("koko_networks.lessons", relation="attendees_lesson_rel",string="Lessons", required=True)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for record in self:
            if not record.name and record.partner_id:
                record.name = record.partner_id.name
    
    @api.constrains('courses')
    def _constraint_total_attendees(self):
        for record in self:
            for course in record.courses:
                capacity = course.room and course.room.capacity or 0
                total_attendees = len(course.attendees)
                if total_attendees > capacity:
                    raise ValidationError(_("Total Attendees for course '%s' cannot exceed the room capacity of %s"%(course.name,capacity)))
        
    @api.constrains('courses','partner_id')
    def _constraint_instructor(self):
        for record in self:
            for course in record.courses:
                if record.partner_id.id == course.instructor.id:
                    raise ValidationError(_("Instructor of course '%s' cannot enroll."%(course.name)))
    
