from telethon import TelegramClient
from telethon import events
from datetime import datetime
from gtts import gTTS
from telethon import utils
from telethon.utils import pack_bot_file_id
from telethon import events, functions
from deep_translator import GoogleTranslator
from googletrans import LANGUAGES
from langdetect import detect
from googletrans import Translator
from telethon.tl import functions
from telethon import events, functions, __version__
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.types import ChatBannedRights
from logging import *
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest

import sys
import traceback
import io
import re
import requests
import emoji
import os
import speedtest
import random
import subprocess
import asyncio
import wikipedia

#import yt
import asyncio
import math
import os
import time
import ffmpeg
import json

from asyncio import sleep
from telethon import TelegramClient
from telethon import events
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

api_id = 8544088
api_hash ="eeaab790f54273020abb090afa4a2786"
user = TelegramClient("ubot_me", api_id,api_hash)






@user.on(events.NewMessage(pattern=".ping"))
async def dq(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n{}".format(ms))


borg = user

@borg.on(events.NewMessage(pattern="dm ?(.*)"))
async def _(dc):

    d = dc.pattern_match.group(1)

    c = d.split(" ")

    chat_id = c[0]
    try:
        chat_id = int(chat_id)

    except BaseException:

        pass

    msg = ""
    masg = await dc.get_reply_message()  # ghanta😒😒
    if dc.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await dc.edit("⚜️Message Delivered! Sar⚜️")
    for i in c[1:]:
        msg += i + " " 
    if msg == "":  # hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit("⚜️Message Delivered!⚜️")
    except BaseException:  # hmmmmmmmmm🤔🤔
        await dc.edit(".dm (username) (text)")

######
import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location


async def edit_or_reply(event, msg):
  try:
    await event.edit(msg)
  except:
    await event.reply(msg)
        
    
import os
 
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "\downloads")

@borg.on(events.NewMessage(pattern="info(?: |$)(.*)"))
async def who(event):
    cat = await edit_or_reply(
        event, "Astro steal some data from This guuyyy.🌚."
    )
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        await edit_or_reply(event, "Could not fetch info of that user.")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await borg.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
    except TypeError:
        await cat.respond(caption, parse_mode="html")


async def get_user(event):
    """Get the user from argument or replied message."""
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "User haven't set profile pic"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except:
        dc_id = "Couldn't fetch ViU ID!"
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about

    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TEMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("This User has no First Name")
    )
    last_name = (
        last_name.replace("\u2060", "") if last_name else ("This User has no Last Name")
    )
    username = "@{}".format(username) if username else ("This User has no Username")
    user_bio = "This User has no About" if not user_bio else user_bio
    caption = "<b>USER INFO FROM ASTRO-UB :</b>\n\n"
    caption += f"👤First Name: {first_name} {last_name}\n"
    caption += f"🤵Username: {username}\n"
    caption += f"🔖ID: <code>{user_id}</code>\n"
    caption += f"🌏Data Centre ID: {dc_id}\n"
    caption += f"🖼Number of Profile Pics: {replied_user_profile_photos_count}\n"
    caption += f"🤖Is Bot: {is_bot}\n"
    caption += f"🔏Is Restricted: {restricted}\n"
    caption += f"🌐Is Verified by Telegram: {verified}\n\n"
    caption += f"✍️Bio: \n<code>{user_bio}</code>\n\n"
    caption += f"👥Common Chats with this user: {common_chat}\n"
    caption += f"🔗Permanent Link To Profile: "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    return photo, caption

        
 
 

#-*-coding:utf8;-*-
import os 
from telethon import events 
TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
        
