## 4. Unidade 2 - Desenvolvimento de Aplicação Utilizando TDD
## 4.1. Situação Problema da Unidade 2
## Para a execução da atividade, abaixo é apresentada a proposta da história de usuário a ser implementada. Observa-se que ela é semelhante a que desenvolvemos durante a aula mas, suas diferenças implicarão na implementação de uma aplicação ligeiramente diferente.
## 
##  
## 
## Segue abaixo o esboço da classe de teste functional_test.py que irá guiar todo o processo de implementação da to-do list com prioridades.

############################## INICIO ####################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVsitorTest(unittest.TestCase): 

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    # Auxiliary method 
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar que agora a aplicação online de lista de tarefas
        # aceita definir prioridades nas tarefas do tipo baixa, média e alta
        # Ela decide verificar a homepage
        
        self.browser.get("http://localhost:8000")

        # Ela percebe que o título da página e o cabeçalho mencionam
        # listas de tarefas com prioridade (priority to-do)
        
        self.assertIn('Priority To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Priority To-Do', header_text)

        # Ela é convidada a inserir um item de tarefa e a prioridade da 
        # mesma imediatamente

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
        )

        # Ela digita "Comprar anzol" em uma nova caixa de texto
        # e assinala prioridade alta no campo de seleção de prioridades
        
        inputbox.send_keys('Comprar anzol')

        inputcheckbox = self.browser.find_element_by_id('id_high_priority')
        self.assertEqual(
        inputcheckbox.get_attribute('value'),
        'prioridade alta'
        )
        inputcheckbox.click()

        # Quando ela tecla enter, a página é atualizada, e agora
        # a página lista "1 - Comprar anzol - prioridade alta"
        # como um item em uma lista de tarefas
        
        
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1 - Comprar anzol', [row.text for row in rows])

        # Ainda continua havendo uma caixa de texto convidando-a a 
        # acrescentar outro item. Ela insere "Comprar cola instantâne"
        # e assinala prioridade baixa pois ela ainda tem cola suficiente
        # por algum tempo

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Comprar cola instantânea")
                
        inputcheckbox = self.browser.find_element_by_id('id_low_priority')
        self.assertEqual(inputcheckbox.get_attribute('value'),'prioridade baixa')
        
        inputcheckbox.click()
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        # A página é atualizada novamente e agora mostra os dois
        # itens em sua lista e as respectivas prioridades
        self.check_for_row_in_list_table('1 - Comprar anzol')
        self.check_for_row_in_list_table('2 - Comprar cola instantânea')

        # Edith se pergunta se o site lembrará de sua lista. Então
        # ela nota que o site gerou um URL único para ela -- há um
        # pequeno texto explicativo para isso.
        

        self.fail('Finish the test!')
        # Ela acessa essa URL -- sua lista de tarefas continua lá.

 

################################# FIM ####################################


if __name__ == '__main__':
        unittest.main()