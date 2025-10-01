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

---

## 🚀 Installation

Clone the repository and install in **editable mode** with [`uv`](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/<your-username>/richorm.git
cd richorm
uv tool install --editable .
