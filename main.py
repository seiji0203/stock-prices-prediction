from flask_ngrok import run_with_ngrok
from flask import Flask, request, render_template
from urllib.error import URLError, HTTPError
import os
import predict_stockprice

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('get.html')  # 株価入力ページを表示
    elif request.method == 'POST':
        data = request.form["data"].split('\r\n')  # 入力された株価をリストに変換
        data = [float(val) for val in data if val != '']  # 空白のlistを削除

        y_pred, sub_ma = predict.main(data)  # 株価予測実行
        from datetime import datetime
        datetime = datetime.now().strftime('%Y%m%d%H%M%S')  # 現在日時を取得

        # 株価予測ページを表示
        return render_template('post.html', y_pred=y_pred, sub_ma=sub_ma, datetime=datetime)


if __name__ == "__main__":
    app.run()  # Webサーバーの立ち上げ