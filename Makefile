install:
	poetry install

udp:
	poetry run python3 src/qlabmaker/oscudptest.py
qlab:
	poetry run python3 src/qlabmaker/gfx.py

group:
	poetry run python3 src/qlabmaker/gfxgroup.py


server:
	poetry run python3 src/qlabmaker/async_server.py

django:
	poetry run python3 src/programweb/manage.py runserver

fixtures:
	poetry run python3 src/programweb/manage.py dumpdata > fixtures.json
swagger:
	poetry run python3 src/programweb/manage.py spectacular --color --validate --file src/programweb/schema.yml

migrate:
	poetry run python3 src/programweb/manage.py migrate

migrations:
	poetry run python3 src/programweb/manage.py makemigrations

remoteqlab:
	poetry run python3 src/qlabmaker/remoteqlab.py
