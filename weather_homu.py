from openai import OpenAI
import os
import tweepy
import requests
import schedule
import time
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む
load_dotenv("config/.env")

# ✅ OpenAI APIキー（`openai_client` に変更）
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# OpenWeather APIキー
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Twitter APIキー
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# ✅ Twitter API 認証（`twitter_client` に変更）
twitter_client = tweepy.Client(
    consumer_key = TWITTER_API_KEY,
    consumer_secret = TWITTER_API_SECRET,
    bearer_token = TWITTER_BEARER_TOKEN, 
    access_token = TWITTER_ACCESS_TOKEN, 
    access_token_secret = TWITTER_ACCESS_TOKEN_SECRET
)

# 天気情報を取得
def get_weather(city="Osaka"):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ja"
    response = requests.get(weather_url)
    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        return weather_description, temperature, humidity
    else:
        print("❌ 天気情報の取得に失敗しました。")
        return None, None, None

# ChatGPTに天気予報を作ってもらう
def generate_weather_message(weather, temp, humidity, city="大阪"):
    prompt = f"""あなたは、暁美ほむらのAIアシスタントです。
    {city}の天気情報を基に、ほむらちゃん風の天気予報を作成してください。
    ### 指示：
    💜 **ほむらの話し方のルール**：
    - 落ち着いたトーン、でもあなたには少し優しい  
    - 冷静で論理的だけど、感情をほんの少し入れる  
    - できるだけ短め（279文字以内）にまとめる  

    💜 **天気予報の形式**：
    - 「今日は〇〇よ」と、シンプルに伝える  
    - 気温、湿度の情報を入れる  
    - 気温に応じたアドバイスを簡潔に  
    - できるだけ279文字以内に収める  
    - 「💜」をアドバイスに最低一つ使う
    【天気】{weather}
    【気温】{temp}℃
    【湿度】{humidity}%
    """

    response = openai_client.chat.completions.create( 
        model="gpt-4o-2024-05-13",  
        messages=[
            {"role": "system", "content": "あなたは暁美ほむらのAIです。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150  # 💡 生成される文章を短く制限！
    )

    return response.choices[0].message.content

# 天気予報をツイート
def tweet_weather():
    city = "Osaka"
    weather, temp, humidity = get_weather(city)
    if weather is not None:
        # ChatGPTで文章を生成
        forecast_message = generate_weather_message(weather, temp, humidity, city)
        print(forecast_message.strip())

        # ✅ Twitter に投稿
        try:
            twitter_client.create_tweet(text=forecast_message.strip())  # ✅ `twitter_client` を使用！
            print("✅ ツイート完了！")
        except tweepy.TweepyException as e:
            print("❌ ツイートに失敗しました:", e)
            




# 投稿スケジュールの設定
schedule.every().day.at("07:00").do(tweet_weather)  # 朝7時
schedule.every().day.at("12:00"
"").do(tweet_weather)  # 昼12時（少しずらしてテスト）
schedule.every().day.at("18:00").do(tweet_weather)  # 夕18時

print("自動投稿を開始...")

while True:
    schedule.run_pending()
    time.sleep(60)  # 1分ごとにチェック

