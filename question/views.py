from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import  UserForm
from django.contrib.auth.models import  User
from . models import  Question,Answer 

# Create your views here.

def home(request):
    
    question_list = Question.objects.all() 
    if request.method == 'POST':
        question_text = request.POST.get('question')
        ask_by = request.POST.get('ask_by')

        print(question_text)
        print(ask_by)

        user = User.objects.get(id=ask_by) 
        print(user) 
        question = Question(
            asked_by = user,
            question_text = question_text,
        )
        question.save() 
    context = {
        'question_list':question_list,
    }
        
    return render(request, 'question/home.html',context) 

def reply(request,id):
    question = Question.objects.get(id=id)
   
    if request.method == 'POST':
        answer_text = request.POST.get('answer_text') 
        print(answer_text) 
        pic = request.FILES.get('image')
        
       
        answer = Answer(
            answer_of = question,
            answer_text = answer_text,
            media = pic, 
            
        )
        answer.save() 

        
    context = {
       'question':question,
       
    }
    return render(request,'question/reply.html',context)   


def view_reply(request,id):
    question = Question.objects.get(id=id)
    print(question)  
    all_answer = Answer.objects.filter(answer_of=question.id).order_by('-id')
    print(all_answer)
    return render(request, 'question/view_reply.html',{'ans':all_answer,'question':question})  
  

 

