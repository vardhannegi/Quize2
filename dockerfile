# Dockerfile

FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install uv globally
RUN pip install uv

# Copy pyproject.toml and uv.lock for dependency sync
COPY pyproject.toml uv.lock /code/

# Create uv environment in /code/.venv
RUN uv venv /code/.venv

# Activate uv environment and sync dependencies
RUN . /code/.venv/bin/activate && uv sync

# Copy project files
COPY . /code/

# Expose port
EXPOSE 8000

# Activate environment and run Django commands
CMD ["sh", "-c", ". /code/.venv/bin/activate && uv run python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
