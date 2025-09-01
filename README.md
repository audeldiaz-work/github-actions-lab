# github-actions-lab

This repository contains a Python web application built with the FastAPI framework.

## Important Policy
All documentation, comments, and instructions must always be written in English.

## About

The application provides three API endpoints (`/`, `/items/{item_id}`, `/timestamp`). The `/items/{item_id}` endpoint echoes the provided ID and optional query parameter and does not access any external datastore.

## Development

This repository is configured for development with VS Code Dev Containers. Open the repo in VS Code and run **Remote-Containers: Reopen in Container** to work inside the recommended container.

## CI/CD

This repository includes GitHub Actions workflows that run on pushes and pull requests to `main`. The pipeline installs dependencies, runs tests, lints the code, builds a Docker image, scans for vulnerabilities, and optionally publishes the image to GitHub Container Registry.
