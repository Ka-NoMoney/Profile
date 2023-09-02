
import discord,time
#from discord import File
from ping3 import ping
#from config import * #chỗ này bị lỗi import nên dòng 207 lỗi theo , lệnh Ping(ai biết sửa thì sửa toi kbt :)) )
from discord.utils import escape_mentions
import aiohttp
import asyncio
import random
from random import choice
import os, sys, requests, json
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
import psutil

import discord
import random
import os
import urllib.parse, urllib.request, re
import psutil
import asyncio
import datetime
from discord.ext import commands#, activities
from discord.ext.commands import has_permissions, has_role, command, MissingPermissions, MissingRole, MissingRequiredArgument
from discord import Embed,Color
from asyncio import sleep
import json
from io import BytesIO
import re
import aiohttp
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
import bot_token
import aiosqlite







os.chdir("D:\\botdis")





async def get_prefix(bot, message):
    try:
        with open("prefix.json", "r") as f:
            prefix = json.load(f)

        return prefix[str(message.guild.id)]
    except:
        return "," or ["<@1147435574714695710> "]

intents = discord.Intents.all()
intents.messages = True
threading = ThreadPoolExecutor(max_workers=int(100000000))

bot = commands.Bot(command_prefix=get_prefix,help_command=None, intents=intents)


#bot = commands.Bot(command_prefix=[',','<@!931098231729971210> '], intents=intents)
owner = 928489823709331527

#@bot.event
#async def on_guild_join(guild):


 #   with open("prefix.json", "r") as f:
  #      prefixes = json.load(f)

 #   prefixes[str(guild.id)] = ","

#    with open("prefix.json", "w") as f:
 #       json.dump(prefixes,f)

@bot.command(aliases=["setpr"])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):

    with open("prefix.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefix.json", "w") as f:
        json.dump(prefixes, f)

    await ctx.send(f"prefix mới của sever là `{prefix}`")






list_ban = []
async def check_ban(ctx):
    if ctx.author.id in list_ban:
        return False
    return True


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
       msg = '⏲️Này bạn đang sử dụng bot quá nhanh, vui lòng chờ `{:.2f} giây` để sử dụng tiếp'.format(error.retry_after)
       await ctx.reply(msg, mention_author=False,delete_after=5)



@bot.event
async def on_ready():

        print('bot đã on')
  







def pre():
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)]

import datetime

@bot.command()
async def test(ctx):
    await ctx.send(discord.utils.format_dt(ctx.message.created_at ,"R"))



bot.remove_command("help")
@bot.group(invoke_without_command=True)
async def help(ctx):
    server = ctx.message.guild
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
    embed = discord.Embed(title ='',description =f'Danh sách lệnh cho bot __{bot.user.name}__\nPrefix của bot là: `,`',color=0x00ccff,timestamp=ctx.message.created_at)
    embed.add_field(name='➤𝘾𝙤𝙢𝙢𝙖𝙣𝙙 ',value='`say`,`rep`,`giveaway`,`svinfo`,`ib`,`poll`,`afk`,`info`,`avatar`,`chatgpt`,`botinfo`,`setprefix`',inline=False)
    embed.add_field(name='➤𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝘼𝙙𝙢𝙞𝙣 ',value='`ban`,`kick`,`warn`,`clear`,`mute`,`addrole`',inline=False)
    embed.set_footer(text=f'được yêu cầu bởi- {ctx.author.name}')
    embed.set_thumbnail(url=ctx.bot.user.avatar)
    if ctx.guild.icon is None:
        pass
    else:
     embed.set_author(name='Help command' ,icon_url=server.icon)
    await ctx.send(embed=embed)





    


 



#svinfo owner.display_name
@bot.command(aliases=['server'])
async def svinfo(ctx,guildid:int=None):

  banner =  ctx.message.guild.banner


  server = ctx.message.guild


  channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
  channel_counts = len([x for x in server.channels if type(x) == discord.channel.VoiceChannel])
  svembed = discord.Embed(title=f'Thông tin về server __{ctx.message.guild.name}__',timestamp = ctx.message.created_at, color = discord.Colour.blue())
  svembed.add_field(name='🆔Server ID',value=ctx.message.guild.id)
  svembed.add_field(name="📆 Tạo vào", value=discord.utils.format_dt(ctx.guild.created_at,style="R"))
  svembed.add_field(name='👑Owner', value=f'<@!{ctx.guild.owner_id}>')
  if ctx.guild.premium_tier is None:
      pass
  else:
   svembed.add_field(name=f'👥 Menbers({server.member_count})',value=f' \n**{ctx.message.guild.premium_subscription_count}** Boosts({server.premium_tier}) :sparkles:')
  svembed.add_field(name=f'💬 Channel ({str(channel_counts + channel_count)}) ', value=f' ឵឵឵ ឵឵឵឵ ឵**{str(channel_count)}** <:text:938050236528611338> | **{str(channel_counts)}** <:voice:938050311556325386>')

  svembed.add_field(name='🧾 Role', value=f'  ឵឵ ឵឵ ឵឵ ឵឵ ឵឵ ឵឵ ឵឵  **{len(ctx.message.guild.roles)}**')
  svembed.add_field(name='📘 Emoji', value=f'  ឵឵ ឵឵ ឵឵ ឵឵ ឵឵ ឵឵ ឵឵  **{len(ctx.message.guild.emojis)}**')
  banner = ctx.message.guild.banner
  if ctx.guild.icon is None:
      pass
  else:
   svembed.set_thumbnail(url=server.icon)
  svembed.set_footer(text='឵ ឵')
  if ctx.guild.banner is None:
      pass
  else:
   svembed.set_image(url=banner)
  await ctx.reply(embed = svembed, mention_author=False)


