from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timezone
from glob import glob
from ..db import db

from discord import Embed, Intents
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

PREFIX = "#"
OWNER_IDS = [222071865567477760, 342948804724654082]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            intents=Intents.all()
        )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.env", "r", encoding="utf-8") as token:
            self.TOKEN = token.read()

        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def draak_reminder(self):
        await self.stdout.send("TIJD VOOR EEN DRAKENNEST DING!")

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")
        await self.stdout.send("An error occured.")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(1078381947736301619) #Verander deze waarde voor andere server, is nu BADRNG TEST SERVER
            self.stdout =self.get_channel(1078381948428353599) #Verander deze waarde voor bericht in een kanaal.
            self.scheduler.add_job(self.draak_reminder, CronTrigger(hour="11", minute="0", second="0"))
            self.scheduler.start()

            await self.stdout.send("Ik ben nu online! Dit gaat vast vervelend worden met testen.")

            #embed = Embed(title="Online!", description="MVP Bot is ready for your service now.",
            #              colour=0xFF0000,
            #              timestamp=datetime.now(timezone.utc))
            #fields = [("Name", "MVP BOT", True),
            #          ("Reason", "Gezeik", True),
            #          ("Kut", "Zooi", False)]
            #for name, value, inline in fields:
            #    embed.add_field(name=name, value=value, inline=inline)
            #embed.set_footer(text= "Niet doorvertellen")
            #await channel.send(embed=embed)

            print("bot ready")

        else:
            print("bot reconnected")


    async def on_message(self, message):
        pass

bot = Bot()
