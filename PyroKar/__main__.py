# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from PyroKar import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from PyroKar.helpers.misc import create_botlog, heroku
from PyroKar.modules import ALL_MODULES

MSG_ON = """
✨ **PyroZu-Userbot Udah Aktif** ✨
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}zu` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"PyroKar.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("Html12text")
            await bot.join_chat("getenv")
            await bot.join_chat("Karc0de")
            await bot.join_chat("kazusupportgrp")
            await bot.join_chat("SharingUserbot")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("PyroKar").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("PyroKar").info(f"PyroZu-UserBot v{BOT_VER} [✨ BERHASIL DIAKTIFKAN YA SAYANG! ✨]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("PyroKar").info("Starting PyroZu-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
