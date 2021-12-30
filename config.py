import discord

PREFIX = "d!"
DESCRIPTION = "Dalti is a multi-purpose bot. Just a cool bot, what else do we need to say?"

EMOTES = {
    "success": "<:daltiSuccess:923699355779731476>",
    "error": "<:daltiError:923699414646816768>",
    "green": "<:green:881971370634924063>",
    "yellow": "<:yellow:881971305749028944>",
    "red": "<:red:881971454369988608>",
    "blue": "<:blue:881971628106481694>",
    "grey": "<:grey:881971588973609041>",
    "chain": "<:chain:881974754293215252>",
    "warning": ":warning",
    "info": "<:info:881973831974154250>",
    "gdot": "<:gdot:882404710148083724>",
    "ydot": "<:rdot:882404641286000681>",
    "rdot": "<:ydot:882404755949895730>"
}

COLORS = {
    "success": discord.Colour.from_rgb(67, 181, 130),
    "error": discord.Colour.from_rgb(240, 74, 71),
    "warning": discord.Colour.from_rgb(255, 155, 0),
    "info": discord.Colour.from_rgb(113, 134, 213)
}

ACTIVITY = "with toys"