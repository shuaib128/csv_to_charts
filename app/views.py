from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response


# Create your views here.
class Home(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    def post(self, request, format=None):
        exel_file = request.data["file"]
        file_extention = str(exel_file).split(".")[1]
        title = request.data['Title']
        BGColor = request.data['BGcolor']
        print(exel_file)

        if file_extention == 'xlsx':
            df = pd.read_excel(exel_file)
            labels = df.columns.to_list()
            data = []

            for i in labels:    
                data.append(int(df[i][0]))

            return JsonResponse({
                "labels": labels, "datas": data, "title": title,
                "backgroundcolor": BGColor
            }, safe=False)


        elif file_extention == 'csv':
            df = pd.read_csv(exel_file)
            labels = df.columns.to_list()
            data = []

            for i in labels:    
                data.append(int(df[i][0]))
            
            return JsonResponse({
                "labels": labels, "datas": data, "title": title,
                "backgroundcolor": BGColor
            }, safe=False)
        
        return Response("user")



# Multiple datas
class multiple_chat_home(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    def post(self, request, format=None):
        exel_file = request.data["file"]
        file_extention = str(exel_file).split(".")[1]
        BGColor = request.data['BGcolor']

        if file_extention == 'xlsx':
            df = pd.read_excel(exel_file)
            df_main = df.iloc[: , 1:]
            labels = df_main.columns.to_list()
            indivusial_labels = df.iloc[: , 0].to_list()
            data = []

            for i in labels:
                data.append(df_main[i].tolist())
            
            return JsonResponse({
                "labels": labels,
                "datas": data,
                "backgroundcolor": BGColor,
                "indivusial_labels": indivusial_labels
            }, safe=False)

        elif file_extention == 'csv':
            df = pd.read_csv(exel_file)
            df_main = df.iloc[: , 1:]
            labels = df_main.columns.to_list()
            indivusial_labels = df.iloc[: , 0].to_list()
            data = []

            for i in labels:
                data.append(df_main[i].tolist())
            
            return JsonResponse({
                "labels": labels,
                "datas": data,
                "backgroundcolor": BGColor,
                "indivusial_labels": indivusial_labels
            }, safe=False)
    
        return Response("user")