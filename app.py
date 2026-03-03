
from flask import Flask, request, render_template

app = Flask(__name__)

# 建立題庫
zh_ko_dict = {
    "你好": "안녕하세요",
    "안녕하세요" : "你好",
    "謝謝": "감사합니다",
    "對不起": "죄송합니다",
    "早安": "좋은 아침",
    "晚安": "안녕히 주무세요",
    "老師": "선생님",
    "學生": "학생",
    "朋友": "친구",
    "家人": "가족",
    "愛": "사랑"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask.html', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        answer = zh_ko_dict.get(question, "抱歉，我目前沒有這個詞的韓文對應。")
        return render_template('ask.html', question=question, answer=answer)

    return render_template('ask.html', question="", answer="")


if __name__ == '__main__':
    app.run(debug=False)  # 不觸發 reloader
