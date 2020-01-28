import numpy as np
from django.shortcuts import render
from .forms import PredictionForm
from .classifier import make_prediction


def home(request):
	return render(request, 'estimator/home.html')

def dataset(request):
	return render(request, 'estimator/dataset.html', {'title': 'Dataset'})

def predict(request):
	if request.method == 'POST':
		form = PredictionForm(request.POST)
		if form.is_valid():
			pred_sepal_length = float(form.cleaned_data['sepal_length'])
			pred_sepal_width = float(form.cleaned_data['sepal_width'])
			pred_petal_length = float(form.cleaned_data['petal_length'])
			pred_petal_width = float(form.cleaned_data['petal_width'])
			arr = [float(form.cleaned_data[key]) for key in form.cleaned_data.keys()]
			arr = np.array(arr).reshape(1, -1)
			prediction = make_prediction(arr)
			print("Prediction: ", prediction)
	else:
		form = PredictionForm()
		prediction = ''
	return render(request, 'estimator/predict.html', {'form': form, 'prediction': prediction})
