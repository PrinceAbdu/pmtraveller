#!/bin/bash
echo "Installing dependencies..."
/opt/vercel/python3/bin/python -m pip install -r requirements.txt

echo "Creating staticfiles directory if it doesn't exist..."
mkdir -p staticfiles

echo "Collecting static files..."
/opt/vercel/python3/bin/python manage.py collectstatic --noinput --clear

echo "Listing contents of staticfiles directory..."
ls -la staticfiles/

echo "Build completed."