暁美ほむら 天気予報 bot（非公式）
このプロジェクトは、Pythonを使用して X（旧Twitter）に自動で天気予報を投稿 するbotです。
OpenWeather API から天気データを取得し、ChatGPT（OpenAI API）を活用して ほむらちゃん風 の天気予報を生成します。

🔧 使用技術
言語: Python
API:
OpenWeather API（天気データ取得）
Twitter API v2（自動投稿）
OpenAI API（ChatGPT）（天気予報の文章生成）
ライブラリ:
Tweepy（Twitter API 操作）
Schedule（定期実行）
Requests（APIリクエスト）
dotenv（環境変数管理）
OpenAI（ChatGPT API）
📌 機能
✅ 自動天気予報ツイート

毎日 07:00 / 12:00 / 18:00 に天気予報を自動投稿
✅ ChatGPT による文章生成

OpenAI API を利用し、暁美ほむら風のセリフ で天気予報を投稿
気温や湿度に応じたアドバイスも追加
✅ .env による APIキー管理

.env を使い、APIキーを安全に管理（GitHub には含めない）
✅ 手動でも実行可能

スケジュール設定だけでなく、tweet_weather() を手動実行することも可能

🚀 使い方
1️⃣ .env ファイルを作成し、APIキーを設定

ini
コピーする
編集する
OPENWEATHER_API_KEY=your_openweather_api_key
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
OPENAI_API_KEY=your_openai_api_key
2️⃣ 必要なライブラリをインストール

sh
コピーする
編集する
pip install -r requirements.txt
3️⃣ weather_homu.py を実行

sh
コピーする
編集する
python weather_homu.py
→ 自動投稿が開始される！（手動実行もOK）

📝 注意
⚠ 本プロジェクトは、暁美ほむら の非公式 bot です。
⚠ Twitter API の無料プランでは自動投稿の制限があるため、必要に応じて有料プランを検討してください。
⚠ OpenAI API（ChatGPT）を使用するため、API利用に料金が発生する可能性があります。

© 2025 どやせ / HomuLabo
