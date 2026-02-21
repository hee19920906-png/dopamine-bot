import discord
from discord.ext import commands
from datetime import datetime
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('---')
    print(f'성공! {bot.user} 이름으로 로그인했습니다.')
    print('---')

# [1. 입장 로그 기능]
@bot.event
async def on_member_join(member):
    target_name = '👋ㆍ신규멤버'
    channel = discord.utils.get(member.guild.text_channels, name=target_name)
    
    if channel:
        now = datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분')
        embed = discord.Embed(
            title="💜 Dopamine 💜 서버에 오신것을 환영합니당!",
            description=f"{member.mention} 님! 환영합니다!\n원활한 서버 이용을 위한 단계를 숙지 해주세요!",
            color=0x8A2BE2,
            timestamp=datetime.now()
        )
        embed.add_field(name="✅ 필수 확인 단계", value="📢ㆍ서버공지 채널 읽어보기\n🐣ㆍ신규가이드 채널 읽어보기", inline=False)
        embed.add_field(name="✨ 활동 가이드 ✨", value="ㆍ즐겁게 활동하기\nㆍ각종 문의사항은 관리자에게 언제든 말씀해 주세요.", inline=False)
        embed.add_field(name="📅 입장 시간", value=now, inline=False)
        
        if member.display_avatar:
            embed.set_thumbnail(url=member.display_avatar.url)
        
        embed.set_footer(text=f"💜도파민💜 서버의 소중한 멤버가 되어주셔서 감사합니다!\n유저 ID: {member.id}")
        await channel.send(embed=embed)
        print(f"[{member.display_name}]님 입장 메시지 전송 완료")

# [2. 퇴장 로그 기능]
@bot.event
async def on_member_remove(member):
    target_name = '☁️ㆍ멤버퇴장'
    channel = discord.utils.get(member.guild.text_channels, name=target_name)
    
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
        print(f"[{member.display_name}]님 퇴장 메시지 전송 완료")

token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
