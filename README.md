# 🐍 Python Fundamentals

A structured, progressive repository for building a solid foundation in Python, from absolute basics to concurrency and real-world automation. Every module follows a logical learning path designed to compound knowledge naturally.

---

## 👤 Background

I'm a data student who, like many in the field, got into Python through libraries like pandas, NumPy, and scikit-learn, jumping straight into data manipulation and machine learning without ever properly learning the language underneath.

That gap became obvious over time. Debugging pipelines, writing reusable code, understanding what was actually happening under the hood, all of it was harder than it needed to be because the fundamentals weren't solid. Watching tutorials never fixed it. Reading documentation helped, but not enough.

The only thing that works is building things. So that's what this repository is.

---

## 🎯 Goal

This is not a collection of tutorial follow-alongs. Every project here is built from scratch, with intention, to understand why things work and not just that they work.

The objective is simple: close the gap between knowing how to use Python and actually understanding it. Project by project, module by module, until the language stops being a barrier and becomes a tool I reach for confidently, whether writing a data pipeline, automating a workflow, or building something entirely new.

---

## 📁 Structure

```
python-fundamentals/
│
├── 01-basics/
├── 02-control-flow/
├── 03-functions/
├── 04-modules-and-packages/
├── 05-data-structures/
├── 06-files-and-persistence/
├── 07-error-handling/
├── 08-oop/
├── 09-testing/
├── 10-apis-and-web/
├── 11-automation/
├── 12-concurrency/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── assets/
├── docs/
├── tests/
│
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
└── pyproject.toml
```

---

## 🗺️ Modules

| # | Module | What you'll learn |
|---|--------|-------------------|
| 01 | **Basics** | Variables, types, input/output, operators, string formatting |
| 02 | **Control Flow** | Conditionals, loops, comprehensions, pattern matching |
| 03 | **Functions** | Scope, recursion, decorators, lambda, `*args`/`**kwargs` |
| 04 | **Modules & Packages** | Imports, `__init__.py`, building your own packages, virtual environments |
| 05 | **Data Structures** | Lists, dicts, sets, tuples, stacks, queues, custom structures |
| 06 | **Files & Persistence** | File I/O, CSV, JSON, pathlib, context managers |
| 07 | **Error Handling** | Exceptions, custom exceptions, `try/except/finally`, logging |
| 08 | **OOP** | Classes, inheritance, dunder methods, dataclasses, SOLID principles |
| 09 | **Testing** | pytest, TDD, fixtures, mocks, coverage |
| 10 | **APIs & Web** | HTTP requests, REST APIs, JSON parsing, authentication |
| 11 | **Automation** | File operations, web scraping, email, PDF generation, scheduling |
| 12 | **Concurrency** | `threading`, `asyncio`, `multiprocessing`, the GIL explained |

---

## 🚀 Getting Started

**Requirements:** Python 3.11+

```bash
# Clone the repository
git clone https://github.com/your-username/python-fundamentals.git
cd python-fundamentals

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

To run any project:

```bash
cd 01-basics/hello-world-improved
python main.py
```

To run tests for a specific project:

```bash
cd 03-functions/math-library
pytest tests/
```

---

## 🛠️ CI / Code Quality

Every push runs automated checks via GitHub Actions:

- **ruff** — linting and formatting
- **mypy** — static type checking
- **pytest** — test suite

```bash
# Run locally before committing
ruff check .
mypy .
pytest
```

---

## 📌 Conventions

- Commits follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `refactor:`)
- Branch naming: `module/project-name` (e.g. `03-functions/scientific-calculator`)
- All code uses type hints and passes mypy in strict mode
- Projects are refactored as new modules introduce better patterns

---