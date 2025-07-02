from odoo import models, fields, api
from datetime import date


class TodoCategory(models.Model):
    _name = 'todo.category'
    _description = 'TODO Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    task_count = fields.Integer(string='Task Count', compute='_compute_task_count')
    active_task_count = fields.Integer(string='Active Tasks', compute='_compute_task_count')

    @api.depends('task_ids', 'task_ids.state')
    def _compute_task_count(self):
        for category in self:
            category.task_count = len(category.task_ids)
            category.active_task_count = len(category.task_ids.filtered(lambda t: t.state != 'done'))

    task_ids = fields.One2many('todo.task', 'category_id', string='Tasks')
