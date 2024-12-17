Clone the repository : git clone 

Navigate to the project directory:  cd agritech_project/agritech

create a virtual environment: virtualenv env

activate the environment : cd env/scripts/activate

Install dependencies: pip install -r requirements.txt

Install Tesseract OCR tool in your local machine (windows) : https://github.com/tesseract-ocr/tesseract

confirm installation using : tesseract --version

finally run the following command : python manage.py makemigrations
                                    python manage.py migrate
                                    python manage.py  runserver
