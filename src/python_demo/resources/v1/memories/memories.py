# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import memory_list_params, memory_create_params, memory_delete_params, memory_search_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .conversation_meta import (
    ConversationMetaResource,
    AsyncConversationMetaResource,
    ConversationMetaResourceWithRawResponse,
    AsyncConversationMetaResourceWithRawResponse,
    ConversationMetaResourceWithStreamingResponse,
    AsyncConversationMetaResourceWithStreamingResponse,
)
from ....types.v1.memory_list_response import MemoryListResponse
from ....types.v1.memory_create_response import MemoryCreateResponse
from ....types.v1.memory_delete_response import MemoryDeleteResponse
from ....types.v1.memory_search_response import MemorySearchResponse

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
    @cached_property
    def conversation_meta(self) -> ConversationMetaResource:
        return ConversationMetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jssfy/stainless-sdk-demo#accessing-raw-response-data-eg-headers
        """
        return MemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jssfy/stainless-sdk-demo#with_streaming_response
        """
        return MemoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        create_time: str,
        message_id: str,
        sender: str,
        group_id: Optional[str] | Omit = omit,
        group_name: Optional[str] | Omit = omit,
        refer_list: Optional[SequenceNotStr[str]] | Omit = omit,
        role: Optional[str] | Omit = omit,
        sender_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateResponse:
        """
        Store a single message into memory.

        Args:
          content: Message content

          create_time: Message creation time (ISO 8601 format)

          message_id: Message unique identifier

          sender: Sender user ID

          group_id: Group ID

          group_name: Group name

          refer_list: List of referenced message IDs

          role: Message sender role, used to identify the source of the message. Enum values
              from MessageSenderRole:

              - user: Message from a human user
              - assistant: Message from an AI assistant

          sender_name: Sender name (uses sender if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories",
            body=maybe_transform(
                {
                    "content": content,
                    "create_time": create_time,
                    "message_id": message_id,
                    "sender": sender,
                    "group_id": group_id,
                    "group_name": group_name,
                    "refer_list": refer_list,
                    "role": role,
                    "sender_name": sender_name,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryCreateResponse,
        )

    def list(
        self,
        *,
        end_time: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        memory_type: Optional[Literal["profile", "episodic_memory", "foresight", "event_log"]] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        start_time: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryListResponse:
        """
        Retrieve memory records by memory_type with optional filters

        Args:
          end_time: End time for time range filtering (ISO 8601 format)

          group_id: Group ID

          limit: Maximum number of memories to return

          memory_type:
              Memory type, enum values from MemoryType:

              - profile: user profile
              - episodic_memory: episodic memory (default)
              - foresight: prospective memory
              - event_log: event log (atomic facts)

          offset: Pagination offset

          start_time: Start time for time range filtering (ISO 8601 format)

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/memories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "group_id": group_id,
                        "limit": limit,
                        "memory_type": memory_type,
                        "offset": offset,
                        "start_time": start_time,
                        "user_id": user_id,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            cast_to=MemoryListResponse,
        )

    def delete(
        self,
        *,
        event_id: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete memory records based on combined filter criteria

                ## Functionality:
                - Delete records matching combined filter conditions
                - If multiple conditions provided, ALL must be satisfied (AND logic)
                - At least one filter must be specified

                ## Filter Parameters (combined with AND):
                - **event_id**: Filter by specific event_id
                - **user_id**: Filter by user ID
                - **group_id**: Filter by group ID

                ## Examples:
                - event_id only: Delete specific memory
                - user_id only: Delete all user's memories
                - user_id + group_id: Delete user's memories in specific group
                - event_id + user_id + group_id: Delete if all conditions match

                ## Use cases:
                - User requests data deletion
                - Group chat cleanup
                - Privacy compliance (GDPR, etc.)
                - Conversation history management

        Args:
          event_id: Memory event_id (filter condition)

          group_id: Group ID (filter condition)

          user_id: User ID (filter condition)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/v1/memories",
            body=maybe_transform(
                {
                    "event_id": event_id,
                    "group_id": group_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryDeleteResponse,
        )

    def search(
        self,
        *,
        current_time: Optional[str] | Omit = omit,
        end_time: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        include_metadata: bool | Omit = omit,
        memory_types: Optional[List[Literal["profile", "episodic_memory", "foresight", "event_log"]]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        retrieve_method: Literal["keyword", "vector", "hybrid", "rrf", "agentic"] | Omit = omit,
        start_time: Optional[str] | Omit = omit,
        top_k: int | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Retrieve relevant memory data based on query text using multiple retrieval
        methods

        Args:
          current_time: Current time, used to filter forward-looking events within validity period

          end_time: Time range end (ISO 8601 format)

          group_id: Group ID (at least one of user_id or group_id must be provided)

          include_metadata: Whether to include metadata

          memory_types:
              List of memory types to retrieve, enum values from MemoryType:

              - episodic_memory: episodic memory
              - foresight: prospective memory
              - event_log: event log (atomic facts) Note: profile type is not supported in
                search interface

          query: Search query text

          radius: COSINE similarity threshold for vector retrieval (only for vector and hybrid
              methods, default 0.6)

          retrieve_method:
              Retrieval method, enum values from RetrieveMethod:

              - keyword: keyword retrieval (BM25, default)
              - vector: vector semantic retrieval
              - hybrid: hybrid retrieval (keyword + vector)
              - rrf: RRF fusion retrieval (keyword + vector + RRF ranking fusion)
              - agentic: LLM-guided multi-round intelligent retrieval

          start_time: Time range start (ISO 8601 format)

          top_k: Maximum number of results to return

          user_id: User ID (at least one of user_id or group_id must be provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/memories/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "current_time": current_time,
                        "end_time": end_time,
                        "group_id": group_id,
                        "include_metadata": include_metadata,
                        "memory_types": memory_types,
                        "query": query,
                        "radius": radius,
                        "retrieve_method": retrieve_method,
                        "start_time": start_time,
                        "top_k": top_k,
                        "user_id": user_id,
                    },
                    memory_search_params.MemorySearchParams,
                ),
            ),
            cast_to=MemorySearchResponse,
        )


class AsyncMemoriesResource(AsyncAPIResource):
    @cached_property
    def conversation_meta(self) -> AsyncConversationMetaResource:
        return AsyncConversationMetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jssfy/stainless-sdk-demo#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jssfy/stainless-sdk-demo#with_streaming_response
        """
        return AsyncMemoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        create_time: str,
        message_id: str,
        sender: str,
        group_id: Optional[str] | Omit = omit,
        group_name: Optional[str] | Omit = omit,
        refer_list: Optional[SequenceNotStr[str]] | Omit = omit,
        role: Optional[str] | Omit = omit,
        sender_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateResponse:
        """
        Store a single message into memory.

        Args:
          content: Message content

          create_time: Message creation time (ISO 8601 format)

          message_id: Message unique identifier

          sender: Sender user ID

          group_id: Group ID

          group_name: Group name

          refer_list: List of referenced message IDs

          role: Message sender role, used to identify the source of the message. Enum values
              from MessageSenderRole:

              - user: Message from a human user
              - assistant: Message from an AI assistant

          sender_name: Sender name (uses sender if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "create_time": create_time,
                    "message_id": message_id,
                    "sender": sender,
                    "group_id": group_id,
                    "group_name": group_name,
                    "refer_list": refer_list,
                    "role": role,
                    "sender_name": sender_name,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryCreateResponse,
        )

    async def list(
        self,
        *,
        end_time: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        memory_type: Optional[Literal["profile", "episodic_memory", "foresight", "event_log"]] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        start_time: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryListResponse:
        """
        Retrieve memory records by memory_type with optional filters

        Args:
          end_time: End time for time range filtering (ISO 8601 format)

          group_id: Group ID

          limit: Maximum number of memories to return

          memory_type:
              Memory type, enum values from MemoryType:

              - profile: user profile
              - episodic_memory: episodic memory (default)
              - foresight: prospective memory
              - event_log: event log (atomic facts)

          offset: Pagination offset

          start_time: Start time for time range filtering (ISO 8601 format)

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/memories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "group_id": group_id,
                        "limit": limit,
                        "memory_type": memory_type,
                        "offset": offset,
                        "start_time": start_time,
                        "user_id": user_id,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            cast_to=MemoryListResponse,
        )

    async def delete(
        self,
        *,
        event_id: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete memory records based on combined filter criteria

                ## Functionality:
                - Delete records matching combined filter conditions
                - If multiple conditions provided, ALL must be satisfied (AND logic)
                - At least one filter must be specified

                ## Filter Parameters (combined with AND):
                - **event_id**: Filter by specific event_id
                - **user_id**: Filter by user ID
                - **group_id**: Filter by group ID

                ## Examples:
                - event_id only: Delete specific memory
                - user_id only: Delete all user's memories
                - user_id + group_id: Delete user's memories in specific group
                - event_id + user_id + group_id: Delete if all conditions match

                ## Use cases:
                - User requests data deletion
                - Group chat cleanup
                - Privacy compliance (GDPR, etc.)
                - Conversation history management

        Args:
          event_id: Memory event_id (filter condition)

          group_id: Group ID (filter condition)

          user_id: User ID (filter condition)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/v1/memories",
            body=await async_maybe_transform(
                {
                    "event_id": event_id,
                    "group_id": group_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryDeleteResponse,
        )

    async def search(
        self,
        *,
        current_time: Optional[str] | Omit = omit,
        end_time: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        include_metadata: bool | Omit = omit,
        memory_types: Optional[List[Literal["profile", "episodic_memory", "foresight", "event_log"]]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        retrieve_method: Literal["keyword", "vector", "hybrid", "rrf", "agentic"] | Omit = omit,
        start_time: Optional[str] | Omit = omit,
        top_k: int | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Retrieve relevant memory data based on query text using multiple retrieval
        methods

        Args:
          current_time: Current time, used to filter forward-looking events within validity period

          end_time: Time range end (ISO 8601 format)

          group_id: Group ID (at least one of user_id or group_id must be provided)

          include_metadata: Whether to include metadata

          memory_types:
              List of memory types to retrieve, enum values from MemoryType:

              - episodic_memory: episodic memory
              - foresight: prospective memory
              - event_log: event log (atomic facts) Note: profile type is not supported in
                search interface

          query: Search query text

          radius: COSINE similarity threshold for vector retrieval (only for vector and hybrid
              methods, default 0.6)

          retrieve_method:
              Retrieval method, enum values from RetrieveMethod:

              - keyword: keyword retrieval (BM25, default)
              - vector: vector semantic retrieval
              - hybrid: hybrid retrieval (keyword + vector)
              - rrf: RRF fusion retrieval (keyword + vector + RRF ranking fusion)
              - agentic: LLM-guided multi-round intelligent retrieval

          start_time: Time range start (ISO 8601 format)

          top_k: Maximum number of results to return

          user_id: User ID (at least one of user_id or group_id must be provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/memories/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "current_time": current_time,
                        "end_time": end_time,
                        "group_id": group_id,
                        "include_metadata": include_metadata,
                        "memory_types": memory_types,
                        "query": query,
                        "radius": radius,
                        "retrieve_method": retrieve_method,
                        "start_time": start_time,
                        "top_k": top_k,
                        "user_id": user_id,
                    },
                    memory_search_params.MemorySearchParams,
                ),
            ),
            cast_to=MemorySearchResponse,
        )


class MemoriesResourceWithRawResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_raw_response_wrapper(
            memories.create,
        )
        self.list = to_raw_response_wrapper(
            memories.list,
        )
        self.delete = to_raw_response_wrapper(
            memories.delete,
        )
        self.search = to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> ConversationMetaResourceWithRawResponse:
        return ConversationMetaResourceWithRawResponse(self._memories.conversation_meta)


class AsyncMemoriesResourceWithRawResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_raw_response_wrapper(
            memories.create,
        )
        self.list = async_to_raw_response_wrapper(
            memories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            memories.delete,
        )
        self.search = async_to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> AsyncConversationMetaResourceWithRawResponse:
        return AsyncConversationMetaResourceWithRawResponse(self._memories.conversation_meta)


class MemoriesResourceWithStreamingResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_streamed_response_wrapper(
            memories.create,
        )
        self.list = to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = to_streamed_response_wrapper(
            memories.delete,
        )
        self.search = to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> ConversationMetaResourceWithStreamingResponse:
        return ConversationMetaResourceWithStreamingResponse(self._memories.conversation_meta)


class AsyncMemoriesResourceWithStreamingResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_streamed_response_wrapper(
            memories.create,
        )
        self.list = async_to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            memories.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> AsyncConversationMetaResourceWithStreamingResponse:
        return AsyncConversationMetaResourceWithStreamingResponse(self._memories.conversation_meta)
