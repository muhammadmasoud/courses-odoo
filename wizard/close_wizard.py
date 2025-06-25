# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CourseCloseWizard(models.TransientModel):
    _name = 'course_close_wizard'
    _description = 'Course Close Wizard'

    name = fields.Char(string='Reason', required=True)
    course_id = fields.Many2one('courses', string='Course', required=True)

    def confirm_reason(self):
        if self.course_id:
            self.course_id.write({
                'state': 'closed',
                'reason': self.name,
            })