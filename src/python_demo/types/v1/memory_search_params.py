# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MemorySearchParams"]


class MemorySearchParams(TypedDict, total=False):
    current_time: Optional[str]
    """Current time, used to filter forward-looking events within validity period"""

    end_time: Optional[str]
    """Time range end (ISO 8601 format)"""

    group_id: Optional[str]
    """Group ID (at least one of user_id or group_id must be provided)"""

    include_metadata: bool
    """Whether to include metadata"""

    memory_types: Optional[List[Literal["profile", "episodic_memory", "foresight", "event_log"]]]
    """List of memory types to retrieve, enum values from MemoryType:

    - episodic_memory: episodic memory
    - foresight: prospective memory
    - event_log: event log (atomic facts) Note: profile type is not supported in
      search interface
    """

    query: Optional[str]
    """Search query text"""

    radius: Optional[float]
    """
    COSINE similarity threshold for vector retrieval (only for vector and hybrid
    methods, default 0.6)
    """

    retrieve_method: Literal["keyword", "vector", "hybrid", "rrf", "agentic"]
    """Retrieval method, enum values from RetrieveMethod:

    - keyword: keyword retrieval (BM25, default)
    - vector: vector semantic retrieval
    - hybrid: hybrid retrieval (keyword + vector)
    - rrf: RRF fusion retrieval (keyword + vector + RRF ranking fusion)
    - agentic: LLM-guided multi-round intelligent retrieval
    """

    start_time: Optional[str]
    """Time range start (ISO 8601 format)"""

    top_k: int
    """Maximum number of results to return"""

    user_id: Optional[str]
    """User ID (at least one of user_id or group_id must be provided)"""
