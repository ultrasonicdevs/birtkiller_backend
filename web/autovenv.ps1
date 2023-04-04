"Creating local virtual environment"
"==================================="
python -m venv venv

"Activating local virtual environment"
"==================================="
./venv/Scripts/activate.ps1

"Upgrading pip"
"==================================="
python -m pip install --upgrade pip

"Installing requirements from project's folder requirements.txt"
"==================================="
pip install -r .\req.txt

"Making Django migrations"
"==================================="
python manage.py makemigrations
python manage.py migrate

"Asking for Superuser creation prompt"
"==================================="
python manage.py createsuperuser
"Successfully prepared to start"
"Congratulations!!!"
"==================================="
"==================================="
"==================================="
"execute 'python manage.py runserver' to start test webserver"