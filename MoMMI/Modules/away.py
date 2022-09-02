from typing import Match
from discord import Message
import discord
from MoMMI import MChannel, master, command

@command("away", "away")
async def dance(channel: MChannel, match: Match, message: discord.Message) -> None:
    await channel.send(None, file=discord.File('/home/gutter/MoMMI/Files/away.gif'))
