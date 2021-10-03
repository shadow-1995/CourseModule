# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Partners(models.Model):
    _inherit = 'res.partner'
    
    instructor = fields.Boolean("Instructor")
    instructor_lesson_count = fields.Integer("Instructor Lesson Count", compute="_compute_instructor_lesson_count")
    attendee_lesson_count = fields.Integer("Attendee Lesson Count", compute="_compute_attendee_lesson_count")

    def _compute_instructor_lesson_count(self):
        lesson_model = self.env['koko_networks.lessons'].sudo()
        for record in self:
            record.instructor_lesson_count = lesson_model.search_count([('courses.instructor','=',record.id)])
    
    def _compute_attendee_lesson_count(self):
        lesson_model = self.env['koko_networks.lessons'].sudo()
        for record in self:
            record.attendee_lesson_count = lesson_model.search_count([('attendees.partner_id','=',record.id)])