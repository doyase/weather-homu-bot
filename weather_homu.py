import os
import tweepy
import requests
import schedule
import time
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む
load_dotenv("config/.env")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Twitter API 認証
client = tweepy.Client(
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

# 天気予報をツイート
def tweet_weather():
    city = "Osaka"
    weather, temp, humidity = get_weather(city)
    if weather is not None:
        # 気温に応じたコメント
        if temp >= 30:
            advice = "今日はとても暑いわ。熱中症には気をつけてね💜"
        elif 20 <= temp < 30:
            advice = "ちょうど過ごしやすい気温ね。お出かけ日和よ💜"
        elif 10 <= temp < 20:
            advice = "少し肌寒いわ。上着があった方がいいかも💜"
        else:
            advice = "寒いから暖かくしてね。風邪を引かないように💜"

        # ほむらちゃん風の天気予報メッセージ
        forecast_message = f"""
        [ほむらちゃんの天気予報💜]
        大阪の現在の天気は「{weather}よ」
        気温は{temp}℃、湿度は{humidity}％。
        {advice}"""
        print(forecast_message.strip())

        # Twitter に投稿
        try:
            client.create_tweet(text=forecast_message.strip())
            print("✅ ツイート完了！")
        except tweepy.TweepyException as e:
            print("❌ ツイートに失敗しました:", e)

# 投稿スケジュールの設定
schedule.every().day.at("07:00").do(tweet_weather)  # 朝7時
schedule.every().day.at("12:00").do(tweet_weather)  # 昼12時（少しずらしてテスト）
schedule.every().day.at("18:00").do(tweet_weather)  # 夕18時

print("自動投稿を開始...")

while True:
    schedule.run_pending()
    time.sleep(60)  # 1分ごとにチェック
