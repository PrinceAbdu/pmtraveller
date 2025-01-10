echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating static directory if it doesn't exist..."
mkdir -p staticfiles

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear
echo "Build completed"