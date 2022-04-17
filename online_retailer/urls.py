
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from online_retailer import views
from online_retailer.views import productList,productUpdateView,productDeleteView

urlpatterns = [
    # path('', productList.as_view(),name="ho"),
     path('<pk>/update', productUpdateView.as_view(),name="Product_update"),
    path('<pk>/delete/', productDeleteView.as_view(),name="Product_delete"),
    # api product retrive url
    path('',views.productApiView.as_view(), name="product" ),
    path('<int:pk>',views.productApiView.as_view()),
    
    # order url
    path('orderReterive/',views.orderApiView.as_view(), name="order" ),
    path('orderReterive/<int:pk>',views.orderApiView.as_view()),
    #customr url
    path('customerReterive/',views.customerApiView.as_view(), name="customer" ),
    path('customerReterive/<int:pk>',views.customerApiView.as_view()),
  
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
