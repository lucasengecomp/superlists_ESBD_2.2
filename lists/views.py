from django.shortcuts import render
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		new_item_priority = request.POST['item_priority']
		Item.objects.create(text=new_item_text, priority=new_item_priority)
	else:
		new_item_text = ''
		new_item_priority = ''		

	return render(request, 'home.html', {
		'new_item_text': new_item_text,
		'new_item_priority': new_item_priority
	})