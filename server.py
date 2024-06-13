from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/process_input', methods=['GET'])
def process_input():
    input_text = request.args.get('input')
    response = generate_response(input_text)
    return jsonify({'input': input_text, 'response': response})

def generate_response(input_text):
    if "다이어트" in input_text:
        return "다이어트가 고민이시군요!"
    elif "치매" in input_text:
        return "치매는 심각한 질병입니다."
    else:
        return "입력한 내용에 대한 답변을 찾을 수 없습니다."

if __name__ == '__main__':
    app.run(debug=True)
