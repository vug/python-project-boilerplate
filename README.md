# Boilerplate for Python Projects

## Description

Skeleton code for a new Python project.

- Layout
  - for single package "helloworld" project with a main module and helper modules (from [Python Application Layouts: A Reference – Real Python](https://realpython.com/python-application-layouts/))
  - tests for main and helper modules
- Dependencies
  - `pipenv` based dependency management
  - It also handles virtual environment management
  - Basic development libraries included such as
    - `flake8` for linting, formatting style and other warnings
    - `black` for auto formatting. Frees developers from thinking about style and bikeshedding
    - `pytest` for unittesting
    - `mypy` for static type checking (tried `pyre-check` first but thanks to Unix only dependency `fcntl` it does not work on windows.)
- `setup.py` for distribution
- `README.md` for project description
- `.gitignore` for common files not needed in version control
- Recommended editors
  - VS Code with following extensions. As the main IDE.
    - [Python \- Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [PlantUML \- Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml) (requires GraphViz) for software design with UML diagrams
  - Vim. When not having access to my desktop/laptop. For example, when SSH'ing to my devserver from iPad.

## Usage

- Download the project zip file (TODO: think about a flow with `git clone`)
- Rename files and folder according to new project name
- `pipenv`
  - if `pipenv` does not exist in base Python distribution install it via `pip install pipenv`
  - `pipenv install --dev --pre` to create virtual environment for the project under `~/.virtualenvs/PROJECT_NAME-hash` and install developer dependencies. (Currently `--pre` is needed for black because its version is less then `1`.)
  - to activate project environment `pipenv shell`
- `git init` to initialize a git repo
- for VS Code
  - set `python.pythonPath` setting
  - install following extensions if not already installed
