# Horarios ETSIINF UPM
Django app that generates the different possible schedules for the combination of subjects you choose.

The web also has some relevant links that are useful for a ETSIINF's student. 

## Installation
1\. Install **python 3.7** 
```bash
$ sudo apt install python3.7
```
2\. Install pip
```bash
$ sudo apt install python-pip
```
3\. Install virtualenvwrapper
```bash
$ sudo apt install virtualenvwrapper
```
4\. Create a virtual environment
```bash
$ mkvirtualenv --python=/usr/bin/python3.7 Horarios-ETSIINF
```
If the virtual environment is not activated, activate it
```bash
$ workon Horarios-ETSIINF
```
5\. Install the requirements
```bash
$ pip install -r requirements.txt
```
## Run
1\. You need to set up the DB. For that I have created a script that creates the DB and loads the subjects in the [data.dat](/ImportData/data.dat) into the database.

**Note**: The subjects in the file are the ones taught in the course 18-19 in the ETSIINF.
```bash
$ ./importData.sh
```
2\. Once the DB is created, just run the server
```bash
$ ./run.sh
```
And go to the url: `http://127.0.0.1:8000`.

If you want to go to the admin site, you have to create a superuser for the DB. When you run the [importData.sh](/importData.sh) script, it will ask you if you want to create a superuser.

Other way to create a superuser is:
```bash
$ python manage.py createsuperuser
```
or
```bash
$ ./manage.py createsuperuser
```
Once you have your superuser created, got to the admin page: `http://127.0.0.1:8000/admin`.
## Import your own data
If you want this app to work with your specific data, edit the file [data.dat](/ImportData/data.dat), with the requirements in the [README.md](/ImportData/README.md) in the [ImportData](/ImportData) directory.
## License
[GNU GENERAL PUBLIC LICENSE](/LICENSE).
## Links
[Escuela Técnica Superior de Ingenieros Informáticos](http://www.etsiinf.upm.es/)

[Universidad Politécnica de Madrid](http://www.upm.es/)

## Author
[Victor Nieves Sánchez](https://twitter.com/VictorNS69)