# Simple TODO List Module

A basic TODO list application for Odoo 17 with task management and categories.

## Features

- **Task Management**: Create, edit, and track tasks
- **Categories**: Organize tasks into categories
- **Priority System**: Set task priorities (Low, Normal, High)  
- **Due Dates**: Track task deadlines with overdue indicators
- **User Assignment**: Assign tasks to users
- **Mass Updates**: Update multiple tasks at once
- **Reports**: Generate PDF reports for tasks

## Models

### Tasks (`todo.task`)
- Name, description, category
- Priority levels and due dates
- Status workflow: Draft → To Do → Done
- User assignment and overdue tracking

### Categories (`todo.category`) 
- Name and description
- Automatic task counting
- Links to related tasks

## Views

- **Kanban Board**: Visual task management by status
- **List View**: Table view with sorting and filtering
- **Form View**: Detailed task editing

## Security

- **TODO User**: Can manage own tasks
- **TODO Manager**: Can manage all tasks and categories

## Installation

1. Copy module to Odoo addons directory
2. Update app list
3. Install "Simple TODO List" module

## Usage

1. Go to **TODO List** menu
2. Create categories first
3. Add tasks and assign to categories
4. Use kanban view to drag tasks between states
5. Generate reports from task form view

## File Structure

```
todo_module/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── task.py
│   └── category.py
├── views/
│   ├── task_views.xml
│   ├── category_views.xml
│   └── menu_views.xml
├── wizard/
│   ├── todo_wizard.py
│   └── todo_wizard_views.xml
├── security/
│   ├── security.xml
│   └── ir.model.access.csv
└── report/
    └── todo_report.xml
```