Write-Host "Creating Python Virtual Environment..."
python -m venv venv

Write-Host "Activating Virtual Environment..."
.\venv\Scripts\Activate.ps1

Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "Installing requirements..."
pip install -r requirements.txt

Write-Host "Setup complete. Environment ready!"
pause