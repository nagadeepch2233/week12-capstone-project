# API Documentation

## Base URL
''
## Endpoints

### `GET /`
- **Description:** API health check
- **Response:** `{ "message": "Portfolio API is running 🚀" }`

### `POST /add`
- **Description:** Add a portfolio entry
- **Request Body:**
```json
{
  "category": "SKILL",
  "content": "Python Async"
}
