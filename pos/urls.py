

from django.urls import path

from rest_framework.routers import DefaultRouter

from pos import views

router=DefaultRouter()

router.register("category",views.CategoryViewSet,basename="category")

router.register("products",views.ProductViewSetView,basename="products")



urlpatterns=[
    
     path("category/<int:pk>/products/",views.ProductCreateView.as_view()),
     
     path('orders/',views.OrderCreateView.as_view()),
     
     path('orders/<int:pk>/items/',views.OrderItemCreateView.as_view()),
     
     path('orders/<int:pk>/',views.OrderRetrieveView.as_view()),


    
]+router.urls