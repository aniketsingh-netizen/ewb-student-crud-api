# EWB Internship Project: Students Database CRUD Application

A robust Python-based backend application built with FastAPI and SQLite to manage student records via Create, Read, Update, and Delete (CRUD) operations, complete with automated input validation using Pydantic.

---

## **Project Features**
* **Create**: Add new student profiles with personal and academic details.
* **Read**: Retrieve all student records or filter them by specific courses.
* **View**: Look up individual student records using their unique student ID.
* **Update**: Modify existing student details dynamically.
* **Delete**: Remove student records from the database.

---

## **Tech Stack**
* **Backend Framework:** FastAPI (Python)
* **ASGI Server:** Uvicorn
* **Database:** SQLite
* **Data Validation:** Pydantic

---

## **Project Structure**
```text
├── main.py              # Main FastAPI application and SQLite configuration
└── requirements.txt     # Project dependencies


git clone https://github.com/aniketsingh-netizen/ewb-student-crud-api/new/main


python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate




pip install -r requirements.txt




uvicorn main:app --reload



Method,Endpoint,Purpose
POST,/students,Create a new student record
GET,/students,List all students or filter by course
GET,/students/{student_id},View a single student by ID
PUT,/students/{student_id},Update student details
DELETE,/students/{student_id},Delete a student record




Prerequisites & InstallationMake sure you have Python installed on your system. Follow these steps to run the project locally:Clone the repository:Bashgit clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)
cd YOUR-REPOSITORY-NAME
Create and activate a virtual environment (Optional but recommended):Bashpython -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:Bashpip install -r requirements.txt
How to Run the ApplicationStart the FastAPI development server using Uvicorn:Bashuvicorn main:app --reload
The server will start running locally at http://127.0.0.1:8000.API Testing Instructions (Swagger UI)FastAPI automatically generates interactive API documentation.Open your browser and navigate to:👉 http://127.0.0.1:8000/docsExpand any of the endpoints (POST, GET, PUT, DELETE).Click Try it out, fill in the required payload or parameters, and click Execute to test the API responses and interact with the SQLite database.API Endpoints SummaryMethodEndpointPurposePOST/studentsCreate a new student recordGET/studentsList all students or filter by courseGET/students/{student_id}View a single student by IDPUT/students/{student_id}Update student detailsDELETE/students/{student_id}
