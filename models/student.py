from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    name = fields.Char()
    code = fields.Char()
    birthdate = fields.Date()
    address = fields.Char()
