🚀 CodePilot API  
CodePilot is a lightweight, high-performance RESTful API backend built with Django REST Framework (DRF) designed to automate online coding exams, question bank management, and real-time submission evaluation.

⚙️ Key Architecture
accounts/: Custom auth backends, student/admin profiles, and RBAC token authentication.
problem/: Dynamic problem generation, difficulty levels, and test-case mapping.
exams/: Assessment scheduling, time-window constraints, and duration enforcement.
evaluation/: Secure submission handling, permission guards, and automated test-case scoring.
🛠️ Quick Start
# Clone the project
git clone https://github.com/allwin-dev-in/code_pilot.git
cd codepilot

# Setup environment & dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirments.txt

# Run migrations & start server
python manage.py migrate
python manage.py runserver

⚡ API Endpoint Testing
Use the included APIDOC.http file with the VS Code REST Client extension or import into Postman to test auth, exam creation, and evaluation endpoints directly.