@bot.command(name="info")
async def info(ctx,member: discord.Member = None):
    if member == None:
        member = ctx.author
    else:
        member = member
    usr = await bot.fetch_user(member.id)
    if usr.banner:
        banner = usr.banner.url
    voice_state = None if not member.voice else member.voice.channel.mention
    embed = discord.Embed(title=f'Thông tin về:  __{member.display_name}__',timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=member.display_avatar)
    embed.add_field(name='🆔 ID',value=member.id)
    embed.add_field(name='📛 tên gốc',value=member.name)
    embed.add_field(name='📘 create nick',value=discord.utils.format_dt(member.created_at,style="R")) #member.created_at.strftime("%d/%m/%Y"))
    embed.add_field(name='📈 join sever',value=f'឵{discord.utils.format_dt(member.joined_at,style="R")}')
    embed.add_field(name=' In Voice', value=voice_state)
    embed.add_field(name='🔝 Top Role',value=f'  ឵឵ ឵឵ ឵ ឵{member.top_role.mention}')
    if usr.banner is None:
        pass
    else:
        embed.set_image(url=banner)
    await ctx.send(embed=embed)


@bot.command()
async def say(ctx, *, text):
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")




@bot.command(case_insensitive=True)
@commands.has_permissions(ban_members=True)
@has_permissions(kick_members=True)
async def ban(ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"`{member.name}` đã bị ban khỏi server!")


@ban.error
async def purge_error(ctx, MissingPermissions):
	  await ctx.reply('bạn ko đủ quyền')

@bot.command()
@commands.has_permissions(ban_members=True)
@has_permissions(kick_members=True)
async def unban(ctx, user_id : int):
    user = await bot.fetch_user(user_id)
    try:
      await ctx.guild.unban(user)
      await ctx.send(f"**{user.name}** đã được unban")
    except:
      await ctx.send(f"**{user.name}** không nằm trong danh sách ban")
@unban.error
async def purge_error(ctx,MissingPermissions):
	  await ctx.reply('bạn ko đủ quyền')


@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.name} đã bị kick!")
@kick.error
async def purge_error(ctx,MissingPermissions):
	  await ctx.reply('bạn ko đủ quyền')





@bot.command(aliases=['clear','xóa'])
@has_permissions(kick_members=True)
async def purge(ctx,amount):
	if amount == 'all':
		await ctx.channel.purge()
		await ctx.send('Đã xoá tất cả tin nhắn')
		await asyncio.sleep(5.0)
		await ctx.channel.purge(limit=1)
	else:
		await ctx.channel.purge(limit=int(amount) +1)
		await ctx.send(f"Đã xoá {amount} tin nhắn",delete_after=5)
		await ctx.channel.purge(limit=1)
@purge.error
async def purge_error(ctx,MissingPermissions):
	  await ctx.send('bạn ko đủ quyền')


@bot.command()
async def ping(ctx,member: discord.Member = None):
    if member == None:
        member = ctx.author
    ping = random.randint(0,1000)
    ping = discord.Embed(title="",description= f"⚾Pong! {ping}m ")
    await ctx.reply(embed = ping)


@bot.command(kick_members=True)
@has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, arg):
    
    user = member.mention
    embed = discord.Embed(title="Cảnh cáo", color=0xf40000)
    embed.add_field(name="Cảnh báo: ", value=f'Lý do: {arg}', inline=False)
    embed.add_field(name="Người đã bị cảnh cáo: ", value=f'{member.mention}', inline=False)
    embed.add_field(name="Được cảnh cáo bởi: ", value=f'{ctx.author}', inline=False)
    
    embed2 = discord.Embed(title="Cảnh cáo!", color=0xf40000)
    embed2.add_field(name="Cảnh báo: ", value=f'Lý do: {arg}', inline=False)
    embed2.add_field(name="Người đã bị cảnh cáo: ", value=f'{member.mention}', inline=False)
    embed2.add_field(name="Được cảnh cáo bởi: ", value=f'{ctx.author}', inline=False)

    await member.send(f'Bạn đã được cảnh cáo trong server {ctx.message.guild.name} vì: **{arg}**!')
    message = await ctx.send(embed=embed)

@warn.error
async def purge_error(ctx, MissingPermissions):
	  await ctx.reply('bạn ko đủ quyền')


@bot.command(kick_members=True)
async def ib(ctx, member: discord.Member, *, arg):
    await ctx.message.delete()
    await member.send(f'{arg} ')


@bot.command()
async def edit(ctx,msgID:int,*,msg):
	user_msg = ctx.message
	message = await ctx.fetch_message(msgID)
	await message.edit(content=msg)
	await user_msg.delete()

