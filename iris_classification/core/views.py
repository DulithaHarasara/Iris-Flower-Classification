from django.shortcuts import render,redirect
from django.http import HttpResponse

from joblib import load

model = load('./mlModels/model.joblib')

result = ''

# Create your views here.
def index(request):

    if request.method == 'POST':
        sepal_length = request.POST.get('sepal_length')
        sepal_width = request.POST.get('sepal_width')
        petal_length = request.POST.get('petal_length')
        petal_width = request.POST.get('petal_width')

        sepal_length = eval(sepal_length)
        sepal_width = eval(sepal_width)
        petal_length = eval(petal_length)
        petal_width = eval(petal_width)

        predResult = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        

        if predResult[0] == 0:
            predResult = 'Setosa'

        elif predResult[0] == 1:
            predResult = 'versicolor'

        else:
            predResult = 'virginica'


        print(predResult)

        return render(request,'index.html',{'predResult':predResult})
    

    return render(request,'index.html')