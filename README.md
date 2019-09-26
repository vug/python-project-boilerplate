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
      - Needs [Graphviz](https://graphviz.gitlab.io/) to be installed and in `PATH` to produce diagrams other than sequence
      - http://plantuml.com has lots of diagram examples
    - [Better Comments \- Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
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
  - set `python.pythonPath` setting (TODO: figure out the right way of doing this.)
  - install following extensions if not already installed
- Runing unittests
  - CLI: Run either `pytest` or `python -m pytest` from project root
    - (The latter puts project root to `sys.path`)
    - `python -m pytest tests/ --collect-only` command to only discover tests
  - VS Code: Tests can be discovered and run from the "Tests" tab. Individual tests can be run from the opened file directly.
    - (Added an `__init__.py` file in `tests/` folder to turn it into a package (which can do imports from sibling packages). It shouldn't be needed but the way test discovery mechanism works in VS Code Python extension requires that. See [1](https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada), [2](https://github.com/microsoft/vscode-python/issues/6347) )
