from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import QuestionModel, QuizModel
# Create your views here.

def QuizView(request):
    quiz_objs = QuizModel.objects.all()
    return render(request, 'quizzes/quizzes.html', {"quizzes": quiz_objs})

def QuestionsView(request, id):
    if request.user.is_authenticated:
        quiz = QuizModel.objects.get(id=id)
        question_objs  = quiz.questions.all()
        return render(request, 'questions/question.html', {"questions": question_objs, "quiz": id, "duration": quiz.duration, "title": quiz.title})
    else:
        return redirect('login')
    

def quiz_data_view(request, id):
    quiz = QuizModel.objects.get(pk=id)
    question_objs  = quiz.questions.all()
    questions_list = []
    for q in question_objs:
        questions_list.append(
            {
                "question": q.question,
                "op1": q.op1,
                "op2": q.op2,
                "op3": q.op3,
                "op4": q.op4,
                "ans": q.ans
            }
        )
   
    return JsonResponse({
        'data': questions_list,
        'time': quiz.duration,
    })

def save_quiz_view(request, id):
    if request.is_ajax():
        data = request.POST
        quiz = QuizModel.objects.get(id=id)
        question_objs = quiz.questions.all()
        time_taken = data['time_taken']
        score=0
        wrong=0
        correct=0
        total=0
        questions = []
        for q in question_objs:
            total+=1
           
            if q.ans == data.get(q.question):
                score+=10
                correct+=1
                questions.append({'q': q.question, 'correct': True, 'correct_ans': q.ans})
            elif data.get(q.question) == '':
                wrong+=1
                questions.append({'q': q.question, 'correct': False, 'answered': 'Not answered', 'correct_ans': q.ans})
            else:
                wrong+=1
                questions.append({'q': q.question, 'correct': False, 'answered': data.get(q.question), 'correct_ans': q.ans})
        percent = score/(total*10) *100
        
        context = {
                'user': str(request.user),
                'score':score,
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total,
                'time_taken': time_taken,
                'questions': questions
            }
   
    
    return JsonResponse(context)
    

def ResultView(request, id):
    
    if request.method == 'POST':
        quiz = QuizModel.objects.get(id=id)
        question_objs = quiz.questions.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in question_objs:
            total+=1
            
            if q.ans == request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        
        return render(request,'quizzes/result.html', context)

    else:
        quiz = QuizModel.objects.get(id=id)
        question_objs = quiz.questions.all()
        context = {
            'questions':question_objs
        }
        return render(request,'questions/question.html', context)
