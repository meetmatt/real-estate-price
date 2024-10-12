.PHONY: build
build:
	docker compose build

.PHONY: run
run: build
	docker compose up -d
	${MAKE} open-frontend

.PHONE: open-frontend
open-frontend:
	open "http://localhost"

.PHONY: test-api
test-api:
	@curl -X 'POST' \
      'http://localhost/api/predict' \
      -H 'Content-Type: application/json' \
      -d '{"area": 120, "bedrooms": 3}'
