from odoo import models, fields, api


class TodoMassUpdate(models.TransientModel):
    _name = 'todo.mass.update'
    _description = 'Mass Update Tasks'

    action_type = fields.Selection([
        ('set_priority', 'Set Priority'),
        ('set_category', 'Set Category'),
        ('set_state', 'Set State'),
    ], string='Action', required=True)

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
    ], string='Priority')

    category_id = fields.Many2one('todo.category', string='Category')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('todo', 'To Do'),
        ('done', 'Done'),
    ], string='State')

    task_ids = fields.Many2many('todo.task', string='Tasks')

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        active_ids = self.env.context.get('active_ids', [])
        if active_ids:
            defaults['task_ids'] = [(6, 0, active_ids)]
        return defaults

    def action_apply(self):
        values = {}
        if self.action_type == 'set_priority' and self.priority:
            values['priority'] = self.priority
        elif self.action_type == 'set_category' and self.category_id:
            values['category_id'] = self.category_id.id
        elif self.action_type == 'set_state' and self.state:
            values['state'] = self.state

        if values:
            self.task_ids.write(values)

        return {'type': 'ir.actions.act_window_close'}
