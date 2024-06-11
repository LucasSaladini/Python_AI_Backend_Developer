import pytest
from uuid import UUID
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase
from typing import List

async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "iPhone 14 Pro Max"

async def test_usecases_get_should_return_success(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "iPhone 14 Pro Max"

async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("5090b054-a458-46ac-8a83-c46f3388cc24"))

    assert err.value.message == "Product not found with filter: 5090b054-a458-46ac-8a83-c46f3388cc24"

async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)

async def test_usecases_update_should_return_success(product_id, product_up):
    product_up.price = 7.500
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)