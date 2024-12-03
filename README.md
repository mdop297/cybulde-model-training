# Cyber bullying detection model training

## Project structure
```plaintext
.
├── docker
│   ├── Dockerfile
│   └── scripts
│       └── startup-script.sh
├── docker-compose.yaml
├── .dockerignore
├── .gitattributes
├── .gitignore
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── setup.cfg
└── src
    ├── configs
    │   ├── config.yaml
    │   ├── hydra
    │   │   └── job_logging
    │   │       └── custom.yaml
    │   └── __init__.py
    ├── config_schemas
    │   └── config_schema.py
    ├── entrypoint.py
    ├── __init__.py
    └── utils
        └── config_utils.py

```