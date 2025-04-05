# ConfMan - Remote `.env` & Secrets Manager

A secure, version-controlled environment configuration manager for development teams. ConfMan helps you manage `.env` files across different environments with encryption, version control, and team access management.

## 🚀 Features

- Git-style CLI for managing environment configs
- Per-environment secrets (dev, staging, prod)
- Version control and rollback capability
- Team access control
- End-to-end encryption
- REST API
- Web dashboard
- GitHub integration

## 🛠️ Tech Stack

- Backend: Django + Django REST Framework
- CLI: Go
- Database: SQLite (development) / PostgreSQL (production)
- Authentication: GitHub OAuth

## 🏁 Getting Started

### Prerequisites

- Python 3.8+
- Go 1.18+
- Virtual environment tool (venv)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/icichainz/confman.git
cd confman
```

2. Set up Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

### CLI Tool Installation

From the `envctl` directory:
```bash
go build
go install
```

## 📚 API Documentation

The API endpoints are available at `/api/` and include:

- `GET/POST /api/projects/`
- `GET/POST /api/environments/`
- `GET/POST /api/secrets/`

## 🔒 Security

- End-to-end encryption for all secrets
- Token-based authentication for API access
- Role-based access control

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🛣️ Roadmap

See our [roadmap](docs/roadmap.md) for planned features and improvements.

## 👥 Team

- [Abel Koudaya] - Initial work - [https://github.com/icichainz/confman]

## 🙏 Acknowledgments

- Inspired by the need for better secrets management in development teams
- Built with Django and Go