@bot.command(aliases=['pbeta'])
async def purge_beta(ctx, limit, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        return await ctx.send("Hãy nhập một số tự nhiên >0")
    if not member:
        await ctx.channel.purge(limit=limit)
        return await ctx.send(f"Đã xoá {limit} tin nhắn", delete_after=3)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        if m.author == member:
            msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Đã xoá {limit} tin nhắn của {member.mention}", delete_after=3)




@bot.command(aliases=['rep'])
async def reply(ctx,*,text):
	reference = ctx.message.reference
	if reference is None:
		return await ctx.reply("Bạn chưa trả lời tin nhắn nào")
	await reference.resolved.reply(text)
	await ctx.message.delete()

#@bot.command(aliases=['ga'])
#async def giveaway(ctx, time: int, *, prize,):
 #   embed = discord.Embed(title="{}".format(prize),description=f"pick 🎉 để tham gia \nđược tổ chức bởi:{ctx.author.mention}\nKết thúc vào {} giây ".format(time), colour=discord.Color.green(),timestamp=ctx.message.created_at)
    #embed.set_author(name='🎉Giveaway🎉')


def convert(time):
    pos = ["s", "m", "h", "d"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2
    return val * time_dict[unit]




@bot.command(aliases=['ga'])
async def giveaway(ctx, time: int, *, prize, ):
    await ctx.message.delete()


    giveawayembed = discord.Embed(title="{}".format(prize),
                                   description=f"pick 🎉 để tham gia \nEnd: **{time}** giây tới\nHosted by: {ctx.author.mention}",
                                   colour=discord.Color.green(), timestamp=ctx.message.created_at)
    giveawayembed.set_author(name='🎉Giveaway🎉')

    msg = await ctx.send(embed=giveawayembed)
    await msg.add_reaction("🎉")

    await asyncio.sleep(time)
    msg = await msg.channel.fetch_message(msg.id)
    url = msg.jump_url
    winner = None
    for reaction in msg.reactions:
        if reaction.emoji == "🎉":
            users = await reaction.users().flatten()
            users.remove(bot.user)
            winner = random.choice(users)
    if winner is not None:
        endembed = discord.Embed(title="{}".format(prize),
                                  description=f"Winner: {winner.mention} \nHosted by: {ctx.author.mention}",
                                  color=0x00ccff, timestamp=ctx.message.created_at)
        endembed.set_author(name='🎉Giveaway🎉')
        await msg.edit(embed=endembed)
        jumpembed = Embed(description=f"[**Đi Tới Giveaway**]({url})")
        await ctx.send("Chúc mừng {} đã thắng giải **{}** được tổ chức bởi:{}".format(winner.mention, prize, ctx.author.mention),embed=jumpembed)


@giveaway.error
async def giveaway_error(ctx, error):
    await ctx.send(error)




@help.command(name= "random")
async def Random(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`randomn`',inline=False)
    embed.add_field(name='tác dụng',value='`Để random một số ngẫu nhiên nào đó`',inline=False)
    embed.add_field(name='cách dùng',value=f'`{pr}randomn <số muốn quay>`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def giveaway(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`giveaway`',inline=False)
    embed.add_field(name='tác dụng',value='`tạo sk cho member`',inline=False)
    embed.add_field(name='cách dùng',value='`,ga <số giây> <nhan đề>`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def mute(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`mute`',inline=False)
    embed.add_field(name='tác dụng',value='`khóa mõm mấy thằng phạm luật`',inline=False)
    embed.add_field(name='cách dùng',value='`,mute <thằng muốn mute>`',inline=False)
    embed.add_field(name='cách gỡ',value='`unmute <thằng đó>`')
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def ban(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`ban`',inline=False)
    embed.add_field(name='tác dụng',value='`tống cổ bọn phạm luật khỏi sv`',inline=False)
    embed.add_field(name='cách dùng',value='`,ban <thằng ban>`',inline=False)
    embed.add_field(name='cách gỡ',value='`unban <id thằng đó>`')
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def clear(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`clear`',inline=False)
    embed.add_field(name='tác dụng',value='`xóa tin nhắn`',inline=False)
    embed.add_field(name='cách dùng',value='`,clear <số tin muốn xóa>`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def lock(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`lock`',inline=False)
    embed.add_field(name='tác dụng',value='`anti raid`',inline=False)
    embed.add_field(name='cách dùng',value='`,lock`',inline=False)
    embed.add_field(name='cách tắt', value='`,unlock`', inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)



@help.command()
async def poll(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='poll`',inline=False)
    embed.add_field(name='tác dụng',value='`mở quộc thăm giò`',inline=False)
    embed.add_field(name='cách dùng',value='`,poll <nhan đề> `',inline=False)
    embed.add_field(name='cách dùng',value='`,poll test`')
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)




@help.command()
async def ib(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`dms`',inline=False)
    embed.add_field(name='tác dụng',value='`để id với ng bạn thông qua bot`',inline=False)
    embed.add_field(name='cách dùng',value='`,id <tag người bạn> <nhan đề>`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)





@help.command()
async def botinfo(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`info của bot`',inline=False)
    embed.add_field(name='tác dụng',value='`những thứ lên biết`',inline=False)
    embed.add_field(name='cách dùng',value='`,botinfo`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)


@help.command()
async def afk(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`afk`',inline=False)
    embed.add_field(name='tác dụng',value='`bật chế độ afk`',inline=False)
    embed.add_field(name='cách dùng',value='`,afk [lý do]`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def say(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`say`',inline=False)
    embed.add_field(name='tác dụng',value='`nói chuyện bằng bót`',inline=False)
    embed.add_field(name='cách dùng',value='`,say <từ bạn muốn nói>`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def rep(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`rép`',inline=False)
    embed.add_field(name='tác dụng',value='`trả lời chuyện bằng bót`',inline=False)
    embed.add_field(name='cách dùng',value='`,rep <từ bạn muốn nói>`',inline=False)
    embed.add_field(name='cách dùng sửa',value='`,edit <id từ muốn sửa> <từ thay thế>`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def avatar(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`avatar`',inline=False)
    embed.add_field(name='tác dụng',value='`coi avt người khác`',inline=False)
    embed.add_field(name='cách dùng',value='`,avt <tag 1 ng nào đó>`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)


@help.command()
async def svinfo(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`serverinfo`',inline=False)
    embed.add_field(name='tác dụng',value='`tổng quát sv`',inline=False)
    embed.add_field(name='cách dùng',value='`,svinfo`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)

@help.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.add_field(name='tên lệnh',value='`help`',inline=False)
    embed.add_field(name='tác dụng',value='`cho bạn biết tất cả lệnh bot có`',inline=False)
    embed.add_field(name='cách dùng',value='`,help`',inline=False)
    embed.set_footer(text=f'Cú pháp: <> = bắt buộc, [] = không bắt buộc')
    await ctx.reply(embed=embed)



@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)




@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member,  *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")



#ODk0MDg3MDExMzE1NjM4Mjcz.YVk5ag.ac7rU10HI333MGauczypSAdsxcs
import typing





from datetime import datetime


@bot.command()
async def addrole(ctx,member : discord.Member, role : discord.Role):
    await member.add_roles(role)

@bot.command()
async def unrole(ctx,member : discord.Member, role : discord.Role):

   await member.remove_roles(role)
    


@bot.command()
async def botinfo(ctx):

    inbot = discord.Embed(title=f'Đây là thông tin về bot',description='```discord : 2.0.0a \nPython : 3.11.1 \nOS : Windows```',color=0x00ccff)
    inbot.add_field(name=':name_badge:  Tên bot',value=f'`{bot.user.name}`')
    inbot.add_field(name=':clock1: hoạt động',value='`24/7`')
    inbot.add_field(name='👑 người tạo',value='<@!928489823709331527>')
    inbot.add_field(name='📘 Tạo vào',value=discord.utils.format_dt(ctx.bot.user.created_at,style="R"))
    inbot.set_thumbnail(url=bot.user.avatar)
    inbot.add_field(name='🏓 ping',value=f'`{round(bot.latency * 1000)} ms`')
    inbot.add_field(name='💻 Ram',value=f'`{psutil.virtual_memory().percent} MB`')
    inbot.set_image(url = "https://i.imgur.com/GSX64Rv.jpg")
    await ctx.reply(embed=inbot,mention_author=False)

@bot.command()
async def wanted(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    av = user.avatar.with_size(128)
    await av.save(f"avatar-{user.id}.png")
    img = await make_wanted(user)
    img.save(f"avatar-{user.id}.png")
    file = discord.File(f"avatar-{user.id}.png")
    await ctx.send(file=file)
    os.unlink(f"avatar-{user.id}.png")

async def make_wanted(user):
	from PIL import Image
	img = Image.open("wanted.png").convert("RGBA")
	avatar = Image.open(f"avatar-{user.id}.png").convert("RGBA")
	avatar = avatar.resize((84,84))
	img.paste(avatar,(51,91))
	return img

@bot.command()
async def rip(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    av = user.avatar.with_size(128)


    await av.save(f"ripc.png")
    img = await make_rip(user)
    img.save(f"ripc.png")
    file = discord.File(f"ripc.png")
    await ctx.send(file=file)
    os.unlink(f"ripc.png")

async def make_rip(user):
	from PIL import Image
	img = Image.open("rip.png").convert("RGBA")
	avatar = Image.open(f"ripc.png").convert("RGBA")
	avatar = avatar.resize((355,355))
	img.paste(avatar,(231,397))
	return img




@bot.command()
async def poll(ctx, *, question=None):
    if question == None:
        await ctx.send("Hãy viết một cuộc Bình chọn!")



    pollEmbed = discord.Embed(title="Bình chọn nào!", description=f"{question}",color=0x00ffb3)

    pollEmbed.set_footer(text=f"bởi {ctx.author.display_name}")


    pollEmbed.timestamp = ctx.message.created_at

    await ctx.message.delete()

    msg = await ctx.send(embed=pollEmbed)

    await msg.add_reaction("👍")
    await msg.add_reaction("👎")

##############################################################################################################################


import discord, wikipedia






from gtts import gTTS

from discord import File, ButtonStyle
from discord.ui import Button, View

@bot.command(aliases=['av', 'avt'])
async def avatar(ctx,  member: discord.Member = None):
    if member == None:
        member = ctx.author

    memberAvatar = member.avatar

    avaembed = discord.Embed(color=0xAE0808)
    avaembed.set_image(url=memberAvatar)
    avaembed.set_author(name=f'{member.display_name} Avatar', icon_url=member.avatar)
    avaembed.timestamp = ctx.message.created_at

    hi = Button(label="Avatar Server", style=ButtonStyle.blurple,emoji='📁')


    async def hi_callback(interaction):
        if interaction.user != ctx.author:
            await interaction.send(f"chỉ có {ctx.author} nhấn được thôi", ephemeral=True)
        embed = interaction.message.embeds[0].set_image(url=member.display_avatar).set_author(name=f'{member.display_name} Avatar Server' ,icon_url=member.display_avatar)
        await interaction.response.edit_message(embed=embed)

    hi.callback = hi_callback


    myview = View(timeout=180)
    myview.add_item(hi)
    await ctx.send(embed=avaembed, mention_author=False, view=myview)



##################################################################################################################################
#@bot.event
#async def on_command_error(ctx, error):
    #if isinstance(error, commands.errors.CommandNotFound):
      #  await ctx.reply(
     #       'làm j có lệnh này :/ bấm `,help` mà coi lại lệnh đi',mention_author=False)
    #else:
        #raise error



@bot.command()
async def afk(ctx, *, reason="afk"):
    global afklog
    with open("afk.json", "r") as f:
        afklog = json.load(f)
    if str(ctx.author.id) in afklog:
        del afklog[str(ctx.author.id)]
        with open("afk.json", "w") as f:
            json.dump(afklog, f)
        try:
            cur_nick = ctx.author.nick
            await ctx.author.edit()
        except Exception as e:
            print(e)
        await ctx.reply(f"**{ctx.author.display_name}** Chào mừng bạn trở lại ", mention_author=False)

    else:
        afklog[str(ctx.author.id)] = str(reason)
        with open("afk.json", "w") as f:
            json.dump(afklog, f)
        try:
            cur_nick = ctx.author.nick
            await ctx.author.edit()
        except Exception as e:
            print(e)
        await ctx.reply(f"✅| **{ctx.author.display_name}** đã bật chế độ AFK \nlý Do: **{reason}**",
                        mention_author=False)

@bot.command()
async def chatgpt(ctx, *,arg):
    cookies = {
        'mp_d7d7628de9d5e6160010b84db960a7ee_mixpanel': '%7B%22distinct_id%22%3A%20%2218630f8da0b3b2-0609209a8a36a4-7d5d547c-e1000-18630f8da0c25b%22%2C%22%24device_id%22%3A%20%2218630f8da0b3b2-0609209a8a36a4-7d5d547c-e1000-18630f8da0c25b%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fplatform.openai.com%2Fsignup_ext%3Fapp%3Dchat%26__cf_chl_tk%3DXkIbizS2DgTQ_2Fl5QrfthwcBTW3lpJXpOHRux69oTQ-1675858837-0-gaNycGzNCqU%22%2C%22%24initial_referring_domain%22%3A%20%22platform.openai.com%22%7D',
        'cf_clearance': 'gjRCRzj8EC3Q17k8lkw4kkD9Dn7wXOpVOSF4olDLldA-1676188426-0-1-cbde067b.dc12b9b9.21586d8f-160',
        '_ga': 'GA1.1.1618815198.1675858772',
        'intercom-device-id-dgkjq2bp': '30235d5a-1a64-48f3-b2ff-eb50304317fb',
        '_ga_9YTZJE58M9': 'GS1.1.1686055284.7.0.1686055284.0.0.0',
        'intercom-session-dgkjq2bp': 'R2xPR2RMNmVpMFFvSzduQXpjckZBODRkNEwrcDhwZkJXalA5bW9WTFNqNnltYi9nelZHWUtRSGNCOW5Xd20zYi0tZE9yN0szOXdnaHFkUXdwdGM2c25hQT09--c921181815618f2ffc554bda761801feb85c4944',
        '__Host-next-auth.csrf-token': '5ac55f5e29e1259d66c29c48a945f14bbeb3762da1ac57801fb0cbda739f578b%7Cdee8c561f6aadd888e2b58b27a9de1a4d44e28a28291af3f4eb89b4e048bca4b',
        '_cfuvid': 'EoOyDStQZnD2W5sjZL9OI.9HsrDLl5lzHzoV8dQ9CLE-1693484121075-0-604800000',
        'cf_clearance': 'MSAEkPzCqIgHWdI.nNP_g7aS4TnI.XfZ7w6svCW1kGM-1693624582-0-1-169b5711.71a874ae.42e6ad0d-0.2.1693624582',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fchat.openai.com%2F',
        '__cf_bm': '_P94C8BzBuM3u8o3yNTIFs4lgntcAQhKuANKjyl4FLg-1693664714-0-AUOSHJlqZvn3iylztKCNm2EOkbfAU7GW3J4PW0hFsLHixCZMHw4RNZnO6NiHVAM/d8Xvbbq9fzigVZ1PpBS5Alg=',
        '__Secure-next-auth.session-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..uRtNc7VfSE-n6SS4.QP1AYPJvRWr16RJ4sVovXzvNkEU9XKL3VttFSqFY6OauW4cMmDqQWXmuWwZwrNXvVjB-kMB-9E70cYX20fekBizMB9Nwwm6wu2nwzcCtRPfFpvpaRhyQmAD-jPKtMCz6Rn3wAegk_QbEMFcz2KKEI3YqWUCv49WXYj4U0NRCr6Qp_SVdqNWxgpX98f0eAqFbRL5GmNJafnPSHCHGhdbYKNwJh1ybM0xtmssrYfqiy-Icu0_6MpXnPrCr9_U78dw0TBEhhvhTAs8INkUC9UXDfTnvce45jKBelQDNJyaqeoPMk9yd67lEahwEBwioxPVvIQo3tMXgC0pw_yWA47_fjztnddgue6QLAj-7U3s3Rd3Vmt41lKPpXd1icFt8VEanhcGyRBAPN4oQPp_RFNV_Zs0-mgsmzMhtiZkwx9c2X_xbT44dRi3y-P_2v6lsgFkOKLTui1wE0ItAOBgJgFiv7d5irtJ85svgXo3Avj_leg8thTct7xz3KS7rpcGFBX43fEt-CGb3FBJhZGU_2q3UbGW9siCOHtBnU0tJQSP7nUwuV4FEd_K7RId4-umQXkopQDA-DO74xB-EHtTJRWwBM660nQIA-iprzHWxU0wgNwt1Mmz49aPMOKBUXp_gZTUkkD6kyq1qvSU6TqivwIsJrmtNUrfeoK4CjWvZdLtUtNwkIffMiV5k2SKpyKLlp0W0bD-2dvm6yMADC0-LqhV3bTuLoeoqdE8fEH_zJL2wSfPjcCozAp9ldNEHxZ-UaAhHNdVVAm3p3hjfkvE0y6MevRt5YMUW8wDJW_bQQRXKQAPOgEh4coJO2aMeOks0RL87zqYhWLqadBAALu6FpRLW5xa_cegltACKcbW3F0i2hxM7Yz_0d2M4fLxhYwlnkMhBCqA4eSSajN4BtmVHVA1vj6mKp17PPuInlTyY2du0bKIfbeY84oOwVNeotzUIMKt3iKOgxgh7rF5e09wkcAveT3nmJ-Km7PKubT3T-5BX9vWXpikSkO65S_fian9Zx0oKsbdDiOcv4GZeR_TCcQv3AJA3uHe2AVDcXZe5oXbz-6CY4qvQP8ja1T8FVBq_Ri174Yg0QWyDhNWGJKbnUnPL1A5HTPvHAA8ZJaRf__bEuOXKaJ_t75OzzbbtL3lJY5pjcMpFAAeIn-2f7RtBRxF-qvdoesW0-KxQZm2GbGbbHHzSIg_qlAsB8NaLTaNKjDiJt8v6lx4myPK0MEX8wxPrHGZwX_mEoO5mh2jAv61_Xu_37bltCoB1aoWk71gdV4iYU6HKR-6Cpva81Gwzv5exeHZr2pVvb1CKbcW1rKEsOgjlzYfe3b4qGGg4IdF_YDQ11jDSilntJ_0WMf84MUjupqKRp1ZCE88m6qXS5UJpJhwrrHBFxVHJ5TtnFy7xFxT774kyVjfscWwbdoVQXkxaxxmhnFZh-ZdzNRBLmi6RMukDu4N6ft6sxwceS24lFZMWAYXtfr3PvmdRcFVLmv2oKubvZOrVfhxuw0pQXkLCQJftqyQXeELtva8DhbShg7kTq1VpJtrZbrTnfRMEqjWPOEFJmIQxwLQe0T8zqYD8CBCanXYSqJqzAep8Eel2S6VBzXT4ST3sOXBt3iSD3yn5o3nDAYfHVaQ0C7gBpJJcfqaWfFT27lTTMHy7zF6bFCmYRZLIZsJITBHGDTxX8rIAK9eeG-PYzQImuswIwH3arObTtfrMtAL_w_SDX9_0K2TDIm1TA0vJYIQSJzByxLnty463cs1voMc-0FXnSkyPnAXX1SAwLjj5UH0ejfAycVldHQbwf0GJcLz1INwtHBym93-ltIQrbsx14um2zITkaqHHvxvRlGhrfcnFGMHbdU7IrrBYjF06TD7MvFiFKZvCVWyhbc3MAGLicQL-NUOKIeSHBFXT5JfDHoJCFEGtIc_Ko2YRIDgjOPoWpSaO5euQfU5vDvXDoPfnrFAmrkDlitzxmvirXt_F9HIOOMxB9mSbjwO1TDm-mtBWf9XnahTrsqGKOtsic0_k6n-vn3Hc9ACB4X7GzQCKCjjlusk5_p5efiqhr1gX-6CRktqdqzWH3-eU46px0zHTd2Rp7y0AoSba3rjO5K3ti3j3yKughrfB-Fl-fbVOp4cewVSHdpOmmpv9ukZVLW_irKI21yzUoXNOgCKAh484K1E0l-6oy8bkH8bCxFCsaK4E80i8juIzGSA-p1RWo4nmbZmUDlGRSnPmB4iXndXnaculie_oLJzpKH9cvNk9yVRresGXKTIzZ0kkOdSVqB3gtkEke2pu5JjUxU7g6X8XQjuTwRbNMmI1rCjejXgBINpCMBsH8H2yz1rHU8WvHdRO4mKyDtOX2DgSQIZleoSLzA7IDfllrxIaoJwTgKUwlSXZCxBouubK2vZtPc5oIIHdWxa-qzbG2I_EyrGNgcqsBt83NfCMmqvAZt3agmB_yQFOuzmr2kPt3-CHs8e5LNKPvfG431PrVKrcOeYyJcDbJv9oQ_RUG1t_1ooGz57VLiJDN-HZz6pu8pNRID9Vy8k44i-y6B_5tgEEcbhPtnh0sJER_jj1NuE4VFn52Y5LnafpONijpCCwrmuFEMG3CEIpNaN59HNkDJtpoBErOvUR33wWekoyFcaPVrYO2uuNnnRwfRKHyN2duhnrvx3qdeSw11JMdSfvoRNqkvkmcYHb3jVyp1Z7gpOsbjoJj9V4z5bBi6wlYRM6eQ0wb572T44TwUp9DK6Oauqf9BaR1wk4ZOPpK_iQ7Ppu-5cwTZIad_wkFIAceNWSE8D4W0qVPLqleKGXOH5Vs8zLuHGeQcL_oOe83k_lyPmf9HBmAyEhCGNh9rlxlmA8H9Ni0Jn40IjoUg.hK-u4-e0iTpwgaI_4FAUNg',
        '_uasid': '"Z0FBQUFBQms4MGpsYzlDNDhQdTh0NUY1X0pHaGx1UjRNTW1YZUFIMHVFUk1QRmhWb3NGZDZCS1FIbWNMc3lJdkRKNEFFeW9QS09PbF8xcWVVM2QxZ1pDdE5Mal9XZGFSS2Q4QzJiVEJxVmFfaTF3WUdmQlNKZEpIcFN1SXFxbHpTWUdveTNsXy1TSXlBdGlCTGpVSTlSTTFQTl95M1Uybkd4TDNkODhvQS1EWWMwNWNfUFJRQjZ6SXB2Ymk0VjRBQkM2ZW9GWTJYR3FySG9NVmlkNVpGNFIySW1kZV8taUctODIxQ2NDYlc3WEFTbGZjdFQxR2hWamJ5LUpuVE1tMno2TXRadHpBT3NaM1RRWGtFcTRkc3JZdXBDeGQ5QXF4T3Q3b1kwdjhLX3g3aGZlZmlBWnJEZjVtTU1ONjJlbzZVeTZXdEduRUxBbWw5aTNDbk5Pbkc2enNlLWdIVTJDR0hnPT0="',
        '_dd_s': 'rum=0&expire=1693666528779',
        }

    headers = {
        'authority': 'chat.openai.com',
        'accept': 'text/event-stream',
        'accept-language': 'en-US',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJoY2NndDQ0NDRAZGNjdGIuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItYVFlNzJkSXVTZkxkcW5qT1h2TGJTVndnIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2M2RjYmM2YjZhYzBiNTFkMGFjMGFiMWYiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjkzNjI0NTg5LCJleHAiOjE2OTQ4MzQxODksImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.M6R9SLjR31v9EYmMq2Q_-nfqqJwg2hZwA6m4YekLQ9F3w2IL0LS1SnatuOFZjC3LPwxJo9LFI6UH0-A0emNYbqVnmK9Qy4aZrMF-tOvpHzuHJr9eUS6UjA43GAOKMAoj4KcVRbq7RHzu0ES91GqWus9jGbrh-trCu5njdvzo1RrIai1RzcXD5ZoWK49we4BBnefx618-txK0vQ81oLcDGHTV_IduHJBn1H0-n3NIuiJ85Luo_Vf7lW0Bg2jKcl5r8lyVY5lJ8FoJX7JkFJH1-5a_kmCxhtcfKvwyDhwu4XYvodVQGKXrNqBAAOUmX3Ck_pZJsiz6Xs4P2O8-YdRTVw',
        'content-type': 'application/json',
        # 'cookie': 'mp_d7d7628de9d5e6160010b84db960a7ee_mixpanel=%7B%22distinct_id%22%3A%20%2218630f8da0b3b2-0609209a8a36a4-7d5d547c-e1000-18630f8da0c25b%22%2C%22%24device_id%22%3A%20%2218630f8da0b3b2-0609209a8a36a4-7d5d547c-e1000-18630f8da0c25b%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fplatform.openai.com%2Fsignup_ext%3Fapp%3Dchat%26__cf_chl_tk%3DXkIbizS2DgTQ_2Fl5QrfthwcBTW3lpJXpOHRux69oTQ-1675858837-0-gaNycGzNCqU%22%2C%22%24initial_referring_domain%22%3A%20%22platform.openai.com%22%7D; cf_clearance=gjRCRzj8EC3Q17k8lkw4kkD9Dn7wXOpVOSF4olDLldA-1676188426-0-1-cbde067b.dc12b9b9.21586d8f-160; _ga=GA1.1.1618815198.1675858772; intercom-device-id-dgkjq2bp=30235d5a-1a64-48f3-b2ff-eb50304317fb; _ga_9YTZJE58M9=GS1.1.1686055284.7.0.1686055284.0.0.0; intercom-session-dgkjq2bp=R2xPR2RMNmVpMFFvSzduQXpjckZBODRkNEwrcDhwZkJXalA5bW9WTFNqNnltYi9nelZHWUtRSGNCOW5Xd20zYi0tZE9yN0szOXdnaHFkUXdwdGM2c25hQT09--c921181815618f2ffc554bda761801feb85c4944; __Host-next-auth.csrf-token=5ac55f5e29e1259d66c29c48a945f14bbeb3762da1ac57801fb0cbda739f578b%7Cdee8c561f6aadd888e2b58b27a9de1a4d44e28a28291af3f4eb89b4e048bca4b; _cfuvid=EoOyDStQZnD2W5sjZL9OI.9HsrDLl5lzHzoV8dQ9CLE-1693484121075-0-604800000; cf_clearance=MSAEkPzCqIgHWdI.nNP_g7aS4TnI.XfZ7w6svCW1kGM-1693624582-0-1-169b5711.71a874ae.42e6ad0d-0.2.1693624582; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; __cf_bm=_P94C8BzBuM3u8o3yNTIFs4lgntcAQhKuANKjyl4FLg-1693664714-0-AUOSHJlqZvn3iylztKCNm2EOkbfAU7GW3J4PW0hFsLHixCZMHw4RNZnO6NiHVAM/d8Xvbbq9fzigVZ1PpBS5Alg=; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..uRtNc7VfSE-n6SS4.QP1AYPJvRWr16RJ4sVovXzvNkEU9XKL3VttFSqFY6OauW4cMmDqQWXmuWwZwrNXvVjB-kMB-9E70cYX20fekBizMB9Nwwm6wu2nwzcCtRPfFpvpaRhyQmAD-jPKtMCz6Rn3wAegk_QbEMFcz2KKEI3YqWUCv49WXYj4U0NRCr6Qp_SVdqNWxgpX98f0eAqFbRL5GmNJafnPSHCHGhdbYKNwJh1ybM0xtmssrYfqiy-Icu0_6MpXnPrCr9_U78dw0TBEhhvhTAs8INkUC9UXDfTnvce45jKBelQDNJyaqeoPMk9yd67lEahwEBwioxPVvIQo3tMXgC0pw_yWA47_fjztnddgue6QLAj-7U3s3Rd3Vmt41lKPpXd1icFt8VEanhcGyRBAPN4oQPp_RFNV_Zs0-mgsmzMhtiZkwx9c2X_xbT44dRi3y-P_2v6lsgFkOKLTui1wE0ItAOBgJgFiv7d5irtJ85svgXo3Avj_leg8thTct7xz3KS7rpcGFBX43fEt-CGb3FBJhZGU_2q3UbGW9siCOHtBnU0tJQSP7nUwuV4FEd_K7RId4-umQXkopQDA-DO74xB-EHtTJRWwBM660nQIA-iprzHWxU0wgNwt1Mmz49aPMOKBUXp_gZTUkkD6kyq1qvSU6TqivwIsJrmtNUrfeoK4CjWvZdLtUtNwkIffMiV5k2SKpyKLlp0W0bD-2dvm6yMADC0-LqhV3bTuLoeoqdE8fEH_zJL2wSfPjcCozAp9ldNEHxZ-UaAhHNdVVAm3p3hjfkvE0y6MevRt5YMUW8wDJW_bQQRXKQAPOgEh4coJO2aMeOks0RL87zqYhWLqadBAALu6FpRLW5xa_cegltACKcbW3F0i2hxM7Yz_0d2M4fLxhYwlnkMhBCqA4eSSajN4BtmVHVA1vj6mKp17PPuInlTyY2du0bKIfbeY84oOwVNeotzUIMKt3iKOgxgh7rF5e09wkcAveT3nmJ-Km7PKubT3T-5BX9vWXpikSkO65S_fian9Zx0oKsbdDiOcv4GZeR_TCcQv3AJA3uHe2AVDcXZe5oXbz-6CY4qvQP8ja1T8FVBq_Ri174Yg0QWyDhNWGJKbnUnPL1A5HTPvHAA8ZJaRf__bEuOXKaJ_t75OzzbbtL3lJY5pjcMpFAAeIn-2f7RtBRxF-qvdoesW0-KxQZm2GbGbbHHzSIg_qlAsB8NaLTaNKjDiJt8v6lx4myPK0MEX8wxPrHGZwX_mEoO5mh2jAv61_Xu_37bltCoB1aoWk71gdV4iYU6HKR-6Cpva81Gwzv5exeHZr2pVvb1CKbcW1rKEsOgjlzYfe3b4qGGg4IdF_YDQ11jDSilntJ_0WMf84MUjupqKRp1ZCE88m6qXS5UJpJhwrrHBFxVHJ5TtnFy7xFxT774kyVjfscWwbdoVQXkxaxxmhnFZh-ZdzNRBLmi6RMukDu4N6ft6sxwceS24lFZMWAYXtfr3PvmdRcFVLmv2oKubvZOrVfhxuw0pQXkLCQJftqyQXeELtva8DhbShg7kTq1VpJtrZbrTnfRMEqjWPOEFJmIQxwLQe0T8zqYD8CBCanXYSqJqzAep8Eel2S6VBzXT4ST3sOXBt3iSD3yn5o3nDAYfHVaQ0C7gBpJJcfqaWfFT27lTTMHy7zF6bFCmYRZLIZsJITBHGDTxX8rIAK9eeG-PYzQImuswIwH3arObTtfrMtAL_w_SDX9_0K2TDIm1TA0vJYIQSJzByxLnty463cs1voMc-0FXnSkyPnAXX1SAwLjj5UH0ejfAycVldHQbwf0GJcLz1INwtHBym93-ltIQrbsx14um2zITkaqHHvxvRlGhrfcnFGMHbdU7IrrBYjF06TD7MvFiFKZvCVWyhbc3MAGLicQL-NUOKIeSHBFXT5JfDHoJCFEGtIc_Ko2YRIDgjOPoWpSaO5euQfU5vDvXDoPfnrFAmrkDlitzxmvirXt_F9HIOOMxB9mSbjwO1TDm-mtBWf9XnahTrsqGKOtsic0_k6n-vn3Hc9ACB4X7GzQCKCjjlusk5_p5efiqhr1gX-6CRktqdqzWH3-eU46px0zHTd2Rp7y0AoSba3rjO5K3ti3j3yKughrfB-Fl-fbVOp4cewVSHdpOmmpv9ukZVLW_irKI21yzUoXNOgCKAh484K1E0l-6oy8bkH8bCxFCsaK4E80i8juIzGSA-p1RWo4nmbZmUDlGRSnPmB4iXndXnaculie_oLJzpKH9cvNk9yVRresGXKTIzZ0kkOdSVqB3gtkEke2pu5JjUxU7g6X8XQjuTwRbNMmI1rCjejXgBINpCMBsH8H2yz1rHU8WvHdRO4mKyDtOX2DgSQIZleoSLzA7IDfllrxIaoJwTgKUwlSXZCxBouubK2vZtPc5oIIHdWxa-qzbG2I_EyrGNgcqsBt83NfCMmqvAZt3agmB_yQFOuzmr2kPt3-CHs8e5LNKPvfG431PrVKrcOeYyJcDbJv9oQ_RUG1t_1ooGz57VLiJDN-HZz6pu8pNRID9Vy8k44i-y6B_5tgEEcbhPtnh0sJER_jj1NuE4VFn52Y5LnafpONijpCCwrmuFEMG3CEIpNaN59HNkDJtpoBErOvUR33wWekoyFcaPVrYO2uuNnnRwfRKHyN2duhnrvx3qdeSw11JMdSfvoRNqkvkmcYHb3jVyp1Z7gpOsbjoJj9V4z5bBi6wlYRM6eQ0wb572T44TwUp9DK6Oauqf9BaR1wk4ZOPpK_iQ7Ppu-5cwTZIad_wkFIAceNWSE8D4W0qVPLqleKGXOH5Vs8zLuHGeQcL_oOe83k_lyPmf9HBmAyEhCGNh9rlxlmA8H9Ni0Jn40IjoUg.hK-u4-e0iTpwgaI_4FAUNg; _uasid="Z0FBQUFBQms4MGpsYzlDNDhQdTh0NUY1X0pHaGx1UjRNTW1YZUFIMHVFUk1QRmhWb3NGZDZCS1FIbWNMc3lJdkRKNEFFeW9QS09PbF8xcWVVM2QxZ1pDdE5Mal9XZGFSS2Q4QzJiVEJxVmFfaTF3WUdmQlNKZEpIcFN1SXFxbHpTWUdveTNsXy1TSXlBdGlCTGpVSTlSTTFQTl95M1Uybkd4TDNkODhvQS1EWWMwNWNfUFJRQjZ6SXB2Ymk0VjRBQkM2ZW9GWTJYR3FySG9NVmlkNVpGNFIySW1kZV8taUctODIxQ2NDYlc3WEFTbGZjdFQxR2hWamJ5LUpuVE1tMno2TXRadHpBT3NaM1RRWGtFcTRkc3JZdXBDeGQ5QXF4T3Q3b1kwdjhLX3g3aGZlZmlBWnJEZjVtTU1ONjJlbzZVeTZXdEduRUxBbWw5aTNDbk5Pbkc2enNlLWdIVTJDR0hnPT0="; _dd_s=rum=0&expire=1693666528779',
        'origin': 'https://chat.openai.com',
        'referer': 'https://chat.openai.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
    }

    json_data = {
        'action': 'next',
        'messages': [
            {
                'id': 'aaa2de37-90e4-4b0b-a699-134f2adda7e5',
                'author': {
                    'role': 'user',
                },
                'content': {
                    'content_type': 'text',
                    'parts': [
                            'hello\n',
                    ],
                },
                'metadata': {},
            },
        ],
        'conversation_id': 'cbe255c1-127b-493d-9069-1dae59001b7b',
        'parent_message_id': '06f819f9-ca1f-45e6-80d2-1db0e344e598',
        'model': 'text-davinci-002-render-sha',
        'timezone_offset_min': -420,
        'suggestions': [],
        'history_and_training_disabled': False,
        'arkose_token': None,
    }

    response = requests.post('https://chat.openai.com/backend-api/conversation', cookies=cookies, headers=headers, json=json_data)
    rp = response['message']
    await ctx.reply(f"```{rp}```")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if (message.author.bot):
        return
    with open("afk.json", "r") as f:
        afklog = json.load(f)
    if str(message.author.id) in afklog and "afk" not in message.content:
        del afklog[str(message.author.id)]
        with open("afk.json", "w") as f:
            json.dump(afklog, f)

        try:

            nick = message.author.nick
            await message.author.edit()

        except Exception as e:
            print(e)
            print(f"Bạn thiếu quyền tại guild {message.guild.name} ID:{message.guild.id}")
        await message.channel.send(f"Chào mừng trở lại **{message.author.display_name}**" ,mention_author=False)
    for member in message.mentions:
        if str(member.id) != str(message.author.id):
            if str(member.id) in afklog:
                reason = afklog[str(member.id)]
                await message.channel.send(f" **{member.display_name}** đang afk với lý do: **{reason}** ")


#token = "MTEwMjU4OTExODc0NTE3MDAwMA.Gwq28k.AJrga5ESyGEuOgpGlsXpcYOnnDTXGeDrHDbP10"
bot.run(bot_token.TOKEN)
