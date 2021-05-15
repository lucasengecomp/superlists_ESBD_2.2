from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from lists.models import Item

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEquals(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_only_saves_items_when_necessary(self):
		self.client.get('/')
		self.assertEquals(Item.objects.count(), 0)	

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item', 'item_priority': "Prioridade Alta"})

		self.assertEquals(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEquals(new_item.text, 'A new list item')
		self.assertEquals(new_item.priority, "Prioridade Alta")

		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

	def test_saving_and_retriving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.priority = "Prioridade Alta"
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.priority = "Prioridade Baixa"
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEquals(saved_items.count(),2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]

		self.assertEquals(first_saved_item.text, 'The first (ever) list item')		
		self.assertEquals(first_item.priority, "Prioridade Alta")
		self.assertEquals(second_saved_item.text, 'Item the second')
		self.assertEquals(second_saved_item.priority, "Prioridade Baixa")		