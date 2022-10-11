#jinote-api-v1
Backend server for jinote-web - note taking app
- This server only saves notes that the user has synced to the cloud

##Technologies
- Django 3.2.14
- python 3.7.10
- redis

##Setup
Step 1: active env: ```source ./env/bin/activate```\
Step 2: run ```pip install -r requirements.txt```

##Launch
Step 1: active env: ```source ./env/bin/activate```\
Step 2: run ```python manage.py runserver```\
(Note: change the configurations of the database to suit your environment)

##Migrate DB
```python3 manage.py migrate```
(other functions are list in https://github.com/conganwoz/jinote-api-v1/blob/develop/setup_note.txt)
