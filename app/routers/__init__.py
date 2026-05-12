"""
routers package - HTTP API endpoints

Each module here handles the HTTP endpoints (GET, POST, PUT, DELETE)
for its corresponding entity.
"""

from app.routers.customer_router import router as customer_router
from app.routers.product_router import router as product_router
from app.routers.productline_router import router as productline_router
from app.routers.office_router import router as office_router
from app.routers.employee_router import router as employee_router
from app.routers.order_router import router as order_router
from app.routers.orderdetail_router import router as orderdetail_router
from app.routers.payment_router import router as payment_router
