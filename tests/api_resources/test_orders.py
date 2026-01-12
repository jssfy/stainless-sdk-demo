# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from python_demo import PythonDemo, AsyncPythonDemo
from tests.utils import assert_matches_type
from python_demo.types import Order, OrderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PythonDemo) -> None:
        order = client.orders.create(
            items=[
                {
                    "price": 0,
                    "product_id": "product_id",
                    "quantity": 1,
                }
            ],
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PythonDemo) -> None:
        response = client.orders.with_raw_response.create(
            items=[
                {
                    "price": 0,
                    "product_id": "product_id",
                    "quantity": 1,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PythonDemo) -> None:
        with client.orders.with_streaming_response.create(
            items=[
                {
                    "price": 0,
                    "product_id": "product_id",
                    "quantity": 1,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PythonDemo) -> None:
        order = client.orders.list()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PythonDemo) -> None:
        order = client.orders.list(
            page=0,
            status="pending",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PythonDemo) -> None:
        response = client.orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PythonDemo) -> None:
        with client.orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPythonDemo) -> None:
        order = await async_client.orders.create(
            items=[
                {
                    "price": 0,
                    "product_id": "product_id",
                    "quantity": 1,
                }
            ],
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.orders.with_raw_response.create(
            items=[
                {
                    "price": 0,
                    "product_id": "product_id",
                    "quantity": 1,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.orders.with_streaming_response.create(
            items=[
                {
                    "price": 0,
                    "product_id": "product_id",
                    "quantity": 1,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPythonDemo) -> None:
        order = await async_client.orders.list()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPythonDemo) -> None:
        order = await async_client.orders.list(
            page=0,
            status="pending",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True
