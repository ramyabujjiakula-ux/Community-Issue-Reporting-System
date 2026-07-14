# Community Issue Reporting System

A web-based **Community Issue Reporting System** developed using **Django** that enables citizens to report local community issues such as road damage, water supply problems, health concerns, education-related issues, and other public grievances. The system allows administrators to manage complaints, update their status, and respond to users through an integrated dashboard.

---

## 📌 Project Overview

The Community Issue Reporting System provides a simple platform for citizens to submit issues affecting their locality. Users can register, log in, upload issue images, and monitor the progress of their complaints. Administrators can review submitted issues, categorize them, update their status, and communicate with users by posting replies.

---

## ✨ Features

### User Features

- User Registration
- User Login & Logout
- Submit Community Issues
- Upload Issue Images
- Select Issue Category
- Create Custom Categories
- View Issues by Category
- Track Issue Status
- View Detailed Issue Information

### Administrator Features

- Secure Admin Login
- View All Submitted Issues
- Update Issue Status
- Reply to Citizen Complaints
- Manage Departments
- Manage Categories
- Django Admin Dashboard

---

## 🛠 Tech Stack

| Technology | Description |
|------------|-------------|
| Python | Programming Language |
| Django 5.2.15 | Backend Framework |
| SQLite3 | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| Django Authentication | User Management |
| Pillow | Image Upload Support |

---

## 📂 Project Structure

```
community_app/
│── community_app/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
│── reports/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│
│── templates/
│   └── reports/
│
│── static/
│
│── media/
│
│── manage.py
│── requirements.txt
```

---

## 🗄 Database Models

### Department

- Department Name
- Contact Email

### Issue

- Title
- Description
- Category
- Custom Category
- Photo Upload
- Status
- Created Date
- Submitted User
- Assigned Department

### Reply

- Related Issue
- Author
- Reply Message
- Created Date

---

## 📋 Issue Categories

- Road
- Water
- Education
- Health
- Other (Custom Category)

---

## 📊 Issue Status

- Submitted
- In Progress
- Resolved

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/community-issue-reporting-system.git
```

### Navigate to Project

```bash
cd community-issue-reporting-system
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Database Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start Development Server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

### User

- Register
- Login
- Submit Issues
- Track Complaint Status

### Administrator

- Login through Admin Login
- Manage Issues
- Update Status
- Reply to Complaints

---

## 📷 Screenshots

Add screenshots inside the project and update this section.

Example:

```
screenshots/
    home.png
    login.png
    signup.png
    category.png
    issue-details.png
    admin-dashboard.png
```

Markdown Example:

```md
## Home Page

![Home](community_app/screenshots/home.png)

## Login

![Login](community_app/screenshots/login.png)
```

---

## 🔄 Workflow

1. User Registration
2. User Login
3. Submit Community Issue
4. Upload Supporting Image
5. Issue Stored in Database
6. Administrator Reviews Complaint
7. Administrator Updates Status
8. Administrator Replies
9. User Tracks Progress

---

## 🔮 Future Enhancements

- Email Notifications
- SMS Alerts
- Google Maps Integration
- Complaint Search
- Complaint Filtering
- Dashboard Analytics
- Department-wise Reports
- REST API Integration
- Mobile Application
- Real-time Notifications

---

## 📚 Learning Outcomes

This project demonstrates:

- Django Web Development
- Django Authentication
- CRUD Operations
- Model Relationships
- File Upload Handling
- Admin Customization
- Form Validation
- URL Routing
- Database Design
- User Authorization

---

## 👩‍💻 Author

**Ramya Akula**

B.Tech - Artificial Intelligence

Sri Vasavi Engineering College

---

## 📄 License

This project is developed for educational and learning purposes.