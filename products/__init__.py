from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["products"])


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str | None = None


class Product(ProductCreate):
    id: int


products: list[Product] = [
    Product(
        id=1,
        name="Sample Product",
        price=19.99,
        description="Example product returned by the products API.",
    ),
    Product(
        id=2,
        name="Hardcover Journal",
        price=12.5,
        description="A lined journal with a durable cover.",
    ),
    Product(
        id=3,
        name="Ceramic Mug",
        price=8.75,
        description="A reusable mug for hot drinks.",
    ),
    Product(
        id=4,
        name="Desk Lamp",
        price=34.99,
        description="An adjustable LED lamp for a desk.",
    ),
]


@router.post("", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate) -> Product:
    created_product = Product(id=len(products) + 1, **product.model_dump())
    products.append(created_product)
    return created_product


@router.get("", response_model=list[Product])
async def list_products() -> list[Product]:
    return products