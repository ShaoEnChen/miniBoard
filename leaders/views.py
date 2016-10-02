from django.shortcuts import render, redirect
from .models import Record

query = "SELECT * FROM leaders_record ORDER BY height DESC LIMIT 5"
	
def board_view(request):
	results = Record.objects.raw(query)
	try:
		isEmpty = Record.objects.raw(query)[0]
	except:
		isEmpty = None
	return render(request, 'leaderboard.html', {
		'isEmpty': isEmpty,
		'results': results
	})

def add_record(request):
	if request.method == 'POST':
		if 'name' in request.POST and 'height' in request.POST and 'contact' in request.POST:
			name = request.POST['name']
			height = request.POST['height']
			contact = request.POST['contact']
			Record.objects.create(name = name, height = height, contact = contact)
	return redirect('/')