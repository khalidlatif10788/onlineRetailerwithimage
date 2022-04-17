
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import product,order,customer
from .Serializers import productSerializer,orderSerializer,customerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@method_decorator(login_required, name="dispatch")
class productList(ListView):

    model = product
    #paginate_by=3
    
@method_decorator(login_required, name="dispatch")
class productUpdateView(UpdateView):
    model = product
    fields = [
        "pname",
        "pdescription",
        "psalep",
        "photo"
    ]

    success_url ="/"
    
@method_decorator(login_required, name="dispatch")
class productDeleteView(DeleteView):
    model = product
    success_url ="/"


# Api code

class productApiView(APIView):
    def get(self, request,pk=None,format= None):
        if request.method == 'GET':
         id = pk
         if id is not None:
          stu = product.objects.get(id=id)
          serilizer = productSerializer(stu)
          return Response(serilizer.data)
         else:
          stu = product.objects.all()
          serilizer = productSerializer(stu, many=True)
          return Response(serilizer.data)

    def post(self, request, format=None):
        serilizer= productSerializer(data=request.data)
        #data= request.data
        #image_p =data['image']
        
        if serilizer.is_valid():
           
             serilizer.save()

             #format,imgstr=image_p.split(';base64,')
             #ext=format.split('/')[-1]
             return Response({"msg":"data has added sucessfully"})
            
        else:
         return Response(serilizer.errors)


    
    def put(self, request,pk= None, format=None):
        id = pk
        stu= product.objects.get(id=id)
        serilizer= productSerializer(stu, data=request.data, partial=True)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has updated sucessfully"})
        else:
         return Response(serilizer.errors)
 
 
    def delete(self, request,pk= None, format=None):
        id = pk
        stu= product.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"data deleted"}) 
    
# order class

class orderApiView(APIView):
    def get(self, request,pk=None,format= None):
        if request.method == 'GET':
         id = pk
         if id is not None:
          stu = order.objects.get(id=id)
          serilizer = orderSerializer(stu)
          return Response(serilizer.data)
         else:
          stu = order.objects.all()
          serilizer = orderSerializer(stu, many=True)
          return Response(serilizer.data)

    def post(self, request, format=None):
        serilizer= orderSerializer(data=request.data)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has added sucessfully"})
        else:
         return Response(serilizer.errors)
    
    def put(self, request,pk= None, format=None):
        id = pk
        stu= order.objects.get(id=id)
        serilizer= orderSerializer(stu, data=request.data, partial=True)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has updated sucessfully"})
        else:
         return Response(serilizer.errors)
 
 
    def delete(self, request,pk= None, format=None):
        id = pk
        stu= order.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"data deleted"}) 
    
    #Customer class
    
class customerApiView(APIView):
    def get(self, request,pk=None,format= None):
        if request.method == 'GET':
         id = pk
         if id is not None:
          stu = customer.objects.get(id=id)
          serilizer = customerSerializer(stu)
          return Response(serilizer.data)
         else:
          stu = customer.objects.all()
          serilizer = customerSerializer(stu, many=True)
          return Response(serilizer.data)

    def post(self, request, format=None):
        serilizer= customerSerializer(data=request.data)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has added sucessfully"})
        else:
         return Response(serilizer.errors)
    
    def put(self, request,pk= None, format=None):
        id = pk
        stu= customer.objects.get(id=id)
        serilizer= customerSerializer(stu, data=request.data, partial=True)
        if serilizer.is_valid():
         serilizer.save()
         return Response({"msg":"data has updated sucessfully"})
        else:
         return Response(serilizer.errors)
 
 
    def delete(self, request,pk= None, format=None):
        id = pk
        stu= customer.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"data deleted"}) 