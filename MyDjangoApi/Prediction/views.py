from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Prediction.models import DataArticle
from Prediction.serializers import HistorySerializer
from rest_framework.decorators import api_view
from django.db.models import Max
import sys

import pickle
import numpy as np
from sklearn import model_selection

@api_view(['GET', 'POST', 'DELETE'])
def data_list(request):
    if request.method == 'GET':
        datas = DataArticle.objects.all().order_by('-id')        
        data_serializer = HistorySerializer(datas, many=True)
        return JsonResponse(data_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        myurl = post_data['url']
        mytimedelta = post_data['timedelta']
        post_data.pop('url', None)
        post_data.pop('timedelta', None)

        i = 0
        obj = np.array([])
        for element in post_data:
            obj = np.insert(obj,i,post_data[element])
            i += 1

        loaded_model = pickle.load(open('Prediction/finalized_modelLogistic2.sav', 'rb'))
        result = loaded_model.predict(obj.reshape(1, -1))
        print(result[0])
        post_data.update({"popularity": result[0]})
        post_data.update({"url": myurl})
        post_data.update({"timedelta": mytimedelta})

        post_serializer = HistorySerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = DataArticle.objects.all().delete()
        return JsonResponse({'message': '{} All data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def data_detail(request, pk):
    try: 
        dataSingle = DataArticle.objects.get(pk=pk) 
    except DataArticle.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        post_serializer = HistorySerializer(dataSingle) 
        return JsonResponse(post_serializer.data) 
 
    elif request.method == 'PUT': 
        post_data = JSONParser().parse(request) 
        data_serializer = HistorySerializer(dataSingle, data=post_data) 
        if data_serializer.is_valid(): 
            data_serializer.save() 
            return JsonResponse(data_serializer.data) 
        return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        dataSingle.delete() 
        return JsonResponse({'message': 'Data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

