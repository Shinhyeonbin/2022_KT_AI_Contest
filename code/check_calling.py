import difflib

def check_genie(text):
    input_text = text
    answer_text = "지니야"
    close_text1 = "종료"
    close_text2 = "꺼줘"

    input_bytes = bytes(input_text, 'utf-8')
    answer_bytes = bytes(answer_text, 'utf-8')
    input_bytes_list = list(input_bytes)
    answer_bytes_list = list(answer_bytes)

    sm = difflib.SequenceMatcher(None, input_bytes_list, answer_bytes_list)
    if sm.ratio() > 0.75:
        print(sm.ratio())
        return "지니야"

    elif sm.ratio() > 0 and sm.ratio() <= 0.75:
        close_bytes1 = bytes(close_text1, 'utf-8')
        close_bytes2 = bytes(close_text2, 'utf-8')
        close_bytes1_list = list(close_bytes1)
        close_bytes2_list = list(close_bytes2)

        sm1 = difflib.SequenceMatcher(None, input_bytes_list, close_bytes1_list)
        sm2 = difflib.SequenceMatcher(None, input_bytes_list, close_bytes2_list)
        if sm1.ratio() > 0.65 or sm2.ratio() > 0.75:
            print(sm1.ratio(), ", ", sm2.ratio())
            return "종료"

    return text
