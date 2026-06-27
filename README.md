# 🎫 Internal Employee Ticketing System

A role-based ticket management system built with Django that helps employees report issues, IT staff manage assigned tickets, and managers monitor ticket resolution across the organization.

---

## 🚀 Features

### 👨‍💼 Employee
- Create support tickets
- View submitted tickets
- Track ticket status
- Search and filter tickets

### 🖥️ IT Staff
- View assigned tickets
- Update ticket status
- Assign tickets to IT staff
- Resolve technical issues
- Prioritize work based on ticket urgency

### 📊 Manager
- Monitor all tickets
- Assign tickets to IT staff
- View ticket statistics
- Track team performance

### 🤖 Smart Priority Assignment
The system automatically assigns ticket priority by analyzing issue descriptions.

Priority Levels:
- 🔴 High
- 🟡 Medium
- 🟢 Low

Example:

| Description | Priority |
|------------|----------|
| Server Down | High |
| Performance Issue | Medium |
| Password Reset | Low |

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Backend Logic |
| Django 5 | Web Framework |
| MySQL | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| Tailwind | UI Components |
| Django Authentication | User Management |

---

## 📂 Project Structure

```text
Internal-Employee-Ticketing-System
│
├── authentication/
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   └── forms.py
│
├── dashboard/
│   ├── views.py
│   ├── urls.py
│   └── decorators.py
│
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## 🗄️ Database Design

### Custom User

| Field | Type |
|---------|---------|
| username | CharField |
| email | Unique Email |
| role | Manager / IT Staff / Employee |
| phone | CharField |
| address | TextField |

### Ticket

| Field | Type |
|---------|---------|
| summary | CharField |
| description | TextField |
| employee | ForeignKey |
| assignee | ForeignKey |
| priority | Low / Medium / High |
| status | Open / In-Process / Closed |
| created_at | Date |
| resolved_at | Date |

---

## 🔐 Role-Based Access Control

### Employee Permissions
- Create Ticket
- View Own Tickets

### IT Staff Permissions
- View Assigned Tickets
- Update Ticket Status

### Manager Permissions
- View All Tickets
- Assign Tickets
- Monitor Ticket Progress

---

## 📊 Dashboard Overview

### Manager Dashboard
- Total Open Tickets
- In-Process Tickets
- Closed Tickets
- High Priority Tickets
- IT Staff Workload Analysis

### IT Staff Dashboard
- Assigned Tickets
- Open Tickets Queue
- Resolved Tickets
- High Priority Tasks

---
## 🗃️ Database ER Diagram
```
┌─────────────────┐
│     Employee    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Django Views    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Ticket Service  │
│ Priority Engine │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ MySQL Database  │
└─────────────────┘

         ▲
         │
┌─────────────────┐
│    IT Staff     │
└─────────────────┘

         ▲
         │
┌─────────────────┐
│    Manager      │
└─────────────────┘
```
##🗃️ Database ER Diagram
```
+----------------------+
|      CustomUser      |
+----------------------+
| id (PK)              |
| username             |
| email                |
| role                 |
| phone                |
| address              |
+-----------+----------+
            |
            |
            |
            ▼

+----------------------+
|        Ticket        |
+----------------------+
| id (PK)              |
| summary              |
| description          |
| priority             |
| status               |
| created_at           |
| resolved_at          |
| employee_id (FK)     |
| assignee_id (FK)     |
+----------------------+
```
##📈 Workflow
```
Employee Creates Ticket
           │
           ▼
 Priority Assigned Automatically
           │
           ▼
 Manager Reviews Ticket
           │
           ▼
 Assigns IT Staff
           │
           ▼
 IT Staff Resolves Issue
           │
           ▼
 Ticket Closed
```

##📊 Skills Demonstrated
```
 Backend Development
██████████████████ 95%

Database Design
█████████████████░ 90%

Authentication & Authorization
██████████████████ 95%

Django Framework
██████████████████ 95%

Problem Solving
█████████████████░ 90%
```

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AYUSHIPATEL123/Internal-Employee-Ticketing-System.git
```

### 2️⃣ Navigate to Project

```bash
cd Internal-Employee-Ticketing-System/emp_tic_man
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Configure Database

Update `settings.py` with your MySQL credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 7️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 9️⃣ Start Server

```bash
python manage.py runserver
```
## 🎨 Tailwind CSS Installation & Configuration

### Install Tailwind CSS

```bash
pip install django-tailwind
```

### Add Tailwind to Installed Apps

```python
INSTALLED_APPS = [
    ...
    'tailwind',
    'theme',
]
```

### Create Tailwind App

```bash
python manage.py tailwind init theme
```

### Configure Tailwind App

```python
TAILWIND_APP_NAME = 'theme'
```

### Install Tailwind Dependencies

```bash
python manage.py tailwind install
```

### Start Tailwind Development Server

```bash
python manage.py tailwind start
```

### Build Tailwind for Production

```bash
python manage.py tailwind build
```

### Example Tailwind Component

```html
<div class="bg-white rounded-lg shadow-md p-6">
    <h2 class="text-xl font-bold text-gray-800">
        Employee Dashboard
    </h2>
</div>
```

---

## 📸 Screenshots

<h3>Authentication & Dashboard</h3>

<p align="start">
  <img width="450" height="250" alt="Login Page" src="https://github.com/user-attachments/assets/7637dc81-9a46-4ac9-989b-aa2fd29620fa" />
  <img width="450" height="250" alt="IT Staff Dashboard" src="https://github.com/user-attachments/assets/ffa0253a-4073-4b8f-ac46-bc5b66480ab9" />
</p>

<h3>Ticket Management</h3>

<p align="start">
  <img width="450" height="250" alt="Ticket Management" src="https://github.com/user-attachments/assets/cf5e7ba7-6df1-459a-b688-b475512d956c" />
</p>


## 🎯 Key Highlights

✅ Custom User Authentication

✅ Role-Based Authorization

✅ Automatic Ticket Prioritization

✅ Dashboard Analytics

✅ Search & Filtering

✅ CRUD Operations

✅ MySQL Integration

✅ Class-Based Views

✅ Permission-Based Access

---

## 🔮 Future Improvements

- Email Notifications
- Ticket Comments
- File Attachments
- REST API Integration
- Real-Time Updates
- Activity Logs
- SLA Tracking

---

## 👩‍💻 Author

**Ayushi Patel**

GitHub:  
https://github.com/AYUSHIPATEL123

---

## 📜 License

This project is licensed under the MIT License.