@borg.on(events.NewMessage(pattern="tts (.*)"))
async def tts(event):

    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)

    start = datetime.now()

    if event.reply_to_msg_id:

        previous_message = await event.get_reply_message()

        text = previous_message.message

        lan = input_str

    elif " " in input_str:

        values = input_str.split(" ")
        lan = values[0]
        text = " ".join(values[1:len(values)])

    else:

        await event.edit("Invalid Syntax. Module stopping.")

        return

    text = text.strip()

    lan = lan.strip()

    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):

        os.makedirs(TMP_DOWNLOAD_DIRECTORY)

    required_file_name = TMP_DOWNLOAD_DIRECTORY + "voice.mp3"

    try:

        tts = gTTS(text, lang=lan)

        tts.save(required_file_name)
        
        end = datetime.now()

        ms = (end - start).seconds

        await borg.send_file(
            event.chat_id,
            required_file_name,
            # caption="Processed {} ({}) in {} seconds!".format(text[0:97], lan, ms),
            reply_to=event.message.reply_to_msg_id,
            allow_cache=False,
            voice_note=True,
        )

        await event.delete()

    except Exception as e:

        await event.edit(str(e))


@user.on(events.NewMessage(pattern=".id"))
async def idus(event):
  if event.fwd_from:
    return
  user_reply = None
  if event.reply_to_msg_id:
    user_reply = await event.get_reply_message()
  if user_reply and user_reply.sender_id:
    await event.edit(f"🆔 della persona: {user_reply.sender_id}")
  else:
    await event.edit("🆔 della persona: {}".format(str(event.chat_id)))

@user.on(events.NewMessage(pattern=".get_id"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(str(event.chat_id), str(r_msg.sender_id), bot_api_file_id))
        else:
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`".format(str(event.chat_id), str(r_msg.sender_id)))
    else:
        await event.edit("Current Chat ID: `{}`".format(str(event.chat_id)))

@user.on(events.NewMessage(from_users=(1986957932)))
async def testcommandText(event):
  if event.text == ".testh":
    await event.edit("test event.text a funzionato")


@user.on(events.NewMessage(outgoing=True))
async def blockuser(event):
  if event.text.startswith(".block"):
    try:
      Username =event.text.split(" ")[1]
      result = await event.client(functions.contacts.BlockRequest(id=Username))
      await event.edit(f"this User it has been blocked {Username}")
    except:
      await event.edit(f"utente non trovato {Username}")
    
    
@user.on(events.NewMessage(outgoing=True))
async def unblockuser(event):
  if event.text.startswith(".unblock"):
    try:
      Username =event.text.split(" ")[1]
      result = await event.client(functions.contacts.UnblockRequest(id=(Username)))
      await event.edit(f"this User it has been unblocked {Username}")
    except:
      await event.edit(f"utente non trovato {Username}")
      
      
@user.on(events.NewMessage(from_users=(1986957932)))
async def clear(event):
  if event.text == ".clear":
    await event.delete()
    os.system("clear")
    a = await event.respond("Messaggio di errori cancellati")
    await asyncio.sleep(0.5)
    await a.delete()
    print("userbot In BETA")

#tradutore
@user.on(events.NewMessage(pattern=".tr ?(.*)"))
async def tr(event):
    if len(event.text) > 3 and event.text[3] != " ":
        return
    input = event.text[4:6]
    txt = event.text[7:]
    if txt:
        text = txt
        lan = input or "en"
    elif event.is_reply:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    else:
        await edit_or_reply(event, "`.tr LanguageCode` as reply to a message\n\nCheck Languages Codes at [chat_me](https://t.me/Aledev01_dc1)")
        return
    lan = lan.strip()
    try:
        lmao_bruh = text
        lmao = detect(text)
        after_tr_text = lmao
        translated = GoogleTranslator(source="auto", target=lan).translate(lmao_bruh)
        source_lan = LANGUAGES[after_tr_text]
        transl_lan = LANGUAGES[lan]
        output_str = f"""**TRANSLATED SUCCESSFULLY BY Anto�**
**Source ({source_lan})**:
`{text}`
**Translation ({transl_lan})**:
`{translated}`"""
        if len(output_str) >= 4096:
            out_file = output_str
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("lol")).json()
            url2 = f"https://del.dog/{r['key']}"
            starky = f"Translated Text Was Too Big, Never Mind I Have Pasted It [Here]({url2})"
        else:
            starky = output_str
        await event.edit(starky)
    except Exception as exc:
        await edit_or_reply(event, str(exc))

voiptest = user
#exec

@voiptest.on(events.NewMessage(outgoing=True,pattern=".exec"))
async def exec_new(event):
    
    if event.fwd_from:

        return
    await event.edit("**Processing...**")
    cmd = event.text.split(" ", maxsplit=1)[1]
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "✅"

    final_output = "**► EVALPy**: `{}` \n\n**OUTPUT**: \n`{}` \n".format(cmd, evaluation)

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=f"**PROCCESSED**: `{cmd}`",
                reply_to=reply_to_id
            )
            await event.delete()
    else:
        await event.edit(final_output)


async def aexec(code, event):
    exec(
        f'async def __aexec(event): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](event)


#wikipedia
@user.on(events.NewMessage(outgoing=False,pattern=".wiki (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await event.edit(
        "WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result)
    )
 


      


#code yt
async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for uploads and downloads."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            ''.join(["▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await d.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]
  
@user.on(events.NewMessage(outgoing=False,pattern="yt(a|v) (.*)",from_users=(1986957932)))
async def download_video(v_url):
    """ For .ytdl command, download media from YouTube and many other sites. """
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()

    v = await v_url.respond("`Preparing to download...`")

    if type == "a":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '480',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True

    elif type == "v":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True

    try:
        await v.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await v.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await v.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await v.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await v.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await v.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await v.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await v.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await v.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await v.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await v.edit(f"`Preparing to upload song:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(ytdl_data['duration']),
                                       title=str(ytdl_data['title']),
                                       performer=str(ytdl_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v, c_time, "Uploading..",
                         f"{ytdl_data['title']}.mp3")))
        os.remove(f"{ytdl_data['id']}.mp3")
        await v.delete()
    elif video:
        await v.edit(f"`Preparing to upload video:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp4",
            supports_streaming=True,
            caption=ytdl_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v, c_time, "Uploading..",
                         f"{ytdl_data['title']}.mp4")))
        os.remove(f"{ytdl_data['id']}.mp4")
        await v.delete()  

