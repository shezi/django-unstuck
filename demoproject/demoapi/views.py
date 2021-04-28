from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Demonstration
from .serializers import DemonstrationSerializer


class DemoList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Demonstration.objects.all()
        serializer = DemonstrationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DemonstrationSerializer(data=request.data)
        print("about to validate...")
        if serializer.is_valid():
            print("  was valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


demo_list = DemoList.as_view()
