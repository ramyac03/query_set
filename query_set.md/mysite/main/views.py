from django.shortcuts import render

# Create your views here and template for that 
from django.http import HttpResponse,HttpResponseRedirect
from .models import Define,Info
from .forms import CreateNewList

def index(response,id):
         x =Define.objects.get(id=id)
#          `info =x.info_set.get(id =id)
#          return render(response,"main/base.html",{}) --->using base.html
         return render(response,"main/list.html",{"x":x}) #--->list.html


def v1(response):
          
         return HttpResponse("<h1>hello<h1>")

def home(response):
         return render(response,"main/home.html",{})

#create function
def create(response):
          if response.method =="POST":
                    form =CreateNewList(response.POST)
                    if form.is_valid():#valid the function
                              n=form.cleaned_data["name"]# adding the name in models
                              t=Define(name =n)
                              t.save()
                    return HttpResponseRedirect ("/%i" %t.id) # /-->gives the id to the url
          else:
            form =CreateNewList()

          return render(response,"main/create.html",{"form":form}) #using the variables forms

#customs forms
def index(response,id):
         x =Define.objects.get(id=id)
         if response.method =="POST": #mention the method
          print(response.POST)
          if response.POST.get("save"): #give name of  button
            for info in x.info_set.all():#iterate the list
              if response.post.get("c"+str(info.id)) =="clicked":
                info.email =True#update the element when we click
              else:
                info.email =False

              info.save() #save the checklist

          elif response.POST.get("newinfo"):
            print("yes")
            txt =response.POST.get("new")#get the new info
            if len(txt)>2:
                x.info_set.create(text =txt,email=True)
            else:
                print("Invalid")


         return render(response,"main/list.html",{"x":x}) #--->list.html


