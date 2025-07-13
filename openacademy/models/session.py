# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import timedelta




# Add this class to your models.py
class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy session"  # Fixed description

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    duration = fields.Float(string="Duration")
    start_date = fields.Date(default=fields.Date.today)
    seats = fields.Integer(string="Seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', string="Course", required=True, ondelete='cascade')
    attendee_id = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken Seats", compute='_compute_taken_seats')
    active = fields.Boolean(default=True)
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer(compute='_compute_attendees_count', store=True, string="Number of attendees")

    @api.depends('attendee_id')
    def _compute_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_id)

    @api.depends('seats', 'attendee_id')
    def _compute_taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_id) / r.seats

    @api.constrains('attendee_id')
    def _onchange_attendee_warning(self):
        if len(self.attendee_id) > self.seats:
            raise exceptions.ValidationError(
                f'You have {len(self.attendee_id)} attendees but only {self.seats} seats available.')

    @api.constrains('instructor_id', 'attendee_id')
    def _check_attendee_id(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_id:
                raise exceptions.ValidationError(" a session instructor can only be used on instructors")





    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration
