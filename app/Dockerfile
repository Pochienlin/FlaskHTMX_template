FROM python:3.10-alpine as runner

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
    
COPY . /app

# Default command if not overridden by docker-compose
CMD  ["python3", "-m", "flask", "run", "--host=0.0.0.0"]