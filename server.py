from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/api/process_input', methods=['GET'])
def process_input():
    input_text = request.args.get('input')
    response = generate_response(input_text)
    return jsonify({'input': input_text, 'response': response})
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/api/process_input', methods=['GET'])
def process_input():
    input_text = request.args.get('input')
    response = generate_response(input_text)
    return jsonify({'input': input_text, 'response': response})

def generate_response(input_text):
    if "일 번" in input_text:
        return "자가진단은 간단한 문진 형식으로 진행되며, 각 질문에 답변하면 자동으로 다음 질문으로 넘어갑니다."
    elif "이 번" in input_text:
        return "자가진단 결과는 초기 평가를 위한 것이며, 정확한 진단은 반드시 의료 전문가와 상담이 필요합니다."
    elif "삼 번" in input_text:
        return "일반적으로 5-10분 정도 소요됩니다."
    elif "사 번" in input_text:
        return "네, 모든 개인정보는 암호화되어 안전하게 저장되며, 사용자의 동의 없이 외부로 유출되지 않습니다."
    elif "오 번" in input_text:
        return "자가진단 결과는 사용자의 건강 상태 평가와 맞춤형 건강 정보를 제공하는 데 사용됩니다."
    elif "육 번" in input_text:
        return "오류가 발생하면 페이지를 새로고침하거나 고객 지원팀에 연락해 주세요."
    elif "칠 번" in input_text:
        return "네, 자가진단 서비스는 무료로 제공됩니다."
    elif "팔 번" in input_text:
        return "네, 언제든지 다시 자가진단을 할 수 있습니다."
    elif "1번" in input_text:
        return "자가진단은 간단한 문진 형식으로 진행되며, 각 질문에 답변하면 자동으로 다음 질문으로 넘어갑니다."
    elif "2번" in input_text:
        return "자가진단 결과는 초기 평가를 위한 것이며, 정확한 진단은 반드시 의료 전문가와 상담이 필요합니다."
    elif "3번" in input_text:
        return "일반적으로 5-10분 정도 소요됩니다."
    elif "4번" in input_text:
        return "네, 모든 개인정보는 암호화되어 안전하게 저장되며, 사용자의 동의 없이 외부로 유출되지 않습니다."
    elif "5번" in input_text:
        return "자가진단 결과는 사용자의 건강 상태 평가와 맞춤형 건강 정보를 제공하는 데 사용됩니다."
    elif "6번" in input_text:
        return "오류가 발생하면 페이지를 새로고침하거나 고객 지원팀에 연락해 주세요."
    elif "7번" in input_text:
        return "네, 자가진단 서비스는 무료로 제공됩니다."
    elif "8번" in input_text:
        return "네, 언제든지 다시 자가진단을 할 수 있습니다."
    else:
        return "입력한 내용에 대한 답변을 찾을 수 없습니다."

if __name__ == '__main__':
    app.run(debug=True)
