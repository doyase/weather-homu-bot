# 暁美ほむら 天気予報 bot（非公式）

このプロジェクトは、Pythonを使用して **X（旧Twitter）に自動で天気予報を投稿** するbotです。  
OpenWeather API から天気データを取得し、Tweepyを使って自動投稿を行います。

## 🔧 使用技術
- 言語: **Python**
- API: **OpenWeather API、Twitter API v2**
- ライブラリ: **Tweepy、Schedule、Requests、dotenv**

## 📌 機能
- 毎日 **朝7時 / 昼12時 / 夜18時** に **天気予報を自動投稿**
- 気温・天候に応じて異なるメッセージを表示
- `.env` ファイルでAPIキーを管理

## 🚀 使い方
1. `.env` ファイルを作成し、APIキーを設定
2. `requirements.txt` を使って必要なライブラリをインストール
3. `weather_homu.py` を実行すれば、自動投稿がスタート！

## 📝 注意
- 本プロジェクトは、**暁美ほむら** の非公式 bot です。
- Twitter API の制限により、**無料プランでは自動投稿が制限される場合があります**。

---
**© 2025 誠 / HomuLabo**
