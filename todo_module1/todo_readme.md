# Simple TODO List Module

A comprehensive TODO list management module for Odoo 17.0 with task organization and team collaboration features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Views](#views)
- [Security](#security)
- [Technical Details](#technical-details)
- [File Structure](#file-structure)

## Features

### Core Features
- **Task Management**: Create, edit, and track tasks
- **Category System**: Organize tasks into categories
- **Priority Levels**: Low, Normal, High priority settings
- **Due Date Tracking**: Set deadlines with overdue detection
- **User Assignment**: Assign tasks to specific users
- **Status Workflow**: Draft → To Do → Done

### Advanced Features
- **Multiple Views**: Kanban, Tree, Calendar, Form views
- **Mass Operations**: Bulk update multiple tasks
- **PDF Reports**: Generate task reports
- **Security Groups**: User and Manager roles
- **Overdue Detection**: Automatic overdue task highlighting

## Installation

### Prerequisites
- Odoo 17.0
- Base module (included with Odoo)

### Steps
1. Copy `todo_module1` folder to your Odoo addons directory
2. Restart Odoo server
3. Update apps list: **Apps → Update Apps List**
4. Search for "Simple TODO List"
5. Click **Install**

## Configuration

### Security Groups
The module creates two security groups:
- **TODO User**: Basic task management
- **TODO Manager**: Full access to all tasks and categories

### Initial Setup
1. Assign users to appropriate security groups
2. Create initial categories for task organization

## Usage

### Getting Started
1. Navigate to **TODO List** menu
2. Create categories first: **TODO List → Categories**
3. Start adding tasks: **TODO List → Tasks**

### Task Management

#### Creating Tasks
1. Go to **TODO List → Tasks**
2. Click **Create**
3. Fill required fields:
   - **Task Name** (required)
   - **Category** (optional)
   - **Priority** (Low/Normal/High)
   - **Due Date**
   - **Description**
4. Click **Save**

#### Task Workflow
- **Draft**: Initial state
- **To Do**: Click "Start" button
- **Done**: Click "Done" button
- **Reset**: Return to Draft (from Done state)

#### Mass Operations
1. Select multiple tasks in tree view
2. Go to **Action → Mass Update Tasks**
3. Choose operation:
   - Set Priority
   - Set Category
   - Set State
4. Click **Apply**

### Category Management

#### Creating Categories
1. Go to **TODO List → Categories**
2. Click **Create**
3. Enter:
   - **Category Name** (required)
   - **Description** (optional)
4. Click **Save**

#### Category Statistics
- **Task Count**: Total tasks in category
- **Active Task Count**: Non-completed tasks

## Views

### Kanban View
- **Purpose**: Visual task management
- **Features**: Drag-and-drop between states
- **Usage**: Default view for quick task overview

### Tree View
- **Purpose**: Detailed task listing
- **Features**: Sortable columns, bulk selection
- **Visual Indicators**:
  - Red: Overdue tasks
  - Green: Completed tasks

### Calendar View
- **Purpose**: Deadline management
- **Features**: Monthly/weekly/daily views
- **Date Range**: From start_date to due_date

### Form View
- **Purpose**: Detailed task editing
- **Features**: All fields, status buttons
- **Actions**: Start, Done, Reset buttons

## Security

### User Permissions

#### TODO User
- **Tasks**: Create/Read/Write own tasks
- **Categories**: Read-only access
- **Restrictions**: Cannot delete tasks

#### TODO Manager
- **Tasks**: Full CRUD access to all tasks
- **Categories**: Full CRUD access
- **Users**: Can manage all user tasks

### Security Rules
- **User Level**: Users see only their assigned tasks
- **Manager Level**: Managers see all tasks
- **Category Access**: All users can read categories

## Technical Details

### Models

#### `todo.task`
**Fields:**
- `name`: Char (required) - Task name
- `description`: Text - Task description
- `category_id`: Many2one('todo.category') - Task category
- `state`: Selection - Task status (draft/todo/done)
- `priority`: Selection - Priority level (0/1/2)
- `due_date`: Date - Task deadline
- `user_id`: Many2one('res.users') - Assigned user
- `start_date`: Date - Task start date
- `is_overdue`: Boolean (computed) - Overdue status
- `priority_label`: Char (computed) - Priority display

**Methods:**
- `action_start()`: Move to 'todo' state
- `action_done()`: Move to 'done' state
- `action_reset()`: Reset to 'draft' state

#### `todo.category`
**Fields:**
- `name`: Char (required) - Category name
- `description`: Text - Category description
- `task_count`: Integer (computed) - Total tasks
- `active_task_count`: Integer (computed) - Active tasks
- `task_ids`: One2many('todo.task') - Related tasks

### Wizard Models

#### `todo.mass.update`
**Purpose**: Mass update selected tasks
**Fields:**
- `action_type`: Selection - Update type
- `priority`: Selection - New priority
- `category_id`: Many2one - New category
- `state`: Selection - New state
- `task_ids`: Many2many - Selected tasks

## File Structure

```
todo_module1/
├── __init__.py                 # Module initialization
├── __manifest__.py             # Module manifest
│
├── models/                     # Data models
│   ├── __init__.py
│   ├── category.py            # Category model
│   └── task.py                # Task model
│
├── views/                      # User interface
│   ├── category_views.xml     # Category views
│   ├── menu_views.xml         # Menu structure
│   └── task_views.xml         # Task views
│
├── wizard/                     # Wizard functionality
│   ├── __init__.py
│   ├── todo_wizard.py         # Mass update wizard
│   └── todo_wizard_views.xml  # Wizard views
│
├── security/                   # Security configuration
│   ├── security.xml           # Groups and rules
│   └── ir.model.access.csv    # Access rights
│
└── report/                     # Reports
    └── todo_report.xml        # PDF report template
```

## Dependencies

- **Odoo**: 17.0
- **Base Module**: Included with Odoo
- **Category**: Productivity

## Author

**Youssef Abdalnaby**

---

*Version: 17.0.1.0.0*