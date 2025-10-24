# ChronoSpace

ChronoSpace is an interactive 3D platform for visualizing historical events along a timeline. This application allows you to create, manage, and visualize historical events in an immersive 3D environment.

## Features

- **3D Timeline Visualization**: Interactive timeline with smooth camera controls and event highlighting
- **Event Management**: Full CRUD operations for historical events
- **Categorization**: Group events by categories and epochs
- **Filtering**: Filter events by date range, categories, and epochs
- **Responsive Design**: Works on desktop and mobile devices with dark mode support
- **Real-time Updates**: Instant visualization updates when data changes

## Tech Stack

### Backend

- FastAPI (async web framework)
- SQLAlchemy (async ORM)
- Alembic (database migrations)
- PostgreSQL (production) / SQLite (testing)
- Pydantic v2 (data validation)

### Frontend

- React 18 with Vite
- Three.js with React Three Fiber
- Framer Motion for animations
- TailwindCSS for styling
- Axios for API communication

## Development Setup

### Quick Start with Make

```bash
# Install and run backend
make install-backend
make run-backend

# In another terminal, install and run frontend
make install-frontend
make run-frontend
```

### Manual Setup

1. Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r app/req.txt
cd app
uvicorn app_main:app --reload --port 8000
```

2. Frontend

```bash
cd frontend
npm install
npm run dev
```

## Database Configuration

- **Development**: Uses PostgreSQL by default
- **Testing**: Automatically switches to SQLite
- **Production**: Configure using environment variables

Environment variables (`.env` or system environment):

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=chronospace
POSTGRES_PORT=5432
```

## API Endpoints

All endpoints are prefixed with `/api/v1`

### Events

- `GET /events` - List events (supports filtering)
- `POST /events` - Create event
- `GET /events/{id}` - Get event details
- `DELETE /events/{id}` - Delete event

### Categories

- `GET /categories` - List categories
- `POST /categories` - Create category
- `GET /categories/{id}` - Get category details
- `DELETE /categories/{id}` - Delete category

### Epochs

- `GET /epochs` - List epochs
- `POST /epochs` - Create epoch
- `GET /epochs/{id}` - Get epoch details
- `DELETE /epochs/{id}` - Delete epoch

## Testing

```bash
# Run backend tests (uses SQLite)
make test-backend

# Run frontend tests
cd frontend && npm test
```

## CI/CD

- GitHub Actions workflow runs tests and builds
- Configured for deployment to:
  - Backend: Render/Railway (see `Procfile`)
  - Frontend: Vercel (automatic from `main` branch)

## Development Notes

- Backend uses `app_main.py` as the clean entrypoint
- Package structure follows FastAPI best practices
- Async SQLAlchemy for better performance
- Testing uses SQLite for speed and simplicity
- Environment-based configuration for flexibility

## Docker Support

Use `docker-compose` for full stack development:

```bash
docker-compose up
```

This starts:

- PostgreSQL database
- FastAPI backend on port 8000
- React frontend on port 5173

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request
