export PYTHONPATH=${PROJDIR}/dj:${PROJDIR}/

function pushd2() {
  PUSHED="$(pwd)"
  cd "$PROJDIR""$1" >>/dev/null
}

function popd2() {
  cd "${PUSHED:-"$PROJDIR"}" >>/dev/null
  unset PUSHED
}

function manage() {
  pushd2 /dj
  python manage.py $*
  r=$?
  popd2
  return ${r}
}

showmigrations() {
  manage showmigrations $*
}

function makemigrations() {
  manage makemigrations $*
}

function migrate() {
  manage migrate $*
}

function djshell() {
  manage shell_plus
}

function dbshell() {
  manage dbshell
}

function createsuperuser() {
  manage createsuperuser
}

function recreatedb() {
  psql -h pg -U postgres -c "DROP USER IF EXISTS shankara;"
  psql -h pg -U postgres -c "CREATE USER shankara;"
  psql -h pg -U postgres -c "ALTER USER shankara WITH SUPERUSER;"
  psql -h pg -c "DROP DATABASE IF EXISTS shankara;" template1
  psql -h pg -c "CREATE DATABASE shankara" template1
  psql -h pg -c "CREATE EXTENSION IF NOT EXISTS citext;" shankara
  migrate $*
}

function pyfmt() {
  black "$PROJDIR"/dj
}

function cmp() {
  mvn -B package -DskipTests=true
}

function run() {
  java -jar -Dspring.profiles.active=local target/shankara-0.0.1-SNAPSHOT.jar
}

function run_dj() {
  manage runserver 0.0.0.0:8002
}

function cmr() {
  cmp && run
}