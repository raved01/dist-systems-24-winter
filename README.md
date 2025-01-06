# dist-systems-24-winter
## Lab repository of the lecture "Parallele und verteilte Systeme", Hochschule Esslingen, WS24/25

### Project Overview
A REST API for a Shopping List application, implemented with Django and deployed in Kubernetes. The application enables Creating, Reading, Updating, and Deleting of shopping items.
The application is adhering to core principles of distributed systems and cloud-native development applying the 12-factor methodology.

### System Architecture
- **Backend**: Django REST Framework
- **Database**: PostgreSQL
- **Container**: Docker
- **Orchestration**: Kubernetes
- **Components**:
 - Django Backend Service (4 Replicas)
 - PostgreSQL Database
 - Persistent Volume for data storage

### Docker Image:
The public Docker image is available on DockerHub: `https://hub.docker.com/repository/docker/raved02/shopping-list-api/general`
### API Endpoints
- `GET /shopping`: List all shopping items
- `POST /shopping`: Create new item
- `GET /shopping/<name>`: Get item details
- `PUT /shopping/<name>`: Update item
- `DELETE /shopping/<name>`: Delete item

### Installation
#### 1. Prerequisites:
  - Docker Desktop
  - Kubernetes (Minikube)
  - kubectl
#### 2. Docker setup instructions
Build and start containers:
```
docker-compose up --build
```
Verify if containers are running:
```
docker-compose ps
```
#### 3. Access the application:
- Backend API: `http://localhost:80/shopping`
- Frontend: `http://localhost:80/shopping`
#### 4. Kubernetes Deployment:
Start Minikube
```
minikube start
```
Build Docker Image
```
eval $(minikube docker-env)
docker build -t django-backend:latest .
```
Kubernetes Deployment
```
kubectl apply -f postgres-pvc.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
#### 5. CORS Configuration
The application is configured to allow cross-origin requests (CORS) using `django-cors-headers`:
```
#Installation
pip install django-cors-headers
```

### Usage
1. Enable port forwarding:
```
kubectl port-forward service/django-service 8000:80
```
2. Test API:
```
# List all items
curl http://localhost:8000/shopping

# Create new item
curl -X POST http://localhost:8000/shopping \
     -H "Content-Type: application/json" \
     -d '{"name": "Apple", "amount": 5}'

# Get specific item
curl http://localhost:8000/shopping/Apple

# Update item
curl -X PUT http://localhost:8000/shopping/Apple \
     -H "Content-Type: application/json" \
     -d '{"amount": 10}'

# Delete item
curl -X DELETE http://localhost:8000/shopping/Apple
```
### API Documentation
The API is documented using Swagger/OpenAPI. After running the application, you can access:

- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc UI: `http://localhost:8000/redoc/`
- Raw OpenAPI Schema: `http://localhost:8000/swagger.json`

#### Testing with Swagger UI
1. Navigate to `http://localhost:8000/swagger/`
2. The UI provides:
   - Detailed API documentation
   - Request/response schemas
   - Interactive API testing interface
   - Model definitions
#### Testing
1. API Tests:
- Use curl commands as shown in Usage section
- Test all CRUD operations

2. Database tests:
```
# Connect to PostgreSQL
kubectl exec -it $(kubectl get pod -l app=postgres -o jsonpath='{.items[0].metadata.name}') -- psql -U postgres database

#View tables
\dt

# View data
SELECT * FROM app1_shoppingitem;
```
## 12-Factor App Principles: Implementation in Shopping List API

### I. Codebase
- One codebase tracked in Git
- Same code deployed to Kubernetes cluster
- Django application with clear repository structure

### II. Dependencies
- Dependencies explicitly declared in `requirements.txt`
- Isolated dependencies through Docker container
- Example:
 ```txt
 Django>=4.0,<5.0
 djangorestframework
 psycopg2-binary
 drf-yasg
```
### III. Config

- Configuration stored in environment variables
- Kubernetes ConfigMaps and Secrets for sensitive data
- Database credentials and connection settings externalized

### IV. Backing Services

- PostgreSQL database treated as attached resource
- Database connection configured via environment variables
- Easy to switch database service through Kubernetes configuration

### V. Build, Release, Run

- Build: Docker image creation
- Release: Kubernetes deployment configuration
- Run: Container execution in Kubernetes cluster
- Clear separation of stages in deployment process

### VI. Processes

- Application runs as stateless process
- Data persistence handled by PostgreSQL database
- No shared state between Django instances

### VII. Port Binding

- Service self-contained with port binding
- Exposed through Kubernetes Service on port 80
- Port forwarding for local development

### VIII. Concurrency

- Horizontal scaling through Kubernetes
- Multiple Django replicas (4 by default)
- Load balanced through Kubernetes Service

### IX. Disposability

- Fast startup through lightweight Django configuration
- Graceful shutdown handling
- Kubernetes handles pod lifecycle

### X. Dev/Prod Parity

- Same Docker container in all environments
- Environment differences only in configuration
- Consistent database setup across environments

### XI. Logs

- Logs treated as event streams
- Accessible through Kubernetes logging
- Command example:
```
#Get pods:
kubectl get pods

#Get logs:
kubectl logs <pod-name>
```

### XII. Admin Processes
#### Database management
- Database migrations run as one-off processes
- Admin tasks executed through Kubernetes Jobs
- Migration command:
```
kubectl exec -it <pod-name> -- python manage.py migrate
```
### Useful commands
#### Docker
Stop containers:
```
docker-compose down
```
View logs:
```
# All containers
docker-compose logs

# Specific container
docker-compose logs backend
docker-compose logs db
```
Access containers:
```
# Django backend
docker exec -it backend bash

# Database
docker exec -it db psql -U postgres database
```
Container managemenr:
```
# List running containers
docker-compose ps

# Restart specific service
docker-compose restart backend

# Remove containers and volumes
docker-compose down -v
```

#### Project structure
```
project/
├── backend/
│   ├── app1/
│   │   ├── models.py      
│   │   ├── serializers.py 
│   │   ├── views.py       
│   │   └── urls.py        
│   ├── dysSysLab/
│   │   ├── asgi.py      
│   │   ├── settings.py 
│   │   ├── urls.py       
│   │   └── wsgi.py 
│   ├── manage.py
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   └── postgres-pvc.yaml
├── Dockerfile
└── docker-compose.yml
```
