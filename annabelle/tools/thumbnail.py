import ytthumb
from annabelle.commands import Annabelle

async def thumb(Annabelle, message):
    try:
        args = message.text.split(None, 1)      
        d=await message.reply("```Processing...```")
        link=args[1]
        thumb=ytthumb.thumbnail(video=link,
                                quality="maxres")
        await message.reply_photo(photo=thumb)      
        await d.delete()            
    except:
        await message.reply("<b>No results found!\nTry to check your link..</b>")
        await d.delete()
