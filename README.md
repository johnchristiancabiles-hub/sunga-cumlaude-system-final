# 🎓 Sunga Cumlaude System

A comprehensive and unified School Management System designed to streamline class record management, daily attendance tracking, and grade computations for teachers and administrators.

## 🌟 Key Features
* **Unified Teacher Dashboard:** A single-page interface to minimize clicking and navigating between different pages.
* **Class Record (Excel View):** Fast and intuitive encoding of attendance and grades grouped by subject and schedule.
* **Individual Student 360 Records:** Combined attendance history and grading assessments organized into clean, interactive badges.
* **Admin Control Panel:** Masterlist management for globally adding, editing, and deleting student records and subject schedules.
* **Anti-Duplicate Class Logic:** Built-in error handling to prevent teachers from creating double rosters for the same schedule.

## 🛠️ Technology Stack
* **Backend Framework:** Django (Python)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Accordion & Tabs for UI)
* **Database:** SQLite (Default Django DB)

## 👥 Meet the Development Team

**Lead Developers / System Integrators**
* John Christian Cabiles
* Jerric Sayno

**1. User & Attendance Module**
* Kenneth Oliva (User Accounts & Masterlist)
* Vanessa Anacin (Attendance Logs & Tracking)

**2. Scheduling & Record Module**
* Mark Anthony Sunga (Schedules & Roster Matrix)
* Rodnie Malacas (Roster UI & Security)
  
**3. Grading & Assessment Module**
* Jerric Sayno (Grading Engine & Computations)
* John Christian Cabiles (System Integration & Dashboard)

## 🚀 How to Run the System Locally

Follow these steps to run the Sunga Cumlaude System on your own machine. You can copy and run these commands in your terminal:

```bash
# 1. Clone the repository
git clone [https://github.com/johnchristiancabiles-hub/sunga-cumlaude-system-final.git](https://github.com/johnchristiancabiles-hub/sunga-cumlaude-system-final.git)

# 2. Navigate to the project folder
cd sunga-cumlaude-system-final

# 3. Install the required dependencies
pip install django

# 4. Run the database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the local development server
python manage.py runserver

# 6. Open your browser:
Go to http://127.0.0.1:8000/ to access the login page.
