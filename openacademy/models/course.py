from odoo import models, fields, api, exceptions
from datetime import timedelta


class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Course"  # Fixed description

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    alaa = fields.Text(string="Alaa Field")  # Added proper string attribute
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="Responsible", index=True)
    sessions_id = fields.One2many('openacademy.session', 'course_id', string="Sessions", ondelete='cascade', index=True)
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Course name must be unique!'),
    ]