@user.on(events.NewMessage(outgoing=True,pattern=".spam"))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()


@user.on(events.NewMessage(outgoing=True,pattern="^.tspam"))
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()

@user.on(events.NewMessage(outgoing=True, pattern="^.bigspam"))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()



#riavvio userbot
@user.on(events.NewMessage(outgoing=True))
async def riavviouserbot(event):
  if event.text == ".riavvia":
    await event.delete()
    
    import os, sys, threading

    os.system("clear")

    os.execl(sys.executable, sys.executable, *sys.argv)
    thereading.Thread(target=_restart, args=(bot, msg)).start()

#wikimedia

@user.on(events.NewMessage(outgoing=False,pattern=".wikimedia (.*)",from_users=(1986957932)))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://commons.wikimedia.org/w/api.php?action={}&generator={}&prop=imageinfo&gimlimit={}&redirects=1&titles={}&iiprop={}&format={}".format(
        "query",
        "images",
        "5",
        input_str,
        "timestamp|user|url|mime|thumbmime|mediatype",
        "json"
    )
    r = requests.get(url).json()
    result = ""
    results = r["query"]["pages"]
    for key in results:
        current_value = results[key]
        pageid = current_value["pageid"]
        title = current_value["title"]
        imageinfo = current_value["imageinfo"][0]
        timestamp = imageinfo["timestamp"]
        user = imageinfo["user"]
        descriptionurl = imageinfo["descriptionurl"]
        mime = imageinfo["mime"]
        mediatype = imageinfo["mediatype"]
        result += """\n
        pageid: {}
        title: {}
        timestamp: {}
        user: [{}]({})
        mime: {}
        mediatype: {}
        """.format(pageid, title, timestamp, user, descriptionurl, mime, mediatype)
    await event.edit("**Search**: {} \n\n **Results**: {}".format(input_str, result))

@user.on(events.NewMessage(pattern=".f ?(.*)",from_users=(1986957932)))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.respond(pay)


