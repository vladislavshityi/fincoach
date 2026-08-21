# FinCoach

Personal finance tracker API built with FastAPI, SQLModel and SQLite.

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- uv

## Current Features

- Create transactions
- Get all transactions
- Get transaction by ID
- Update transactions
- Delete transactions

## Roadmap

### Transaction Management
- [x] Basic transaction CRUD
- [ ] Transaction categories
- [ ] Income and expense types
- [ ] Transaction filtering
- [ ] Transaction sorting
- [ ] Pagination

### Financial Analytics
- [ ] Calculate total income
- [ ] Calculate total expenses
- [ ] Calculate current balance
- [ ] Spending statistics by category
- [ ] Monthly financial summaries
- [ ] Spending trends

### Budgeting
- [ ] Create monthly budgets
- [ ] Set spending limits by category
- [ ] Track budget usage
- [ ] Budget warnings when approaching limits

### User Management
- [ ] User registration
- [ ] Authentication
- [ ] User-specific transactions
- [ ] User-specific budgets and statistics

### AI Financial Assistant
- [ ] Analyze user's spending habits
- [ ] Generate personalized financial insights
- [ ] Answer questions about personal finances
- [ ] Suggest ways to reduce unnecessary spending
- [ ] Generate monthly financial reports
- [ ] AI-powered financial recommendations

### Engineering
- [ ] Unit tests
- [ ] API integration tests
- [ ] Database migrations
- [ ] Environment configuration
- [ ] Docker
- [ ] CI/CD
- [ ] API documentation

## Run locally

```bash
uv sync
uv run fastapi dev app/main.py