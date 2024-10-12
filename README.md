# Real Estate Price

Real estate price prediction app.

## HowTo

Pre-requisites: Docker.  
Trains the model, builds the frontend React app and runs everything: `make run`.  
Smoke test the API with `make test-api`.

## Architecture

There are two applications: [Python Backend](./api) and [React Frontend](./frontend).
Frontend also acts as a reverse proxy for the /api route.

### Backend

The backend app has two sub-modules: the [JSON REST API](./api/src/api.py) that's served by the FastAPI, and an [ML model training script](./api/src/train.py).
The training script is very coupled to the [sample dataset](./api/data/data.csv). The model is trained during docker build. See [Backend Dockerfile](./api/Dockerfile) for details.

### Frontend

Frontend is a simple Vite+React+TypeScript app, built during docker build (see [Frontend Dockerfile](./frontend/Dockerfile) for details) served by an nginx container (see [nginx config](./frontend/nginx.conf)).
Nginx also forwards all requests to /api route down to backend container.

## TODO

- Fix local dev environment to be able to submit form from frontend to backend container without messing with production setup.
