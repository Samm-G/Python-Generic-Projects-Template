# Git-test-2 Project
Git-Test-2 project for a standard git testing template.

## Getting Started:

Create a Conda Env using the given bash script, to start development:
```bash
bash init_setup.py -v 3.7.12
```

## Test your project:
- Method 1: Pytest:
    ```bash
    pytest -v
    ```
- Method 2: Tox:
    ```bash
    # Run tests
    tox

    # Run with recreation of all envs again, (If requirements.txt changes)
    tox --recreate
    ```

## Recreate Docs using MkDocs

See Docs for your project:
```bash
mkdocs serve
```

