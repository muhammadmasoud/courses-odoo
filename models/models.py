# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courses(models.Model):
    _name = "courses"
    _description = "Courses"
    name = fields.Char(string="Course Name", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    cost = fields.Float(string="Cost", required=True)
    teacher_id = fields.Many2one(
        "res.partner",
        string="Teacher",
        required=True,
    )
    enrollment_id = fields.One2many('enrollment', 'course_id', string="Enrollment")

    reason = fields.Char(
        string="Reason")

    number_of_enrollments = fields.Integer(
        string="Number of Enrollments",
        compute="_compute_number_of_enrollments",
    )


    state = fields.Selection(
        [
            ('open', 'Open'),
            ('closed', 'Closed'),
        ]
    )
    @api.depends('enrollment_id')
    def _compute_number_of_enrollments(self):
        for course in self:
            course.number_of_enrollments = len(course.enrollment_id)

    def open_course(self):
        for course in self:
            course.state = 'open'
   
    def close_course(self):
        return {
            'name': 'Close Reason',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'course_close_wizard',
            'view_id': self.env.ref("courses.close_reason_view_form").id,
            'context': {'default_course_id': self.id},
            'target': 'new',
        }