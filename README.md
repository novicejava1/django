<h1>Generate Graphs based on JSON Input Files</h1>

############################################################################################################################
### This Project is for generating the selected chart type graph for the provide JSON file
############################################################################################################################

<h2>1. Install and validate Python 3.5 and later version</h2>

sudo apt-get update
sudo apt-get install python3

<h2>2. Install and validate django 2.1 and later version</h2>

pip install Django

<h2>3. Install json2html python module</h2>

pip install json2html

<h2>4. Clone the repository onto local machine</h2>

git clone https://github.com/novicejava1/django.git

<h2>5. Run the Application</h2>

python manage.py runserver 0:8000

<h2>6. Test the URL</h2>

http://<FQDN or IP>:8000/reports/selectchart

Note - Make sure to download and use the json files uploaded in the project repository jsonfiles folder. 

Fusioncharts Usage Ref - https://www.fusioncharts.com/dev/getting-started/django/your-first-chart-using-django
