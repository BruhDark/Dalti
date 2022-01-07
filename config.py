import discord

PREFIX = "d!"
DESCRIPTION = "Dalti is a multi-purpose bot. Just a cool bot, what else do we need to say?"

EMOTES = {
    "success": "<:daltiSuccess:923699355779731476>",
    "error": "<:daltiError:923699414646816768>",

    "warning": ":warning:",
    "info": "<:info:881973831974154250>",
    "question": "<:Question:929051955962195999>",

    "operational": "<:Operational:882404710148083724>",
    "partialoutage": "<:PartialOutage:882404641286000681>",
    "majoroutage": "<:MajorOutage:882404755949895730>",
    "maintenance": "<:UnderMaintenance:881969909247148052>",

    "dnd": "<:DoNotDisturb:928716110822518834>",
    "idle": "<:Idle:929049988573581352>",
    "online": "<:Online:928716318054694993>",
    "offline": "<:Offline:928716879474851870>",

    "loading": "<a:loading:928730342964211712>",
    "spotify": "<:Spotify:929060525881565224>",
}

COLORS = {
    "success": discord.Colour.from_rgb(67, 181, 130),
    "error": discord.Colour.from_rgb(240, 74, 71),
    "warning": discord.Colour.from_rgb(255, 155, 0),
    "info": discord.Colour.from_rgb(113, 134, 213),
    "normal": discord.Colour.from_rgb(94, 23, 235)
    }

BADGES = {
    "bot": "<:Bot:928765691778203719>",
    "bughunter": "<:BugHunter:928765827107422268>",
    "moderator": "<:DiscordCertifiedModerator:881971670921916518>",
    "staff": "<:DiscordStaff:882405445136965633>",
    "events": "<:HypeSquadEvents:928765434281488534>",
    "balance": "<:HypeSquad_Balance:928765104110047273>",
    "bravery": "<:HypeSquad_Bravery:928765052427841628>",
    "brilliance": "<:HypeSquad_Brilliance:928764974103404554>",
    "verifiedbot": "<:VerifiedBot:848277286927073280>",
    "bughunter2": "<:BugHunter:928768063933939783>",
    "partner": "<:DiscordPartner:928768159215923230>",
    "early": "<:EarlySupporter:928768119072231454>",
    "botdev": "<:VerfiedBotDeveloper:928765568058785852>"
}

ACTIVITY = "with toys"