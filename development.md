```markdown id="7nq3ls"
# Development Setup

## Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
