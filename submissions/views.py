from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CodeSubmission
from .serializers import CodeSubmissionSerializer
from core.celery import execute_code


class SubmitCodeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CodeSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            code = serializer.validated_data.get('code')
            result = execute_code.delay(code)
            return Response({'task_id': result.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewSubmissionsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        submissions = CodeSubmission.objects.filter(user=request.user)
        serializer = CodeSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)
