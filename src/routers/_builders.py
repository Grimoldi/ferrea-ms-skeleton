from fastapi import Request
from ferrea.core.context import Context
from ferrea.core.header import FERRA_CORRELATION_HEADER, get_correlation_id

from configs import settings


async def _build_context(request: Request) -> Context:
    """Build a context from the request.

    Args:
        request (Request): the HTTP Request.

    Returns:
        Context: the context of the call.
    """
    ferrea_correlation_id = request.headers.get(FERRA_CORRELATION_HEADER)
    correlation_id = await get_correlation_id(ferrea_correlation_id)
    return Context(str(correlation_id), settings.ferrea_app.name)
