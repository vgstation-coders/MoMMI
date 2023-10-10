import asyncio
from typing import Match
import aiohttp
from discord import Message
from MoMMI.commands import command
from MoMMI.master import master
from MoMMI.server import MChannel
from MoMMI.role import MRoleType


@command("reload", "reload", roles=[MRoleType.OWNER])
async def reload(channel: MChannel, match: Match, message: Message) -> None:
    errors = await master.reload_modules()

    if errors:
        await message.add_reaction("🤒")

    else:
        await message.add_reaction("👌")


@command("modules", "modules", roles=[MRoleType.OWNER])
async def modules(channel: MChannel, match: Match, message: Message) -> None:
    msg = "```"
    for module in master.modules.values():
        msg += f"{module.name}:\n"
        for handler in module.handlers.values():
            msg += f"* {handler.name}\n"

    msg += "```"

    await channel.send(msg)


@command("shutdown", "shutdown", roles=[MRoleType.OWNER])
async def shutdown_command(channel: MChannel, match: Match, message: Message) -> None:
    await channel.send("Shutting down!")
    # Ensure future instead of awaiting to prevent code calling us exploding.
    asyncio.ensure_future(channel.server.master.shutdown())


@command("name", r"name\s+(.+)", roles=[MRoleType.OWNER])
async def name_command(channel: MChannel, match: Match, message: Message) -> None:
    await master.client.user.edit(username=match.group(1))


@command("nick", r"nick\s+(.+)", roles=[MRoleType.OWNER])
async def nick_command(channel: MChannel, match: Match, message: Message) -> None:
    member = message.guild.get_member(master.client.user.id)
    await member.edit(nick = match.group(1))


@command("avatar", r"avatar", roles=[MRoleType.OWNER])
async def avatar_command(channel: MChannel, match: Match, message: Message) -> None:
    attachment = message.attachments[0]["url"]
    async with aiohttp.ClientSession() as session:
        async with session.get(attachment) as request:
            data = await request.read()

    await master.client.user.edit(avatar=data)


@command("save", r"save", roles=[MRoleType.OWNER])
async def save_command(channel: MChannel, match: Match, message: Message) -> None:
    await master.save_all_storage()
