from odoo import models, fields, api
from datetime import date


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'TODO Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one('todo.category', string='Category')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('todo', 'To Do'),
        ('done', 'Done'),
    ], string='Status', default='draft')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
    ], string='Priority', default='1')
    due_date = fields.Date(string='Due Date')
    user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
    is_overdue = fields.Boolean(string='Overdue', compute='_compute_is_overdue')
    priority_label = fields.Char(string='Priority Label', compute='_compute_priority_label')

    @api.depends('due_date', 'state')
    def _compute_is_overdue(self):
        today = date.today()
        for task in self:
            task.is_overdue = (task.due_date and task.due_date < today and task.state != 'done')

    @api.depends('priority')
    def _compute_priority_label(self):
        priority_map = {'0': 'Low', '1': 'Normal', '2': 'High'}
        for task in self:
            task.priority_label = priority_map.get(task.priority, 'Normal')

    @api.onchange('category_id')
    def _onchange_category_id(self):
        if self.category_id and not self.name:
            self.name = f"New task for {self.category_id.name}"

    @api.onchange('state')
    def _onchange_state(self):
        if not self.user_id:
            self.user_id = self.env.user

    def action_start(self):
        self.state = 'todo'
        if not self.user_id:
            self.user_id = self.env.user

    def action_done(self):
        self.state = 'done'

    def action_reset(self):
        self.state = 'draft'
        self.user_id = False
