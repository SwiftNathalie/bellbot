"""Stub test file"""
import pytest


@pytest.mark.asyncio
async def smoke_test() -> bool:
    """Smoke test"""
    assert True is True
    return True