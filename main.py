import discord
from discord.ext import commands
import os
from datetime import datetime

intents = discord.Intents.default()
intents.members = True       
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'성공! {bot.user.name} 이름으로 로그인했습니다.')

@bot.event
async def on_member_remove(member):
    # 디스코드 채널 이름이 '입퇴장-로그'여야 합니다.
    channel = discord.utils.get(member.guild.text_channels, name="입퇴장-로그")
    if channel:
        now = datetime.now().strftime('%Y년 %m월 %d일 %H:%M')
        embed = discord.Embed(
            title="멤버 퇴장 알림 (관리자용)",
            description=f"**{member.name}** 님이 서버를 떠나셨습니다.",
            color=discord.Color.red()
        )
        embed.add_field(name="유저 정보", value=f"ID: {member.id}\n닉네임: {member.mention}", inline=False)
        embed.add_field(name="퇴장 시각", value=now, inline=False)
        embed.set_footer(text="Dopamine 멤버 관리 로그")
        await channel.send(embed=embed)

token = os.getenv('DISCORD_TOKEN')
bot.run(token)
