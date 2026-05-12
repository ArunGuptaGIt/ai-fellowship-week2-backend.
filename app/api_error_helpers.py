"""
api_error_helpers.py - Cleaner error handling across the API

Instead of writing the same error handling code in every route, we centralize it here.
This way if we want to change how errors look, we only change it in one place.
"""

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def not_found(entity: str, key) -> HTTPException:
    """Throw a 404 when someone asks for something that doesn't exist."""
    return HTTPException(status_code=404, detail=f"{entity} {key} not found")


def conflict(message: str) -> HTTPException:
    """Throw a 409 when there's a conflict - like trying to add a duplicate."""
    return HTTPException(status_code=409, detail=message)


def invalid_fk(field: str, value) -> HTTPException:
    """Throw a 422 when someone tries to reference a related record that doesn't exist.
    
    For example, if you try to create a product with a productLine that doesn't exist,
    this catches that and gives a clear error.
    """
    return HTTPException(status_code=422, detail=f"Invalid {field}: {value}")


def commit_or_raise(db, fk_message: str | None = None, conflict_message: str | None = None):
    """Try to save changes to the database, but handle constraint errors gracefully.
    
    SQLAlchemy will throw an IntegrityError if you violate foreign keys or unique 
    constraints. We catch that here and convert it to a proper HTTP error instead 
    of letting raw database errors bubble up to the user.
    """
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        message = str(exc.orig).lower()
        if "foreign key" in message or "violates foreign key" in message:
            raise HTTPException(status_code=422, detail=fk_message or "Foreign key constraint failed")
        if "unique" in message or "duplicate" in message:
            raise HTTPException(status_code=409, detail=conflict_message or "Duplicate record")
        raise HTTPException(status_code=400, detail=str(exc.orig))