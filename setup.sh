#!/bin/bash

echo "Creating Python Virtual Environment..."
python3 -m venv venv

echo "Activating Virtual Environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt

echo "Setup complete!"