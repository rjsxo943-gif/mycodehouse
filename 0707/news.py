from datetime import datetime
import asyncio
import os
import edge_tts


# =========================
# 숫자 입력 함수
# =========================

def input_int(message):
    value = input(message)
    return int(value)


# =========================
# 음성 파일 생성 함수
# =========================

async def make_voice(text, filename):
    #voice = "ko-KR-InJoonNeural"   # 남자 한국어 목소리
    voice = "ko-KR-SunHiNeural"  # 여자 한국어 목소리

    tts = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate="+0%",
        pitch="+0Hz"
    )

    await tts.save(filename)


# =========================
# 경기 결과 입력 받기
# =========================

place = input("경기가 열린 곳은? ")
time = input("경기가 열린 시간은? ")
opponent = input("상대 팀은? ")

goals = input_int("손흥민은 몇 골 넣었나요? ")
aids = input_int("도움은 몇 개인가요? ")

score_me = input_int("손흥민 선수가 속한 팀이 넣은 골 수는? ")
score_you = input_int("상대 팀이 넣은 골 수는? ")


# =========================
# 기사 작성하기
# =========================

news = "[프리미어 리그 속보 - " + str(datetime.now()) + "]\n\n"

news += "손흥민 선수는 " + place + "에서 " + time + "에 열린 경기에 출전하였습니다.\n"
news += "상대 팀은 " + opponent + "입니다.\n\n"


# 승패 결과 기사
if score_me > score_you:
    news += "손흥민 선수의 팀이 " + str(score_me) + "골을 넣어 "
    news += str(score_you) + "골을 넣은 상대 팀을 이겼습니다.\n"

elif score_me < score_you:
    news += "손흥민 선수의 팀이 " + str(score_me) + "골을 넣어 "
    news += str(score_you) + "골을 넣은 상대 팀에게 졌습니다.\n"

else:
    news += "두 팀은 " + str(score_me) + "대" + str(score_you) + "로 비겼습니다.\n"


# 손흥민 활약 기사
if goals > 0 and aids > 0:
    news += "손흥민 선수는 " + str(goals) + "골에 도움 " + str(aids)
    news += "개를 기록하며 경기에서 맹활약했습니다.\n"

elif goals > 0 and aids == 0:
    news += "손흥민 선수는 " + str(goals) + "골을 기록하며 팀에 큰 기여를 했습니다.\n"

elif goals == 0 and aids > 0:
    news += "손흥민 선수는 골은 없었지만 도움 " + str(aids)
    news += "개를 기록하며 팀 공격에 공헌했습니다.\n"

else:
    news += "아쉽게도 이번 경기에서 손흥민 선수는 공격 포인트를 기록하지 못했습니다.\n"


# =========================
# 기사 출력
# =========================

print()
print("========== 생성된 기사 ==========")
print(news)


# =========================
# 음성 파일 만들고 재생하기
# =========================

filename = "news_Son.mp3"

asyncio.run(make_voice(news, filename))

print()
print("음성 파일 생성 완료:", filename)

os.startfile(filename)