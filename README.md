# QuantumLab Course

Standalone quantum computing course — 11 modules, Theory + Hands-on notebooks.
No API keys. No external services. Just Python.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload --port 8001
```

Open http://localhost:8001

## Structure

```
quantumlab-course/
├── main.py              ← FastAPI app (single route)
├── requirements.txt     ← fastapi, uvicorn, jinja2 only
├── templates/
│   ├── base.html
│   └── learn.html       ← sidebar + module loader
└── modules/             ← all 11 course HTML files
    ├── module-00.html
    ├── module-02.html
    └── ...
```

## Modules

| Module | Title |
|--------|-------|
| M00 | Why Quantum Computing? |
| M02 | Quantum Gates & Circuits |
| M03 | Entanglement & Bell States |
| M04 | Grover's Algorithm |
| M05 | Introduction to Optimisation |
| M06 | Classical ML → Quantum ML |
| M07 | VQC Project: Fashion-MNIST on IBM QPU |
| M08 | QAOA – Quantum Approximate Optimization |
| M09 | Quantum Annealing & QUBO |
| M10 | Hybrid Quantum-Classical Workflows |

## Requirements

- Python 3.10+
- No API keys needed
- No database
- No external services
