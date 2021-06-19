# swapi_pro
Implemented search to swapi api

Installation on local machine:
  1. Install Python
  2. Install django-2.2 using **pip install django==2.2**
  3. install requests-cache  **pip install requests-cache**
  4. install pandas **pip install pandas**
  5. Create a new conda environment **conda create -n "name" **
  6. clone repo **https://github.com/Nikhilhc/swapi_pro.git**
  7. cd swapi_pro
  8. python manage.py runserver

OUTPUT:
Watching for file changes with StatReloader
Performing system checks...

URL:  https://swapi.dev/api
STATUS_CODE:  200
Content-type:  application/json
System check identified no issues (0 silenced).
June 19, 2021 - 16:03:37
Django version 2.2, using settings 'swapi_pro.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

In backend it connects to swapi api base url where it fetches the resources available in that api.
You can select the resource in which you want to search for.
If in case you need all the data from the particular resource,type **all** in search bar and you get all the details of the selected resource.

