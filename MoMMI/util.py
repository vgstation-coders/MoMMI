import os
import pickle
from datetime import datetime
from typing import Any
import aiofiles
import pytz
from discord import Message
from MoMMI.master import master


async def pickle_dump(obj: Any, filename: os.PathLike) -> None:
    """
    Async pickle dump.
    """
    byte = pickle.dumps(obj)
    async with aiofiles.open(filename, "wb") as f:
        await f.write(byte)


async def pickle_load(filename: os.PathLike) -> Any:
    """
    Async pickle load.
    """
    async with aiofiles.open(filename, "rb") as f:
        byte = await f.read()

    return pickle.loads(byte)


async def add_reaction(message: Message, reaction: str) -> None:
    await message.add_reaction(reaction)


async def remove_reaction(message: Message, reaction: str) -> None:
    await master.client.remove_reaction(message, reaction)


def utcnow() -> datetime:
    return datetime.now(pytz.utc)
