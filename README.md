# SIM_Master
SIM 卡管理后端


基于 Django + Restful Framework

# STEPS
## 1. Clone
git clone https://github.com/aod321/SIM_Master_Backend.git
## 2. Enter
cd SIM_Master_Backend
## 3. Dependency
pip -r install requirements.txt

## 4. DataBase
### 4.1 Create a Database named sim_master
### 4.2 Change "settings.py"


```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "sim_master",   // DataBase Name
        "USER": "root",   // Change to your Database user
        "PASSWORD": "root", // Change to your Database password
        "HOST": "localhost",
        "PORT": "3306",
    }
}

```

## 5. Migrations
python manage.py makemigrations
python manage.py migrate

## 6. Run Sever
python manage.py runserver



    
