"""Shared Anthropic client + default model for lesson scripts."""

from anthropic import Anthropic, AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()

# Swap this if you want a different default for local practice.
MODEL = "claude-sonnet-4-5"


def get_client() -> Anthropic:
    """Return a sync client; reads ANTHROPIC_API_KEY from the environment."""
    return Anthropic()


def get_async_client() -> AsyncAnthropic:
    """Return an async client; reads ANTHROPIC_API_KEY from the environment."""
    return AsyncAnthropic()
