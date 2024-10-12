.PHONY: build
build:
	docker build -t real-estate-api --progress plain .

.PHONY: run
run:
	docker run -p 8000:8000 real-estate-api

.PHONY: test
test:
	@curl -X 'POST' \
      'http://127.0.0.1:8000/predict' \
      -H 'Content-Type: application/json' \
      -d '{"area": 120, "bedrooms": 3}'
