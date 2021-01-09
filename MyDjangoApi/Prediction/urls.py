from django.conf.urls import url 
from Prediction import views 
 
urlpatterns = [ 
    url(r'^api/alldata$', views.data_list),
    url(r'^api/data/(?P<pk>[0-9]+)$', views.data_detail)
]