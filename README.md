# PROJECT NAME
This is a standalone container that accepts http queries to `PURPOSE`. 

# Running
To start the container, the easiest way is to
1. Navigate to the repository root
2. run `docker compose up`.

## Running only on python flask
You can run `python app/app.py` to get the Flask app running
- This will require you to have installed dependencies
- All dependencies other than Python itself are listed under `requirements.txt`

## Running as a standalone container using Dockerfile provided
If you want to run the container by itself, you can find the Dockerfile at `app/Dockerfile`
1. Run `cd app` at the repository root to enter the `/app` folder
2. Run `docker build .`. This creates the docker image
    1. You are recommended to tag your images in the format of `docker build -t *you_username*/dommons:*version_no* .` for maintainability 
3. (Optional) Run `docker push *you_username*/dommons:*version_no*` to publish to your Dockerhub

## Running as part of your existing Docker Compose set up
1. Copy over the repo files
2. You may rename "app" directory to a more descriptive name. We will call this `yourAppRoot` below
3. Under `services` in your docker compose configuration, include this indented block:

```yaml
dommons_webTempl: 
    build:
      context: app
      target: runner
    ports: 
      - '8000:8000' 
    environment:
      - FLASK_RUN_PORT=8000
      - FLASK_RUN_HOST=0.0.0.0
```

# Modifying
You can find app-wide variables in `app/config.py`. This includes 

# Core function

# Examples

# Licensing 
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.