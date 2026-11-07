# SimPython
SimPython/
│
├── .venv/
│
├── src/
│   └── simp/
│       │
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   ├── simulation.py
│       │   ├── clock.py
│       │   └── state.py
│       │
│       ├── physics/
│       │   ├── __init__.py
│       │   ├── vectors.py
│       │   ├── forces.py
│       │   ├── mechanics.py
│       │   ├── collisions.py
│       │   └── gravity.py
│       │
│       ├── numerical/
│       │   ├── __init__.py
│       │   ├── integrators.py
│       │   ├── solvers.py
│       │   └── errors.py
│       │
│       ├── visualization/
│       │   ├── __init__.py
│       │   ├── pygame_renderer.py
│       │   ├── plots.py
│       │   └── controls.py
│       │
│       └── experiments/
│           ├── __init__.py
│           ├── projectile_motion.py
│           ├── free_fall.py
│           ├── spring_mass.py
│           └── orbital_motion.py
│
├── tests/
│   ├── test_vectors.py
│   ├── test_forces.py
│   └── test_integrators.py
│
├── data/
│   └── .gitkeep
│
├── docs/
│   └── physics_notes.md
│
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md