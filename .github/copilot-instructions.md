# Copilot Instructions for github-actions-lab

## Project Overview
- This repo is a Python FastAPI web app with two main endpoints: `/` (Hello World) and `/items/{item_id}` (item lookup).
- The codebase is containerized for VS Code development using dev containers (`.devcontainer/Dockerfile`).
- CI/CD is managed via GitHub Actions, running tests, linting, building Docker images, and scanning for vulnerabilities.

## Key Files & Structure
- `src/main.py`: Main FastAPI app and endpoints.
- `src/pyproject.toml`: Python project metadata and dependencies.
- `src/uv.lock`: Dependency lock file for reproducible builds.
- `src/tests/main_test.py`: Pytest-based tests for API endpoints.
- `.devcontainer/Dockerfile`: Dev container setup (Debian, Python, Node.js, Fish shell).
- `docker-compose-test.yml`: Compose file for local testing (if present).

## Developer Workflows
  ```fish
  uv sync --locked
  ```
  ```fish
  uvicorn main:app --reload
  ```
  ```fish
  pytest
  ```
  ```fish
  flake8 src/
  ```
  ```fish
  docker build -f Dockerfile.actions -t fastapi-example .
  ```
**Install dependencies:**
  ```fish
  uv sync --locked
  ```
**Run app locally:**
  ```fish
  uvicorn main:app --reload
  ```
**Run tests (use `uv run`):**
  ```fish
  uv run pytest
  ```
**Lint code (use `uv run`, exclude cache/build folders):**
  ```fish
  uv run flake8 src/ --exclude=.venv,__pycache__,build,fastapi_example.egg-info
  ```
**Run coverage (use `uv run`):**
  ```fish
  uv run coverage run -m pytest
  uv run coverage report
  ```
**Build Docker image:**
  ```fish
  docker build -f Dockerfile.actions -t fastapi-example .
  ```

## Patterns & Conventions
- All Python code lives in `src/`.
- Tests are in `src/tests/` and use pytest.
- Use `uv` for dependency management (see `uv.lock`).
- Endpoints follow FastAPI conventions; see `main.py` for structure.
- CI/CD expects tests and linting to pass before building/publishing images.

## Integration Points
- GitHub Actions workflows (not shown here) automate build, test, lint, scan, and publish steps.
- Docker images are pushed to GitHub Container Registry.
- Trivy and Checkmarx are used for security scanning.

## Example: Adding an Endpoint
- Define new routes in `src/main.py` using FastAPI's `@app.get` or `@app.post` decorators.
- Add corresponding tests in `src/tests/main_test.py`.

## References
- See `README.md` and `src/README.md` for more details and example commands.

---
_If any section is unclear or missing, please provide feedback to improve these instructions._
