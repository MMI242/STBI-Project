.PHONY: build dev indexing search extraction webapp clean

# Build the Docker image
build:
	docker compose build

# 1. Development/debug (enter bash)
dev:
	docker compose --profile dev run --rm base bash

# 2. Run Indexing
indexing:
	docker compose --profile indexing run --rm indexing

# 3. Run Search CLI
search:
	docker compose --profile search run --rm search

# 4. Run Extraction CLI
extraction:
	docker compose --profile extraction run --rm extraction

# 5. Run Web App (port 8000)
webapp:
	docker compose --profile webapp up webapp

# Clean up containers
clean:
	docker compose down --remove-orphans
