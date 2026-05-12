# ai-fellowship-week2-backend

Built a FastAPI app with PostgreSQL running in Docker — covers database setup, ORM-based API endpoints, concurrent table stats using asyncio, and a full REST API for all tables.

---

## Tech Stack

- **FastAPI** — API framework
- **PostgreSQL** — Database
- **Docker & Docker Compose** — Containerization
- **SQLAlchemy** — ORM
- **Pydantic** — Data validation & schemas
- **asyncio** — Concurrent table statistics

---

## Project Structure

```
ai-fellowship-week2-backend/
├── app/
│   ├── crud/                      # Database query logic
│   │   ├── customer_crud.py
│   │   ├── employee_crud.py
│   │   ├── office_crud.py
│   │   ├── order_crud.py
│   │   ├── orderdetail_crud.py
│   │   ├── payment_crud.py
│   │   ├── product_crud.py
│   │   └── productline_crud.py
│   ├── routers/                   # Route handlers
│   │   ├── customer_router.py
│   │   ├── employee_router.py
│   │   ├── office_router.py
│   │   ├── order_router.py
│   │   ├── orderdetail_router.py
│   │   ├── payment_router.py
│   │   ├── product_router.py
│   │   └── productline_router.py
│   ├── schemas/                   # Pydantic models
│   │   ├── customer_schemas.py
│   │   ├── employee_schemas.py
│   │   ├── office_schemas.py
│   │   ├── order_schemas.py
│   │   ├── orderdetail_schemas.py
│   │   ├── payment_schemas.py
│   │   ├── product_schemas.py
│   │   └── productline_schemas.py
│   ├── database.py                # DB connection setup
│   ├── models.py                  # SQLAlchemy models
│   ├── router_counts.py           # Async stats endpoints
│   ├── logger.py                  # Logging setup
│   └── main.py                    # App entry point
├── docker-compose.yml
├── Dockerfile
├── seed.sql                       # DB initialization script
├── requirements.txt
└── .env
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ArunGuptaGIt/ai-fellowship-week2-backend.git
cd ai-fellowship-week2-backend
```

### 2. Create a `.env` file

Create a `.env` file in the root of the project. You can copy the template below and update the values to match your setup.

```env
# PostgreSQL credentials — change these to your own
POSTGRES_USER=your_username          # e.g. admin
POSTGRES_PASSWORD=your_password      # e.g. secret123
POSTGRES_DB=your_database_name       # e.g. classicmodels

# These stay the same when running with Docker Compose
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Built from the values above — update user, password, and db name to match
DATABASE_URL=postgresql://your_username:your_password@db:5432/your_database_name
```

Or copy-paste this example directly and update as needed:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=classicmodels
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://admin:admin123@db:5432/classicmodels
```

> **Note:** `.env` is listed in `.gitignore` and will not be committed. Never share your credentials publicly.

### 3. Run with Docker

```bash
docker compose up --build
```

This will:
- Start the PostgreSQL container
- Run `seed.sql` to create and populate the database
- Start the FastAPI server at `http://localhost:8000`

### 4. Access the API

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## API Endpoints

### Customers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/customers` | List all customers (paginated) |
| GET | `/customers/{id}` | Get customer with orders & payments |
| GET | `/customers/{id}/orders` | Get all orders for a customer |
| GET | `/customers/{id}/payments` | Get all payments for a customer |
| POST | `/customers` | Create a new customer |
| PUT | `/customers/{id}` | Update a customer |
| DELETE | `/customers/{id}` | Delete a customer |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | List all products (paginated) |
| GET | `/products/{productCode}` | Get a single product |
| GET | `/products/{productCode}/orderdetails` | Get product with its order line items |
| POST | `/products` | Create a new product |
| PUT | `/products/{productCode}` | Update a product |
| DELETE | `/products/{productCode}` | Delete a product |

### Product Lines
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/productlines` | List all product lines |
| GET | `/productlines/{productLine}` | Get a single product line |
| GET | `/productlines/{productLine}/products` | Get product line with all its products |
| POST | `/productlines` | Create a new product line |
| PUT | `/productlines/{productLine}` | Update a product line |
| DELETE | `/productlines/{productLine}` | Delete a product line |

### Offices
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/offices` | List all offices |
| GET | `/offices/{officeCode}` | Get a single office |
| GET | `/offices/{officeCode}/employees` | Get office with all its employees |
| POST | `/offices` | Create a new office |
| PUT | `/offices/{officeCode}` | Update an office |
| DELETE | `/offices/{officeCode}` | Delete an office |

### Employees
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | List all employees |
| GET | `/employees/{employeeNumber}` | Get a single employee |
| GET | `/employees/{employeeNumber}/customers` | Get employee with their managed customers |
| GET | `/employees/{employeeNumber}/reports` | Get all employees reporting to this employee |
| POST | `/employees` | Create a new employee |
| PUT | `/employees/{employeeNumber}` | Update an employee |
| DELETE | `/employees/{employeeNumber}` | Delete an employee |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/orders` | List all orders |
| GET | `/orders/{orderNumber}` | Get a single order |
| GET | `/orders/{orderNumber}/orderdetails` | Get order with all its line items |
| GET | `/orders/customer/{customerNumber}` | Get all orders for a customer |
| POST | `/orders` | Create a new order |
| PUT | `/orders/{orderNumber}` | Update an order |
| DELETE | `/orders/{orderNumber}` | Delete an order |

### Order Details
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/orderdetails` | List all order detail records |
| GET | `/orderdetails/{orderNumber}/{productCode}` | Get a single line item by composite key |
| GET | `/orderdetails/order/{orderNumber}` | Get all line items for an order |
| GET | `/orderdetails/product/{productCode}` | Get all orders containing a product |
| POST | `/orderdetails` | Add a new line item |
| PUT | `/orderdetails/{orderNumber}/{productCode}` | Update a line item |
| DELETE | `/orderdetails/{orderNumber}/{productCode}` | Remove a line item |

### Payments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/payments` | List all payments |
| GET | `/payments/{customerNumber}/{checkNumber}` | Get a single payment by composite key |
| GET | `/payments/customer/{customerNumber}` | Get all payments for a customer |
| POST | `/payments` | Record a new payment |
| PUT | `/payments/{customerNumber}/{checkNumber}` | Update a payment |
| DELETE | `/payments/{customerNumber}/{checkNumber}` | Delete a payment |

### Statistics (Async)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/overall_counts` | Record count from all tables concurrently |
| GET | `/{table}/count` | Record count for a specific table |

---

## Tasks Breakdown

| Task | Description |
|------|-------------|
| Task 1 | PostgreSQL setup with Docker Compose + `seed.sql` initialization |
| Task 2 | FastAPI CRUD endpoints for customers using SQLAlchemy ORM & Pydantic |
| Task 3 | Async aggregated stats across all 8 tables using `asyncio.gather` |
| Task 4 | Full REST API for all tables — Products, ProductLines, Offices, Employees, Orders, OrderDetails, Payments — following the same 4-layer architecture |

---

## Notes

- Make sure Docker is running before starting
- The `seed.sql` file auto-initializes the database on first run
- All environment variables are configured via `.env`
- API logs are handled via a custom logger in `app/logger.py`