@user.on(events.NewMessage(outgoing=True,pattern=".indiaflang"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    await event.edit("Hello")
    animation_chars = [
    "Indian Flag",
    "**🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧\n⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️\n⬜️⬜️⬜️⬜️⬜️🟦🟦🟦⬜️⬜️⬜️⬜️⬜️\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n\n                🧡🤍💚\n\nProud To Be An Indian❣️!!**"
    ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@user.on(events.NewMessage(outgoing=True,
    pattern=".copy"))
async def copy(e):
  reply = await e.get_reply_message()
  if reply:
    if reply.text and not reply.media:
      await user.send_message(e, reply.text)
    else:
      await reply.reply(reply)
    if e.out:
      await e.delete()
    else:
        await e.edit("`Reply To any message`")

#purge
BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
try:
  BOTLOG_CHATID = int(BOTLOG_CHATID)
except:
  pass

BOTLOG = (os.environ.get('BOTLOG' ,'False'))

client = user

@client.on(events.NewMessage(outgoing=True,pattern="#purge"))
async def fastpurger(purg):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat,
                                               min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "**Purge completato!**\n Messaggi eliminati: " + str(count),
    )
    await sleep(2)
    await done.delete()

#@client.on(events.NewMessage(from_users=(1986957932)))
#async def mr(event):
  #if event.text == ".msg":
    #m = event.text.split(" ",maxsplit=1)[1]
    #await event.respond(m)
  #else:
    #d = await event.get_reply_message()
    #a = event.text.split(" ",maxsplit=1)[1]
    #await client.send_message(event.chat_id, a, reply_to=d)
    #await event.delete()

groups = []
 
@user.on(events.NewMessage(outgoing=True)) 
async def stoptalk(event):
  if event.text == ".stoptalk":
    groups.append(event.chat_id)
    await event.edit("✅ » StopTalk Attivato!")
  elif event.text == ".ontalk":
    await event.edit("❌ » Stotalk Disattivato! ")
    groups.clear()
 
@user.on(events.NewMessage(incoming=True))
async def cancellamsg(event):
  if event.text or event.media:
    if event.chat_id in groups:
      await event.delete()
      
@user.on(events.NewMessage(incoming=True))
async def cancellamsg(event):
  if event:
    if event.chat_id in groups:
      await event.delete()

@client.on(events.NewMessage(pattern=".unisciti"))
async def usniscitineigruppi(event):
  join = event.text.split(" ")[1]
  await event.client(JoinChannelRequest(join))
  await event.edit(f"ti sei unito al gruppo questo -->{join}")

@client.on(events.NewMessage(pattern=".esci"))
async def escineigruppi(event):
  join = event.text.split(" ")[1]
  await event.client(LeaveChannelRequest(join))
  await event.edit(f"sei uscito dal gruppo questo -->{join}")

@client.on(events.NewMessage(pattern="nmbr",from_users=(1986957932)))
async def number(event):
    a = await client.get_me()
    phune = a.phone
    await event.delete()
    await client.send_message(event.chat_id, phune)

@client.on(events.NewMessage(pattern=".delm  ?(.*)",from_users=(1986957932)))
async def delm(event):
  await event.delete()
  r = await event.get_reply_message()
  await r.delete()
  motivo = event.pattern_match.group(1)
  await event.edit(f"[{r.sender.first_name}](tg://user?id={r.sender_id}), il tuo messaggio e stato cancellato\n\n**Motivo:** {motivo}")


@client.on(events.NewMessage(pattern=".rdevale  ?(.*)"))
async def rdevale(event):
  m = event.pattern_match.group(1)
  await client.send_message(1986957932,f"__{event.sender_id}__\n\nMessagio da lui: {m}")
  await event.respond("messaggio inviato")

@user.on(events.NewMessage(outgoing=True, pattern="purgeme"))
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = message[9:]
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) + " messages.",
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    i = 1
    await smsg.delete()

@user.on(events.NewMessage(pattern=r"hl"))
async def hl(event):
  n = event.text.split(" ")[1]
  for a in range(int(n)):
    x = event.text.split(" ")[1]
    v = event.text.split(" ")
    user_or_id = x
    mbsg = v
    await user.send_message(user_or_id,f"{mbsg}")


@user.on(events.NewMessage(outgoing=True,pattern=".calc"))
async def _(car):
    cmd = car.text.split(" ", maxsplit=1)[1]
    event = await car.edit("Calculating ...")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Sorry I can't find result for the given equation"
    final_output = "EQUATION: {} \n\n SOLUTION: \n{} \n".format(
        cmd, evaluation
    )
    await car.edit(final_output)


async def aexec(code, event):
    exec(f"async def aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["aexec"](event) 


@user.on(events.NewMessage(outgoing=True,pattern=".name"))
async def nameuserbot(event):
  x = event.text.split(" ", maxsplit=1)[1]
  result = await client(functions.account.UpdateProfileRequest(
        first_name=x,
    ))
  await event.edit(f"nome messo come **{x}**")


#afk test
if os.path.exists("saves_afk.json"):
	with open("saves_afk.json", "r+") as f:
		SAVES = json.load(f)
else:
	SAVES = {"AFKMode": False, "Approved": [], "mutedList": [], "AFK-Mex": "Puoi customizzare il seguente messaggio con .msgafk", "Block-Mex": "Puoi customizzare il seguente messaggio con .msgblock"}
	with open("saves_afk.json", "w+") as f:
		json.dump(SAVES, f)
	

async def save():
	global SAVES
	with open("saves_afk.json", "w+") as f:
		json.dump(SAVES, f)



inWait = []
	
@user.on(events.NewMessage(outgoing=True, pattern=".msgafk"))
async def setAFKMex(e):
	global SAVES
	st = e.text.split(" ", 1)
	if st.__len__() == 2:
		SAVES["AFK-Mex"] = st[1]
		'(save)'
		await e.edit("**✅ Messaggio Impostato Correttamente ✅**")
	else:
		await e.edit("**❌ Specificare il messaggio ❌**")


@user.on(events.NewMessage(outgoing=True, pattern=".afk"))
async def setAFK(e):
	global SAVES
	if SAVES["AFKMode"]:
		SAVES["AFKMode"] = False
		'(save)'
		await e.edit("**❌ AFK Mode Disattivata ❌**")
	else:
		SAVES["AFKMode"] = True
		'(save)'
		await e.edit("**✅ AFK Mode Attivata ✅**")
	
@user.on(events.NewMessage(outgoing=True,pattern=".approve"))
async def approveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		await e.edit("**❌ Questo utente è già approvato ❌**")
	else:
		SAVES["Approved"].append(e.chat_id)
		'(save)'
		await e.edit("**✅ Utente Approvato ✅**")
	
@user.on(events.NewMessage(outgoing=True,pattern=".disapprove"))
async def disapproveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		SAVES["Approved"].remove(e.chat_id)
		'(save)'
		await e.edit("**❌ Utente Disapprovato ❌**")
	else:
		await e.edit("**❌ Quest utente non è approvato ❌**")
@user.on(events.NewMessage(incoming=True))
async def doAFK(e): 
	global SAVES, inWait
	if SAVES["AFKMode"] and e.is_private and not (await e.get_sender()).bot and not e.chat_id in SAVES["Approved"]:
		await e.delete()
		if not e.chat_id in inWait: 
			inWait.append(e.chat_id)
			if e.text == None or e.text == "":
				mex = "__MEDIA__"
			else:
				mex = e.text
			await e.respond(SAVES["AFK-Mex"].replace("{msg}", mex))
			await asyncio.sleep(30)
			inWait.remove(e.chat_id)
@user.on(events.NewMessage(pattern=".verify"))
async def Verify(e):
  global verify
  verify = e
  await e.client.send_message("@SpamBot", "/start")
@user.on(events.NewMessage(pattern=""))
async def checkVerify(e):
  global verify
  global verify
  if verify != None:
    if e.chat_id == 178220800:
      if ":" in e.text:
        st = e.text.split(" ")
        for i in range(st.__len__()):
          if ":" in st[i]:
            fine = st[i - 3] + " " + st[i - 2] + " " + st[i - 1] + " Ore: " +st[i]
            break
        await verify.edit(f"**? Sei limitato fino al {fine} ?**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
      else:
        await verify.edit("**? Non sei limitato ?**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
        
print("userbot In BETA")

user.start()
user.run_until_disconnected()