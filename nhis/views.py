from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .crawling import find_smokectr,find_dimctr
from rest_framework.response import Response
from .serializers import QuestionSerializer
from rest_framework.decorators import api_view


def index(request):
    
	res = find_dimctr('용인시')

	dimen_ctr = []

	for number in res:
		dimen_ctr.append({'dimen_logt':number['REFINE_WGS84_LOGT'],
			'dimen_lat':number['REFINE_WGS84_LAT']})

	return render(request, 'nhis/index.html',{'dimen_ctr':dimen_ctr})

def get_smokectr(request, high_city, low_city):
    
	city = high_city + ' ' + low_city
	res = find_smokectr()
	smoke_ctr = []

	for key in res:
		if key.startswith(city) :
			smoke_ctr.append({'smoke_ctr': key})

	return JsonResponse(smoke_ctr)


def get_dimenctr(request, city_name):
    
	res = find_dimctr(city_name)

	dimen_ctr = []

	for number in res:
		dimen_ctr.append({'dimen_logt':number['REFINE_WGS84_LOGT'],
			'dimen_lat':number['REFINE_WGS84_LAT']})

	return JsonResponse(dimen_ctr)

