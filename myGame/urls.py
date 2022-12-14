"""myGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from theGame.views import main , team, tutorial,end, taskChoiceBlue,taskChoiceRed,blue1, task11, task21,task31,task41,task51,task61, task71,resultblue1, about , scoring
from theGame.views import task12, task22, task32,task42,task52,task62,task72,task82,resultblue2
from theGame.views import introRed,taskRed11,taskRed12,taskRed13,taskRed14,taskRed15,resultRed1,navigator
from theGame.views import taskRed21,taskRed22,taskRed23,taskRed24,taskRed25,resultRed2
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('tutorial/',tutorial),
    path('scoring/', scoring, name="scoring"),
    path('', main, name="main"),
    path('team/',team, name="team"),
    path('taskChoiceBlue/', taskChoiceBlue, name="taskChoiceBlue"),
    path('taskChoiceRed/', taskChoiceRed, name="taskChoiceRed"),
    path('blue1/', blue1, name="blue1"),
    path('task11/', task11 , name="task11"),
    path('task21/', task21, name="task21"),
    path('task31/', task31, name="task31"),
    path('task41/', task41, name="task41"),
    path('task51/', task51, name="task51"),
    path('task61/', task61, name="task61"),
    path('task71/', task71, name="task71"),
    path('resultblue1/', resultblue1, name="resultblue1"),
    path('task12/', task12, name="task12"),
    path('task22/', task22, name="task22"),
    path('task32/', task32, name="task32"),
    path('task42/', task42, name="task42"),
    path('task52/', task52, name="task52"),
    path('task62/', task62, name="task62"),
    path('task72/', task72, name="task72"),
    path('task82/', task82, name="task82"),
    path('resultblue2/', resultblue2, name="resultblue2"),
    path('introRed/', introRed, name="introRed"),
    path('taskRed11/', taskRed11, name="taskRed11"),
    path('taskRed12/', taskRed12, name="taskRed12"),
    path('taskRed13/', taskRed13, name="taskRed13"),
    path('taskRed14/', taskRed14, name="taskRed14"),
    path('taskRed15/', taskRed15, name="taskRed15"),
    path('resultRed1/', resultRed1, name="resultRed1"),
    path('taskRed21/', taskRed21, name="taskRed21"),
    path('taskRed22/', taskRed22, name="taskRed22"),
    path('taskRed23/', taskRed23, name="taskRed23"),
    path('taskRed24/', taskRed24, name="taskRed24"),
    path('taskRed25/', taskRed25, name="taskRed25"),
    path('resultRed2/', resultRed2, name="resultRed2"),

    path('end/', end, name="end"),
    path('navigator/', navigator, name="navigator"),
]
    
    