# OpenAcademy

A comprehensive course and session management system built for Odoo.

## Overview

OpenAcademy is an educational management module that allows you to create and manage courses, schedule training sessions, and track student enrollment and attendance.

## Features

### Course Management
- Create and manage educational courses
- Assign responsible instructors
- Add detailed course descriptions
- Unique course naming constraints

### Session Management
- Schedule training sessions linked to courses
- Set session capacity and track attendance
- Automatic calculation of occupancy rates
- Calendar view for session scheduling
- Multiple view modes (Tree, Form, Calendar, Graph, Pivot, Kanban)

### Attendee Management
- Register attendees to sessions
- Bulk attendee registration wizard
- Track attendance and capacity
- Prevent instructor from being their own attendee

### Reporting
- Generate comprehensive session reports
- Visual analytics with graphs and pivot tables
- Session occupancy tracking
- Attendance statistics

## Installation

1. Place the `openacademy` folder in your Odoo addons directory
2. Update the addons list in Odoo
3. Install the "OpenAcademy" module from the Apps menu

## Usage

### Creating Courses
1. Navigate to **Open Academy > Courses**
2. Click "Create" to add a new course
3. Fill in course details (title, description, responsible instructor)
4. Save the course

### Scheduling Sessions
1. Go to **Open Academy > Sessions**
2. Create a new session
3. Select the course, instructor, and set capacity
4. Choose start date and duration
5. Save the session

### Managing Attendees
1. Open a session record
2. Use the "Add Attendees" wizard for bulk registration
3. Or manually add attendees in the session form

## Module Structure

```
openacademy/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── course.py          # Course model
│   └── session.py         # Session model
├── views/
│   ├── course.xml         # Course views
│   ├── session.xml        # Session views
│   └── menu_views.xml     # Menu structure
├── wizard/
│   ├── __init__.py
│   ├── wizard.py          # Bulk attendee registration
│   └── wizard.xml         # Wizard views
├── security/
│   ├── security.xml       # Access groups and rules
│   └── ir.model.access.csv # Model access permissions
└── reports/
    └── session_report.xml # Session report template
```

## Models

### Course (`openacademy.course`)
- **name**: Course title (required, unique)
- **description**: Detailed course description
- **responsible_id**: Assigned instructor
- **sessions_id**: Related sessions

### Session (`openacademy.session`)
- **name**: Session title
- **course_id**: Linked course
- **instructor_id**: Session instructor
- **start_date/end_date**: Session dates
- **duration**: Session duration in days
- **seats**: Available capacity
- **attendee_id**: Registered attendees
- **taken_seats**: Calculated occupancy percentage

### Wizard (`openacademy.wizard`)
- **session_ids**: Selected sessions
- **attendee_ids**: Attendees to register

## Security

### User Groups
- **OpenAcademy / Manager**: Full access to all features
- **OpenAcademy / User**: Limited access, can only modify courses they're responsible for

### Access Rights
- Managers have full CRUD access
- Users have read access to courses and sessions
- Only course responsible users can modify their courses

## Views Available

### Course Views
- **Tree View**: List of all courses
- **Form View**: Course details and management
- **Search View**: Filter and group courses

### Session Views
- **Tree View**: Session list with capacity indicators
- **Form View**: Detailed session management
- **Calendar View**: Schedule visualization
- **Graph View**: Attendance analytics
- **Pivot View**: Data analysis
- **Kanban View**: Card-based session overview

## Reports

The module includes a comprehensive session report that displays:
- Session details (title, course, instructor)
- Dates and duration
- Capacity and occupancy statistics
- Session descriptions

## Constraints and Validations

- Course names must be unique
- Session capacity cannot be exceeded
- Instructors cannot be attendees of their own sessions
- Automatic end date calculation based on start date and duration

## Dependencies

- **base**: Core Odoo functionality

## Author

Youssef Abdalnaby

## Version

1.0.0

## License

This module is designed for educational purposes and internal use.