from rest_framework import generics
from api.serializer import UserCustomerSerializer
from .models import Customer
from rest_framework import status
from rest_framework.response import Response
class ListUserCustomerView(generics.ListAPIView):
    serializer_class = UserCustomerSerializer
    
    def get_queryset(self):
        return Customer.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        repeat_true_customers = queryset.filter(repeat=True)
        repeat_false_customers = queryset.filter(repeat=False)

        true_serializer = self.get_serializer(repeat_true_customers, many=True)
        false_serializer = self.get_serializer(repeat_false_customers, many=True)

        return Response({
            'repeat_true_customers': true_serializer.data,
            'repeat_false_customers': false_serializer.data
        }, status=status.HTTP_200_OK)