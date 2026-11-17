# Car Bond Management System

A Django application for managing vehicle brands, models, cars, specifications,
customers, employees, sales, and payments.

## Group Members

- Mariam Isa Ssegujja -'224-063011-29324'
- Nakitende Baayat - '224-063011-30080'
- Sserwadda Safina - '224-063011-28162'
- Ramzan Musa Mutebi - '124-063011-35226'

## Render deployment

Use `build.sh` as the Render build command; the root `Procfile` defines the
Gunicorn start command. Configure these environment variables in Render:

- `SECRET_KEY`: a long, randomly generated secret.
- `DATABASE_URL`: the Render PostgreSQL connection URL. SQLite is used only
  when this variable is not set (for local development).
- `ADMIN_USERNAME`, `ADMIN_EMAIL`, and `ADMIN_PASSWORD`: credentials for the
  deployment superuser.
- `DEBUG`: set to `False` or leave unset.

