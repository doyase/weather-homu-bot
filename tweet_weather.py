import os
import tweepy
from weather_homu import get_weather  # weather_homu から get_weather 関数をインポート
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む
load_dotenv("config/.env")

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Twitter API 認証
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

def tweet_weather():
    city = "Osaka"
    weather, temp, humidity = get_weather(city)
    if weather is not None:
        # 気温に応じてほむらちゃんのコメントを設定
        if temp >= 30:
            advice = "今日はとても暑いわ。熱中症には気をつけてね💜"
        elif 20 <= temp < 30:
            advice = "ちょうど過ごしやすい気温ね。お出かけ日和よ💜"
        elif 10 <= temp < 20:
            advice = "少し肌寒いわ。上着があった方がいいかも💜"
        else:
            advice = "寒いから暖かくしてね。風邪を引かないように💜"

        # ほむらちゃん風の天気予報メッセージを作成
        forecast_message = f"""
        [ほむらちゃんの天気予報💜]
        大阪の現在の天気は「{weather}よ」
        気温は{temp}℃、湿度は{humidity}％。
        {advice}"""
        print(forecast_message.strip())

        # 天気予報をツイート
        try:
            api.update_status(forecast_message.strip())
            print("✅ ツイート完了！")
        except tweepy.TweepError as e:
            print("❌ ツイートに失敗しました:", e)
