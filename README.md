# ClassPulse

ClassPulse is a Streamlit application for classroom attendance. It provides teacher and student portals, uses face recognition for student identification, and includes voice-based attendance features. Supabase is used to store teacher, student, subject, enrollment, and attendance data.

## Features

- Teacher registration and password-based login
- Student identification and registration using a camera
- Subject creation and enrollment using subject codes
- Attendance analysis from classroom photos
- Voice sample enrollment and voice-based attendance
- Attendance records and subject summaries
- QR code generation for sharing subject join links

## Technology

- Python 3.10
- Streamlit
- Supabase
- dlib and face-recognition models
- scikit-learn, NumPy, and Pandas
- PyTorch, Resemblyzer, and librosa
- Pillow, bcrypt, and Segno

## Project Structure

```text
app.py
assets/
  logo.png
src/
  components/   Streamlit dialogs and reusable UI components
  database/     Supabase connection and database helpers
  pipelines/    Face and voice recognition processing
  screens/      Home, teacher, and student screens
  ui/           Shared layout and styling
requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Snapclass
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -3.10 -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Some dependencies, particularly dlib and WebRTC VAD, may require native build tools. On Windows, install Microsoft C++ Build Tools if pip reports that a C++ compiler is missing.

### 4. Configure Supabase

Create `.streamlit/secrets.toml` in the project directory:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_api_key"
```

Keep these credentials private. The repository's `.gitignore` excludes `.streamlit/`.

The Supabase project must have the tables and relationships used by the application:

- `teachers` — teacher account details
- `students` — student details and face/voice embeddings
- `subjects` — subject code, name, section, and teacher
- `subject_students` — student-to-subject enrollments
- `attendance_logs` — student attendance by subject and timestamp

Use column names that match the queries in `src/database/db.py` and the application screens.

### 5. Run the application

```bash
streamlit run app.py
```

## Using the Application

1. Open the Streamlit URL shown in the terminal.
2. Select the Teacher or Student portal.
3. Teachers can register or sign in, create subjects, share subject codes, and use the attendance tools.
4. Students can register or sign in using the camera and enroll in subjects using a subject code.

Camera and microphone access are required for face and voice workflows. The subject-sharing link currently uses `http://localhost:8501`; update the app URL in `src/components/dialog_share_subject.py` before sharing links from a deployed instance.

