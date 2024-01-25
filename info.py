

question_list = [
    {
    "question": "Вы считаете себя счастливым и хорошим человеком?",
    "answer_add_points": "НЕТ",
    "points": 5
},

    {
    "question": "Вы считаете себя неудачником?",
    "answer_add_points": "ДА",
    "points": 5
},
    {
    "question": "Вы испытывали депрессию?",
    "answer_add_points": "ДА",
    "points": 10

},
    {
    "question": "Вы чувствуете себя одиноким?",
    "answer_add_points": "ДА",
    "points": 2

},

    {
    "question": "Есть ли у вас какие-нибудь необычные навязчивые идеи?",
    "answer_add_points": "ДА",
    "points": 3

},

    {
    "question": "Были ли у вас когда-нибудь проблемы с полицией?",
    "answer_add_points": "ДА",
    "points": 10

},

    {
    "question": "Вы когда-нибудь что-нибудь воровали?",
    "answer_add_points": "ДА",
    "points": 10

},

    {
    "question": "Вы часто лжете?",
    "answer_add_points": "ДА",
    "points": 5

},

    {
    "question": "Вы когда-нибудь принимали наркотики?",
    "answer_add_points": "ДА",
    "points": 15

},

    {
    "question": "Вы когда-то угрожали другим, запугивали их?",
    "answer_add_points": "ДА",
    "points": 15

},

    {
    "question": "Относитесь ли вы с подозрением или недоверием к мигрантам?",
    "answer_add_points": "ДА",
    "points": 10

},

    {
    "question": "Вас полностью устраивает ваша жизнь?",
    "answer_add_points": "НЕТ",
    "points": 10

}
]

recomendation_list = ["У тебя все хорошо, продолжай в том же духе.",
                      "Думай меньше о плохом и у тебя все будет хорошо.",
                      "Возможно твое прошлое было не лучшим, но думаю у тебя все будет хорошо.",
                      "Возможно ты связался с плохой компанией,пересмотри свой круг общения, возможно найдешь кого то , с кем не стоит общаться.",
                      "Обратись к сихологу, скорее всего тебе стоит персмотреть свои взгляды на жизнь, попробуй поменять образ жизни."]


def get_recomendation_list(points):
    if 0 <= points <=14:
        return recomendation_list[0]
    elif 15 <= points <= 29:
        return recomendation_list[1]
    elif 30 <= points <= 49:
        return recomendation_list[2]
    elif 50 <= points <= 69:
        return recomendation_list[3]
    elif 70 <= points <= 100:
        return recomendation_list[4]

