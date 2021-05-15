from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request, 'home.html', {
		'new_item_text': request.POST.get('item_text', ''),
		'new_item_priority': request.POST.get('item_priority', '').split(' | ')
	})