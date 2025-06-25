from odoo import models, fields, api

class Enrollment(models.Model):
    _name = 'enrollment'
    _description = 'Enrollment'

    name = fields.Char(string="Name", required=True)
    student_id = fields.Many2one('student', string='Student', required=True)
    course_id = fields.Many2one('courses', string='Course', required=True)
    date = fields.Date(string='Enrollment Date', required=True)
    cost = fields.Float(string='Cost', related='course_id.cost', store=True)
    name = fields.Char()

    @api.model
    def create(self, vals):

        result = super(Enrollment, self).create(vals)
        result.name = f"course {result.course_id.name} enrolled by {result.student_id.name}"
        return result
    
    def write(self, vals):

        result = super(Enrollment, self).write(vals)

        for rec in self:
            if 'course_id' in vals or 'student_id' in vals:
                rec.name = f"Course {rec.course_id.name} enrolled by {rec.student_id.name}"


        return result