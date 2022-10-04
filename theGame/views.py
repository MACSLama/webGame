from django.http import HttpResponse
from django.shortcuts import render


def main (request):
    
    return render (request , 'main.html')


def team (request):
    
    return render (request , 'team.html')

def tutorial (request):
    
    return render (request , 'toturial.html')

def taskChoiceRed(request):

    return render(request , 'taskChoiceRed.html')

def taskChoiceBlue(request):

    return render(request , 'taskChoiceBlue.html')

def end(request):
    
    return render(request , 'thanks.html')

def blue1 (request):
    
    return render (request , 'blue1/blue1.html')

def task12 (request):
    
    return render (request , 'blue2/task12.html')

def task11 (request):
    
    return render (request , 'blue1/task1.html')


def task21 (request):
     context = {}
     theScore=request.POST.get('score', None)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
     score= int(theScore) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
     

     return render (request , 'blue1/task2.html', {'score': score, 'truecounter':truecounter})


def task31 (request):
     
    context = {}
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    return render (request , 'blue1/task3.html',  {'score': score, 'truecounter':truecounter})


def task41 (request):
     
    context = {}
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    return render (request , 'blue1/task4.html', {'score': score, 'truecounter':truecounter})

def task51 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    
    return render (request , 'blue1/task5.html', {'score': score, 'truecounter':truecounter})

def task61 (request):

    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    
    return render (request , 'blue1/task6.html', {'score': score, 'truecounter':truecounter})

def task71 (request):
    
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    
    return render (request , 'blue1/task7.html', {'score': score, 'truecounter':truecounter})

def result (request):
         
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render (request , 'result.html', {'score': score, 'truecounter':truecounter})

def about(request):

     return render (request , 'about.html')

def scoring(request):
    
     return render (request , 'scoring.html')






