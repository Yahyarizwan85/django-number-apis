from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SumView(APIView):
    def post(self, request):
        numbers = request.data.get('numbers', [])
        result = sum(numbers)
        return Response({'result': result}, status=status.HTTP_200_OK)



class AverageView(APIView):
    def post(self, request):
        numbers = request.data.get('numbers', [])
        if len(numbers) == 0:
            return Response({'error': 'Empty list'}, status=status.HTTP_400_BAD_REQUEST)
        result = sum(numbers) / len(numbers)
        return Response({'result': result}, status=status.HTTP_200_OK)


  

class ProductView(APIView):
    def post(self, request):
        numbers = request.data.get('numbers', [])
        result = 1
        for num in numbers:
            result *= num
        return Response({'result': result}, status=status.HTTP_200_OK)
