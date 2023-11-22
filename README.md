
# Clinicals App

Make sure you are in the clinicals Directory. This repository contains the source code for the Clinicals App, a Django-based application that utilizes Docker for containerized deployment and a MySQL database.

## Setup

### 1. Run MySQL Docker Container

```
docker run -d -p 6666:3306 --name=django-mysql --env="MYSQL_ROOT_PASSWORD=test123" --env="MYSQL_DATABASE=clinicalsdb" mysql:8.0.15 --default-authentication-plugin=mysql_native_password
```
### 2. Create Clinical App Docker File
```
docker build -f Dockerfile -t clinicals_app .
```
```
docker run -t --name=clinicals-app --link django-mysql:mysql -p 10555:8000 clinicals_app
```
### 3. Migrate Mysql Database
```
docker exec -it clinicals-app bash
```
```
docker exec -it clinicals-app python manage.py migrate
```
### 4. Run ClinicalApp
```
http://localhost:10555
```
