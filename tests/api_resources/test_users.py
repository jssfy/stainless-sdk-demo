# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from python_demo import PythonDemo, AsyncPythonDemo
from tests.utils import assert_matches_type
from python_demo.types import User, UserListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PythonDemo) -> None:
        user = client.users.create(
            email="newuser@example.com",
            name="新用户",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PythonDemo) -> None:
        user = client.users.create(
            email="newuser@example.com",
            name="新用户",
            avatar_url="https://example.com",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PythonDemo) -> None:
        response = client.users.with_raw_response.create(
            email="newuser@example.com",
            name="新用户",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PythonDemo) -> None:
        with client.users.with_streaming_response.create(
            email="newuser@example.com",
            name="新用户",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PythonDemo) -> None:
        user = client.users.retrieve(
            "id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PythonDemo) -> None:
        response = client.users.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PythonDemo) -> None:
        with client.users.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: PythonDemo) -> None:
        user = client.users.update(
            id="id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PythonDemo) -> None:
        user = client.users.update(
            id="id",
            avatar_url="https://example.com",
            email="dev@stainless.com",
            name="name",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PythonDemo) -> None:
        response = client.users.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PythonDemo) -> None:
        with client.users.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PythonDemo) -> None:
        user = client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PythonDemo) -> None:
        user = client.users.list(
            email="email",
            page=1,
            per_page=1,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PythonDemo) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PythonDemo) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PythonDemo) -> None:
        user = client.users.delete(
            "id",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PythonDemo) -> None:
        response = client.users.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PythonDemo) -> None:
        with client.users.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.create(
            email="newuser@example.com",
            name="新用户",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.create(
            email="newuser@example.com",
            name="新用户",
            avatar_url="https://example.com",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.users.with_raw_response.create(
            email="newuser@example.com",
            name="新用户",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.users.with_streaming_response.create(
            email="newuser@example.com",
            name="新用户",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.retrieve(
            "id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.users.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.update(
            id="id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.update(
            id="id",
            avatar_url="https://example.com",
            email="dev@stainless.com",
            name="name",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.users.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.users.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.list(
            email="email",
            page=1,
            per_page=1,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPythonDemo) -> None:
        user = await async_client.users.delete(
            "id",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPythonDemo) -> None:
        response = await async_client.users.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPythonDemo) -> None:
        async with async_client.users.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPythonDemo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )
