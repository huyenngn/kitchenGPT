.PHONY: generate-api-docs

generate-api-docs:
	@echo "Starting FastAPI app..."
	python -m kitchengpt &
	@sleep 10
	@echo "Downloading OpenAPI JSON..."
	curl http://127.0.0.1:8000/openapi.json -o ./src/public/openapi.json
