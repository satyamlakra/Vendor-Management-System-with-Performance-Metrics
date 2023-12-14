from django.shortcuts import render,get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from  intro.serializers import vpm,poapi,apoapi,pvpm
from  intro.models import  VendorProfileManagement,po
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        
        serializer.is_valid(raise_exception=True)
        print(serializer.errors)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    

class vpmview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = vpm
    def post(self,request,*args, **kwargs):
        try:
            serializer =self.serializer_class(data=request.data)
            
            if  serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data ,status=status.HTTP_200_OK)
              
        except:
            return Response({'error':True},status=status.HTTP_404_NOT_FOUND)
    def get(self,request,vendor_id=None,*args, **kwargs):
        serializer=self.serializer_class
        try: 
            if vendor_id is None:
                
                return Response(serializer(VendorProfileManagement.objects.all(),many=True).data ,status=status.HTTP_200_OK)
            
            else:
                return Response(serializer(VendorProfileManagement.objects.filter(id=vendor_id),many=True).data ,status=status.HTTP_200_OK)
        except:
            return Response({'error':True},status=status.HTTP_404_NOT_FOUND)
    def put(self,request,vendor_id=None,*args, **kwargs):
        try:
            instance = get_object_or_404(VendorProfileManagement,pk=vendor_id)
            
            serializer=self.serializer_class(instance,request.data,partial=True)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(vpm(VendorProfileManagement.objects.filter(id=vendor_id),many=True).data ,status=status.HTTP_200_OK)
            return Response({'done':False} ,status=status.HTTP_200_OK)
        except:
            return Response({'error':True},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,vendor_id=None,*args, **kwargs):
        serializer=self.serializer_class
        try:
            if vendor_id is not None:
                instance = get_object_or_404(VendorProfileManagement,pk=vendor_id)
                instance.delete()
                return Response(serializer(VendorProfileManagement.objects.filter(id=vendor_id),many=True).data ,status=status.HTTP_200_OK)
            
            else:
                return Response({'error':True},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error':True},status=status.HTTP_404_NOT_FOUND)  
class poview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = poapi
    def post(self,request,*args, **kwargs):
        serializer =self.serializer_class(data=request.data)
        try:
            if  serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(serializer.data ,status=status.HTTP_200_OK)
            
        except:
              return Response({'error':True},status=status.HTTP_404_NOT_FOUND)  
    def get(self,request,po_id=None,*args, **kwargs):
        
        serializer=self.serializer_class
        
        try:
            if po_id is None:
                
                return Response(serializer(po.objects.all(),many=True).data ,status=status.HTTP_200_OK)
            
            else:
                return Response(serializer(po.objects.filter(id=po_id),many=True).data ,status=status.HTTP_200_OK)
        except:
              return Response({'error':True},status=status.HTTP_404_NOT_FOUND)     
    def put(self,request,po_id=None,*args, **kwargs):
        try:
            instance = get_object_or_404(po,pk=po_id)
        
            serializer=self.serializer_class(instance,request.data,partial=True)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(poview(po.objects.filter(id=po_id),many=True).data ,status=status.HTTP_200_OK)
            else:
                return Response({'error':True},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error':True},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,po_id=None,*args, **kwargs):
        serializer=self.serializer_class
        try:
            if po_id is not None:
                instance = get_object_or_404(po,pk=po_id)
                instance.delete()
                return Response(serializer(po.objects.filter(id=po_id),many=True).data ,status=status.HTTP_200_OK)
            
            else:
                
                return Response({'error':True},status=status.HTTP_404_NOT_FOUND)  
        except:
            return Response({'error':True},status=status.HTTP_404_NOT_FOUND)            



class apoview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = apoapi
      
     
    def post(self,request,po_id=None,*args, **kwargs):
            print(po_id)
        # try:
            instance = get_object_or_404(po,pk=po_id)
        
            serializer=self.serializer_class(instance,request.data)
           
            if serializer.is_valid(raise_exception=True):
            
                
                serializer.save()
                return Response(poapi(po.objects.filter(id=po_id),many=True).data  ,status=status.HTTP_200_OK)
           
        # except Exception as e:
            
        #     print(e,serializer.errors)
        #     return Response({'error':True},status=status.HTTP_404_NOT_FOUND)
class pvpmview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = pvpm
    
    def get(self,request,vendor_id=None,*args, **kwargs):
        serializer=self.serializer_class
       
        try: 
            if vendor_id is not None:
               
                return Response(serializer(VendorProfileManagement.objects.all(),many=True).data ,status=status.HTTP_200_OK)
            
            else:
               
                return Response(serializer(VendorProfileManagement.objects.filter(id=vendor_id),many=True).data ,status=status.HTTP_200_OK)
        except:
            return Response({'error':True},status=status.HTTP_404_NOT_FOUND)
    