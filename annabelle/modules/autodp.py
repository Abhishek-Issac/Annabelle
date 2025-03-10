import asyncio
from Anabelle import Annabelle
from pyrogram import filters as vrn
from config import MY_ID, HANDLER, CHANNEL_ID
from pyrogram.types.messages_and_media import Message


@Annabelle.on_message(vrn.command("autodp", HANDLER))
async def autodp(bot:Annabelle, msg:Message) :
    chat_id = CHANNEL_ID
    if msg.from_user.id == MY_ID :
        try :
            value = msg.text.split(" ")[1].lower()
        except :
            await msg.edit_text(text="**__Please Enter a value__**")
        if value == "true" :
            for i in await bot.get_history(chat_id) :
                await msg.edit_text(text="**__Plugin Enabled__** : `autodp`")
                profile_pic = await bot.download_media(message=i.photo.file_id)
                asyncio.sleep(4000)
                await bot.set_profile_photo(photo=profile_pic)
        elif value == "false" :
            await msg.edit_text(text="**__Plugin Disabled__** : `autodp`")
        else :
            await msg.edit_text(text="**__Please enter a boolean instead of blah blah blah__**")
