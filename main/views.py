from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileTableSerializer
import json
from .models import FileTable
from datetime import datetime
import sys
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class FileSave(APIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        response = {}
        response['status_code'] = '500'
        response['status_message'] = 'Internal Server Error'
        try:
            file_serializer = FileTableSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                response['status_code'] = '200'
                response['status_message'] = 'Success'
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                response['status_code'] = '400'
                response['status_message'] = 'Bad Request'
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # _, _, exec_tb = sys.exc_info()
            # response['status_message'] = f'Error: {e} at {exec_tb.tb_lineno}'
            return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListFiles(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        response = {}
        response['status_code'] = '500'
        response['status_message'] = 'Internal Server Error'
        try:
            filetable_objs = FileTable.objects.all()

            all_files = []
            for i in filetable_objs:
                all_files.append({
                    'file_name': str(i.file), 
                    'file_link': settings.HOST_URL + '/' + str(i.file), 
                    'created_at': datetime.strftime(i.created_at, '%d/%m/%Y %H:%M:%S')
                })

            response['all_files'] = all_files
            response['status_code'] = '200'
            response['status_message'] = 'Success'
            return Response(data=response, status=status.HTTP_200_OK)
        except Exception as e:
            # _, _, exec_tb = sys.exc_info()
            # response['status_message'] = f'Error: {e} at {exec_tb.tb_lineno}'
            return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)