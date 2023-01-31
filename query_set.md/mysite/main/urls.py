
from django.urls import path

from  . import views # import the current file using (.)
urlpatterns =[path("<int:id>",views.index,name ="index"),#getting the id for the input
 path("",views.home,name =""),
 path("create/",views.create,name ="create")
]# views.index call the views function