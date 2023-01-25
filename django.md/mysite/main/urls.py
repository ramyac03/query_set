
from django.urls import path

from  . import views # import the current file using (.)
urlpatterns =[path("<int:id>",views.index,name ="index"),
 path("",views.home,name ="")
]# views.index call the views function