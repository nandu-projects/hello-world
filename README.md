# Hello World

A clean, modern Hello World application built in Python with automated unit tests and continuous integration readiness.

---

## 🚀 Features

- Configurable greetings via CLI arguments or programmatic API.
- Input sanitization and edge-case handling (empty, whitespace, null inputs).
- Comprehensive test coverage using Python's standard `unittest` framework.
- Zero external dependencies.

---

## 🛠️ Usage

### Run the program:
```bash
python src/main.py
```
Output:
```text
[2026-10-01 07:43:00] Hello, World!
```

### Pass a custom name:
```bash
python src/main.py Antigravity
```
Output:
```text
[2026-10-01 07:43:00] Hello, Antigravity!
```

---

## 🧪 Running Tests

Execute the unit test suite:
```bash
python -m unittest discover tests
```
