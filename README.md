# github-actions-lab

This repository contains a simple Python web application built with the FastAPI framework.

## About

The application has two API endpoints:

*   A root endpoint (`/`) that returns a simple "Hello World" message.
*   An `/items/{item_id}` endpoint that takes an ID and an optional query parameter.

## Development

This repository is set up for development with [VS Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers). This allows you to open the project in a pre-configured Docker container for a consistent development experience.

To get started, open the repository in VS Code and run the **Remote-Containers: Reopen in Container** command.

## CI/CD

This repository has a robust GitHub Actions workflow that automatically runs on every push or pull request to the `main` branch. This pipeline does the following:

*   Installs dependencies and runs tests using `pytest`.
*   Performs static code analysis using `flake8`.
*   Builds a Docker image of the application.
*   Scans the code and Docker image for vulnerabilities using Trivy and Checkmarx tools.
*   Pushes the built Docker image to the GitHub Container Registry.
