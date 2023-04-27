# 문제 출력 정제 함수
def wrap_text(text):
    # 줄바꿈 처리된 문자열을 저장할 리스트
    lines = []
    # 현재 줄에 쌓인 단어들을 저장할 문자열
    current_line = ""
    # 입력된 문자열을 공백을 기준으로 단어를 분리하여 처리
    for word in text.split():
        if word.endswith(".") or word.endswith("?"):
            # 단어가 마침표(.)나 물음표(?)로 끝나면,
            # 현재 줄에 단어를 추가한 후, 현재 줄을 처리하고 다음 줄로 이동
            current_line += " " + word
            lines.append(current_line.strip())
            # 출력 결과에 공백이 없도록 다음 줄에 대해 개행 문자를 추가하지 않음
            current_line = ""
        else:
            # 현재 줄에 단어를 추가할 수 있는 경우 추가
            if len(current_line) + len(word) + 1 <= 50:
                current_line += " " + word
            # 현재 줄에 더 이상 단어를 추가할 수 없는 경우 다음 줄로 이동
            else:
                lines.append(current_line.strip())
                current_line = word
    # 남은 단어를 처리하여 출력 결과 생성
    if current_line:
        lines.append(current_line.strip())
    return "\n".join(lines)