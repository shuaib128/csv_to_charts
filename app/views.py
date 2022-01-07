from django.shortcuts import render
import pandas as pd

# Create your views here.
def home(request):
    try:
        exel_file = request.FILES["csvfile"]
        file_extention = str(exel_file).split(".")[1]
        title = request.POST['title']
        BGColor = request.POST['color_picker']
 
        if file_extention == 'xlsx':
            df = pd.read_excel(exel_file)
            labels = df.columns.to_list()
            data = []

            for i in labels:    
                data.append(int(df[i][0]))
            
            context = {
                "labels": labels,
                "datas": data,
                "title": title,
                "backgroundcolor": BGColor
            }

            return render(request, 'index.html', context)

        elif file_extention == 'csv':
            df = pd.read_csv(exel_file)
            labels = df.columns.to_list()
            data = []

            for i in labels:    
                data.append(int(df[i][0]))
            
            context = {
                "labels": labels,
                "datas": data,
                "title": title,
                "backgroundcolor": BGColor
            }

            return render(request, 'index.html', context)
    except Exception as e:
        print(e)

    return render(request, 'index.html')


def multiple_chat_home(request):
    try:
        exel_file = request.FILES["csvfile"]
        file_extention = str(exel_file).split(".")[1]
        BGColor = request.POST['color_picker']
 
        if file_extention == 'xlsx':
            df = pd.read_excel(exel_file)
            labels = df.columns.to_list()[1:]
            data = []

            for i in labels:    
                data.append(int(df[i][0]))
            
            context = {
                "labels": labels,
                "datas": data,
                "backgroundcolor": BGColor
            }
            return render(request, 'multiple.html', context)

        elif file_extention == 'csv':
            df = pd.read_csv(exel_file)
            df_main = df.iloc[: , 1:]
            labels = df_main.columns.to_list()
            indivusial_labels = df.iloc[: , 0].to_list()
            data = []

            for i in labels:
                data.append(df_main[i].tolist())
            
            context = {
                "labels": labels,
                "datas": data,
                "backgroundcolor": BGColor,
                "indivusial_labels": indivusial_labels
            }
            return render(request, 'multiple.html', context)

    except Exception as e:
        print(e)
    
    return render(request, 'multiple.html')