install:
	poetry install

udp:
	poetry run python3 src/qlabmaker/oscudptest.py
qlab:
	poetry run python3 src/qlabmaker/gfx.py

server:
	poetry run python3 src/qlabmaker/async_server.py

django:
	poetry run python3 src/programweb/manage.py runserver

migrate:
	poetry run python3 src/programweb/manage.py migrate

migrations:
	poetry run python3 src/programweb/manage.py makemigrations

remoteqlab:
	poetry run python3 src/qlabmaker/remoteqlab.py
