from django.http import HttpResponse
from django.shortcuts import render


def main (request):
    
    return render (request , 'main.html')

def about(request):
    
     return render (request , 'about.html')

def scoring(request):
    
     return render (request , 'scoring.html')

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

def resultblue1 (request):
         
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render (request , 'blue1/resultblue1.html', {'score': score, 'truecounter':truecounter})


def task12 (request):
    
    return render (request , 'blue2/task12.html')


def task22 (request):
     context = {}
     theScore=request.POST.get('score', None)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
     score= int(theScore) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
     

     return render (request , 'blue2/task22.html', {'score': score, 'truecounter':truecounter})

def task32 (request):
     theScore=request.POST.get('score', 0)
     theScorAdd = request.POST.get('scoreAdd', 0)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
    
     score= int(theScore) + int(theScorAdd) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
    
     return render (request , 'blue2/task32.html', {'score': score, 'truecounter':truecounter})

def task42 (request):
     theScore=request.POST.get('score', 0)
     theScorAdd = request.POST.get('scoreAdd', 0)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
    
     score= int(theScore) + int(theScorAdd) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
    
     return render (request , 'blue2/task42.html', {'score': score, 'truecounter':truecounter})

def task52 (request):
     theScore=request.POST.get('score', 0)
     theScorAdd = request.POST.get('scoreAdd', 0)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
    
     score= int(theScore) + int(theScorAdd) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
    
     return render (request , 'blue2/task52.html', {'score': score, 'truecounter':truecounter})

def task62 (request):
     theScore=request.POST.get('score', 0)
     theScorAdd = request.POST.get('scoreAdd', 0)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
    
     score= int(theScore) + int(theScorAdd) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
    
     return render (request , 'blue2/task62.html', {'score': score, 'truecounter':truecounter})

def task72 (request):
     theScore=request.POST.get('score', 0)
     theScorAdd = request.POST.get('scoreAdd', 0)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
    
     score= int(theScore) + int(theScorAdd) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
    
     return render (request , 'blue2/task72.html', {'score': score, 'truecounter':truecounter})

def task82 (request):
     theScore=request.POST.get('score', 0)
     theScorAdd = request.POST.get('scoreAdd', 0)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
    
     score= int(theScore) + int(theScorAdd) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
    
     return render (request , 'blue2/task82.html', {'score': score, 'truecounter':truecounter})

def resultblue2 (request):
         
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render (request , 'blue2/resultblue2.html', {'score': score, 'truecounter':truecounter})


def introRed (request):
    return render(request, 'introRed.html')

def taskRed11 (request):
    return render(request, 'red1/taskRed11.html')

def taskRed12 (request):
     theScore=request.POST.get('score', None)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
     score= int(theScore) - int(deduction)
     truecounter = int(counter)+ int(counteradd)

     return render(request, 'red1/taskRed12.html', {'score': score, 'truecounter':truecounter})

def taskRed13 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    return render (request , 'red1/taskRed13.html',  {'score': score, 'truecounter':truecounter})
    

def taskRed14 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/taskRed14.html', {'score': score, 'truecounter':truecounter})

def taskRed15 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/taskRed15.html',{'score': score, 'truecounter':truecounter})

def resultRed1 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/resultRed1.html',{'score': score, 'truecounter':truecounter})

def taskRed21 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/taskRed21.html',{'score': score, 'truecounter':truecounter})

def taskRed22 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/taskRed22.html',{'score': score, 'truecounter':truecounter})

def taskRed23 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/taskRed23.html',{'score': score, 'truecounter':truecounter})

def taskRed24 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/taskRed24.html',{'score': score, 'truecounter':truecounter})

def taskRed25 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/taskRed25.html',{'score': score, 'truecounter':truecounter})

def resultRed2 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    score = int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render(request, 'red1/resultRed2.html',{'score': score, 'truecounter':truecounter})