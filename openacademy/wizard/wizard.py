from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"


    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self.env.context.get('active_ids'))

    session_ids = fields.Many2many('openacademy.session',
                                  string="Sessions",
                                  default=_default_sessions,
                                  required=True)

    def subscribe_button(self):
        for session in self.session_ids:
            session.attendee_id |= self.attendee_ids
        return {'type': 'ir.actions.act_window_close'}

    