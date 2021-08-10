link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
import time
import pytest


def test_present_button(browser):
    browser.get(link)
    time.sleep(2)
    btn=browser.find_element_by_xpath("//button[@type='submit']")
    
    if ('--language'=="es"):
        assert btn.text=="Añadir al carrito", "another language"


    elif('--language'=="fr"):
        assert btn.text=="Ajouter au panier", "another language"

    #безполезный assert, так как если кнопка не будет найдена то всеравно выбросыться исключение, а assert не будет выполнен
    # но в задании сказано его всунуть, вот пожалуйста

    assert btn != None, "button not found"
    




        
   
      
    

        

