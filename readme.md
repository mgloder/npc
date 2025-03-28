## Development

This project uses several tools to maintain code quality:

- **Black**: For code formatting
- **isort**: For import sorting
- **mypy**: For static type checking
- **pytest**: For testing

### Setup Development Environment

1. Clone the repository
   ```bash
   git clone https://github.com/mgloder/npc.git
   cd npc
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

### Running Tests

To run all tests:
```bash
pytest
```

To run specific tests:
```bash
pytest tests/test_hypo_gen.py  # Run only HypoGeneratorAgent tests
```

To run tests with verbose output:
```bash
pytest -v
```

To run tests with coverage report:
```bash
pytest --cov=app
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

[Instructions for contributors]

## Repository

This project is hosted on GitHub at: https://github.com/mgloder/npc
