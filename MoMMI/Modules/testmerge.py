from typing import Match
from discord import Message
from MoMMI import command, MChannel


@command("testmerge_dummy", "testmerge")
async def testmerge_dummy_command(channel: MChannel, match: Match, message: Message) -> None:
    await channel.send("Sorry dude, we can't do that (yet?).")
