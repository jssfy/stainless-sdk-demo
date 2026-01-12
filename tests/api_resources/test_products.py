# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from python_demo import PythonDemo, AsyncPythonDemo
from tests.utils import assert_matches_type
from python_demo.types import Product, ProductListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PythonDemo) -> None:
        product = client.products.create(
            name="name",
            price=0,
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PythonDemo) -> None:
        product = client.products.create(
            name="name",
            price=0,
            category="category",
            currency="currency",
            description="description",
            stock=0,
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PythonDemo) -> None:
        response = client.products.with_raw_response.create(
            name="name",
            price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PythonDemo) -> None:
        with client.products.with_streaming_response.create(
            name="name",
            price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PythonDemo) -> None:
        product = client.products.retrieve(
            "id",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PythonDemo) -> None:
        response = client.products.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PythonDemo) -> None:
        with client.products.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.products.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PythonDemo) -> None:
        product = client.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PythonDemo) -> None:
        product = client.products.list(
            category="category",
            page=0,
            per_page=0,
            search="search",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PythonDemo) -> None:
        response = client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PythonDemo) -> None:
        with client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPythonDemo) -> None:
        product = await async_client.products.create(
            name="name",
            price=0,
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPythonDemo) -> None:
        product = await async_client.products.create(
            name="name",
            price=0,
            category="category",
            currency="currency",
            description="description",
            stock=0,
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.products.with_raw_response.create(
            name="name",
            price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.products.with_streaming_response.create(
            name="name",
            price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPythonDemo) -> None:
        product = await async_client.products.retrieve(
            "id",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.products.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.products.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.products.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPythonDemo) -> None:
        product = await async_client.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPythonDemo) -> None:
        product = await async_client.products.list(
            category="category",
            page=0,
            per_page=0,
            search="search",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True
