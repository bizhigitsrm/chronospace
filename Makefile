VENV=backend/venv
PYTHON=${VENV}/bin/python
PIP=${VENV}/bin/pip
UVICORN=${VENV}/bin/uvicorn

.PHONY: help install-backend run-backend test-backend install-frontend run-frontend

help:
	@echo "Makefile commands:"
	@echo "  make install-backend   -> create venv and install backend deps"
	@echo "  make run-backend       -> run backend (uvicorn app_main:app)"
	@echo "  make test-backend      -> run backend tests"
	@echo "  make install-frontend  -> npm install in frontend"
	@echo "  make run-frontend      -> run frontend dev server"

install-backend:
	python3 -m venv ${VENV}
	${PIP} install --upgrade pip
	${PIP} install -r backend/app/req.txt

run-backend:
	${UVICORN} backend.app.app_main:app --reload --port 8000

test-backend:
	PYTHONPATH=backend ${VENV}/bin/pytest -q backend/app/tests

install-frontend:
	cd frontend && npm install

run-frontend:
	cd frontend && npm run dev
