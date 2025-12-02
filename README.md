# RichORM

RichORM is a lightweight Python Object Relational Mapper (ORM) built from scratch, inspired by Django’s ORM.  
It demonstrates advanced Python concepts such as **metaclasses**, **descriptors**, and **field validation** to provide a minimal but functional ORM layer.

## ✨ Features

- Field system with built-in types:
  - `CharField` (string with `max_length` validation)
  - `IntegerField`
  - `BooleanField`
  - `EmailField`
- Field constraints: `null`, `unique`, `default`, `primary_key`, `max_length`
- Validation of field names (no reserved keywords, no `__`, no trailing `_`)
- Metaclass-based model registration (`BaseModel`)
- Descriptor protocol for attribute management (`__get__`, `__set__`)
- CLI integration with [`uv`](https://docs.astral.sh/uv/)
  
- **CLI Layer**
  - Built with [Click](https://click.palletsprojects.com/)
  - Generates project-level config files in YAML
  - Supports multiple database backends: `sqlite3`, `mysql`, `postgresql`, `oracle`
  - Stores final configuration in a hidden directory (`~/.richorm/config.yaml`)
  - Validation of driver parameters with helpful error messages
---

## 🚀 Installation

Clone the repository and install in **editable mode** with [`uv`](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/Shubham-392/richorm.git
cd richorm
uv tool install --editable .


Usage: richorm [OPTIONS] COMMAND [ARGS]...

Options:
  -d, --driver TEXT  Driver for ORM (default: sqlite3)
  --version          Show the version and exit.
  --help             Show this message and exit.

Commands:
  read  Read and validate a configuration file

Usage: richorm read [OPTIONS] CONFIG_PATH

Arguments:
  CONFIG_PATH  Path to the richorm configuration YAML file.

Options:
  --help  Show this message and exit.

```
<p style="color:red;"><b>⚠️ This is a learning project. It is not intended to replace existing ORMs like Django ORM or SQLAlchemy.</b></p>

