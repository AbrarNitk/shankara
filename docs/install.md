# Install guide

1. Install Java
2. Install Maven
3. Install pip
4. Install pyenv
5. Install autoenv
6. Install postgres
7. Install python 3.8 using pyenv `pyenv install 3.8.0`
8. Create virtual-env with python 3.8 `pyenv virtualenv 3.8.0 shankara`
9. Install requirements `pip install -r requirements.txt`
10. `source etc/zsh/auto.sh`
11. Run command `migrate` as alias to  `python manage.py migrate`
12 Create Super User `createsuperuser`, Enter valid phone and password.
13. Run Django to check Django admin `run_dj` as alias to `manage runserver 0.0.0.0:8002`
13. Compile java `cmp` as alias to  `mvn -B package -DskipTests=true`
14. Now check run java `run` as alias to `java -jar -Dspring.profiles.active=local target/shankara-0.0.1-SNAPSHOT.jar`