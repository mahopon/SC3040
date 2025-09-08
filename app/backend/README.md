# Backend

This is the backend of the SC3040 project.

## ⚙️ Setup

1. Setup python virtual environment

   ```bash
   python -m venv venv

    # Mac/Linux
    source ./venv/bin/activate
    # Windows
    .\venv\Scripts\activate
   ```

2. Install dependencies

   ```bash
   pip install -r requirements-runtime.txt
   pip install -r requirements-dev.txt
   ```
   
3. Ensure local PostgreSQL instance is running (Using docker-compose provided or local install)
4. Create .env file under /app with the following values
```
APPNAME=
database_hostname=
database_port=
database_password=
database_name=
database_admin=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
```

5. Run migrations (Create tables)

   ```bash
   alembic upgrade head
   ```

6. Run mock_data.py to add mock data to database (Auth, user, petowner, petcaretaker, pet, service, offeredservice)

7. Run development server

   ```bash
   python -m app.main
   OR
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
