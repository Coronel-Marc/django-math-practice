from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'questions/home.html')

def practice(request, category):
    question, options, correct_option = generate_question(category)
    context = {
        'question': question,
        'options': options,
        'category': category,
    }
    
    return render(request, 'questions/practice.html', context)

def generate_question(category):
    if category == 'regra_de_3':
        num1, num2, num3 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        correct_answer = (num2 * num3) // num1
        question = f"Se {num1} está para {num2}, quanto está para {num3}?"
        options = generate_options(correct_answer)
        return question, options, correct_answer
    # Adicione outras categorias aqui
    return "Questão não disponível", [], None

def generate_options(correct_answer):
    options = [correct_answer + random.randint(-5, 5) for _ in range(4)]
    options[random.randint(0, 4)] = correct_answer
    return options