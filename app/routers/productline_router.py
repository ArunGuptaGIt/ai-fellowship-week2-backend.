"""
productline_router.py - Product category API endpoints

Handle product categories/lines. Can view, create, update, and delete categories.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.productline_schemas import ProductLineCreate, ProductLineOut, ProductLineUpdate, ProductLineWithProductsOut
from app.crud import productline_crud as crud
from app.logger import get_logger

logger = get_logger(__name__)
router = APIRouter(tags=["ProductLines"])


@router.get("/", response_model=list[ProductLineOut])
def list_productlines(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100), db: Session = Depends(get_db)):
    """Page through all product categories."""
    return crud.get_productlines(db, skip=skip, limit=limit)


@router.get("/{productLine}", response_model=ProductLineOut)
def get_productline(productLine: str, db: Session = Depends(get_db)):
    """Get details about a product category."""
    return crud.get_productline(db, productLine)


@router.get("/{productLine}/products", response_model=ProductLineWithProductsOut)
def get_productline_products(productLine: str, db: Session = Depends(get_db)):
    """See all products in a category."""
    return crud.get_productlines_with_products(db, productLine)


@router.post("/", response_model=ProductLineOut, status_code=201)
def create_productline(data: ProductLineCreate, db: Session = Depends(get_db)):
    """Create a new product category."""
    return crud.create_productline(db, data)


@router.put("/{productLine}", response_model=ProductLineOut)
def update_productline(productLine: str, data: ProductLineUpdate, db: Session = Depends(get_db)):
    """Update a product category."""
    return crud.update_productline(db, productLine, data)


@router.delete("/{productLine}")
def delete_productline(productLine: str, db: Session = Depends(get_db)):
    """Delete a product category."""
    crud.delete_productline(db, productLine)
    return {"detail": f"ProductLine {productLine} deleted successfully"}
