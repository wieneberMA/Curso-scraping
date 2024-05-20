# Importamos las librerías necesarias
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Instalamos la versión de ChromeDriver correspondiente. 
# No es necesario especificar la ruta, el instalador se encarga de eso.
ruta_chromedriver = ChromeDriverManager().install()

# Configuramos el servicio de ChromeDriver con la ruta instalada
s = Service(ruta_chromedriver)

# Instanciamos el WebDriver de Selenium con Chrome
driver = webdriver.Chrome(service=s)

# URL de la petición
url = "https://www.sears.com/patiojoy-np10975ms-patio-3pcs-wicker-swivel-rocker-set/p-A117431005"

# Abrimos la página
driver.get(url)

# Esperamos para que cargue la página o sopa
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extraemos los datos
# Nombre del producto (ejemplo)
#product_title = soup.find('h1', {'class': 'product-title'})
prducto_nombre = soup.find('h1')
print(prducto_nombre)

# Cerramos el navegador
driver.quit()
