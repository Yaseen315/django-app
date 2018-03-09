csv_path = "/Users/tayyibafazal/django-app/helloapp/catalog/ARTISTS.csv"
app_path = "/Users/tayyibafazal/django-app/helloapp"
import sys,os sys.path.append(app_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' from models.py import models import csv dataReader = csv.reader(open(csv_path)