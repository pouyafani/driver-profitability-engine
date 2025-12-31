# Driver Profitability Engine

An AI-driven decision intelligence engine for optimizing driver-level profitability in transportation and logistics operations.

## Architecture

This project follows **Clean Architecture** principles with **DDD-Lite** patterns.

### Project Structure

```
src/
├── domain/          # Core business logic (framework-agnostic)
├── application/     # Use cases and orchestration
├── infrastructure/  # Technical implementations (DB, AI, etc.)
├── interfaces/     # External communication (API, CLI, webhooks)
├── shared/          # Shared utilities and cross-cutting concerns
└── bootstrap/       # Application startup and DI container
```

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python -m src.bootstrap.main
```

## Development

This project uses:
- Python 3.12+
- Clean Architecture + DDD-Lite
- Type hints (mandatory)
- Explicit over implicit

