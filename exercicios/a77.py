# Exercicio de perguntas e respostas

from typing import List, Dict, Union

type question = Dict[str, Union[str, List[str]]]

questions: List[question] = [
    {
        "question": "Qual a capital do Brasil?",
        "options": ["São Paulo", "Rio de Janeiro", "Brasília", "Belo Horizonte"],
        "answer": "Brasília",
    },
    {
        "question": "Qual a capital do Japão?",
        "options": ["Tóquio", "Quioto", "Osaka", "Nagoya"],
        "answer": "Tóquio"
    },
    {
        "question": "Qual a capital da Argentina?",
        "options": ["Buenos Aires", "Córdoba", "Rosário", "Mendoza"],
        "answer": "Buenos Aires"
    },
    {
        "question": "Qual a capital da França?",
        "options": ["Paris", "Lyon", "Marselha", "Toulouse"],
        "answer": "Paris"
    },
    {
        "question": "Qual a capital da Alemanha?",
        "options": ["Berlim", "Hamburgo", "Munique", "Colônia"],
        "answer": "Berlim"
    },
    {
        "question": "Qual a capital da Itália?",
        "options": ["Roma", "Milão", "Nápoles", "Turim"],
        "answer": "Roma"
    },
    {
        "question": "Qual a capital da Espanha?",
        "options": ["Madri", "Barcelona", "Valência", "Sevilha"],
        "answer": "Madri"
    },
    {
        "question": "Qual a capital da Inglaterra?",
        "options": ["Londres", "Manchester", "Liverpool", "Birmingham"],
        "answer": "Londres"
    },
    {
        "question": "Qual a capital da Rússia?",
        "options": ["Moscou", "São Petersburgo", "Novosibirsk", "Ecaterimburgo"],
        "answer": "Moscou"
    },
    {
        "question": "Qual a capital da China?",
        "options": ["Pequim", "Xangai", "Cantão", "Tianjin"],
        "answer": "Pequim"
    }
]


def shufleQuestions(questions: List[question]) -> List[question]:
    from random import shuffle
    shuffle(questions)
    return questions


def shufleOptions(options: List[str]) -> List[str]:
    from random import shuffle
    shuffle(options)
    return options


newQuestions = shufleQuestions(questions)

points = 0

for question in newQuestions:
    print(question["question"])
    options = shufleOptions(question["options"])
    enum_options = enumerate(options)
    for index, option in enum_options:
        print(f"{index + 1} - {option}")
    # answer is a number of the index of the option
    answer = input("Resposta: ")
    if options[1 - 1] == question["answer"]:
        print("Resposta correta!")
        points += 1
    else:
        print("Resposta errada!")
        print(f"A resposta correta é {question['answer']}")

print(f"Você acertou {points} de {len(newQuestions)} perguntas")