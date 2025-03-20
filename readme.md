## Development

This project uses several tools to maintain code quality:

- **Black**: For code formatting
- **isort**: For import sorting
- **mypy**: For static type checking
- **pytest**: For testing

### Setup Development Environment

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install the package in development mode
   ```

### Setup Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality before commits.

1. Install pre-commit
   ```bash
   pip install pre-commit
   ```

2. Install the git hooks
   ```bash
   pre-commit install
   ```

3. (Optional) Run against all files
   ```bash
   pre-commit run --all-files
   ```

Pre-commit will now run automatically on every commit to check your changes.

## License

[Choose an appropriate license]

## Contributing

[Instructions for contributors]
