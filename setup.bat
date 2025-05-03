@echo off
echo Creating Python Virtual Environment...
python -m venv venv

echo Activating Virtual Environment...
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing requirements...
pip install -r requirements.txt

echo Setup complete.
pause