const startBtn = document.getElementById('start-btn');
const resultDiv = document.getElementById('result');
const apiUrl = 'http://localhost:5000/api/process_input'; // 서버 주소를 설정합니다.

startBtn.addEventListener('click', async () => {
  const recognition = new webkitSpeechRecognition();
  recognition.lang = 'ko-KR'; // 한국어 설정, 필요에 따라 변경 가능
  
  recognition.start();

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    resultDiv.innerHTML = `당신이 말한 내용: ${transcript}`;
    getResponse(transcript);
  };

  recognition.onerror = function(event) {
    console.error('음성 인식 중 오류가 발생했습니다.', event.error);
  };
});

async function getResponse(input) {
  try {
    const response = await fetch(`${apiUrl}?input=${encodeURIComponent(input)}`);
    const data = await response.json();
    
    // "당신이 말한 내용"과 함께 응답을 결과 창에 표시
    resultDiv.innerHTML += `<br>컴퓨터의 대답: ${data.response}`;
  } catch (error) {
    console.error('서버 요청 중 오류가 발생했습니다.', error);
    resultDiv.innerHTML += `<br>푸힝힝.`;
  }
}