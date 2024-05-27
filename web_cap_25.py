from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#definir el tipo de busqueda de selenium
from selenium.webdriver.common.by import By
def iniciar_chrome():
    """
    Inicia el navegador Chrome en modo incógnito con opciones configuradas.
    
    Returns:
        driver: Objeto WebDriver de Selenium para interactuar con Chrome.
    """
    # Define las opciones de Chrome
    options = Options()
    options.add_argument("--incognito")  # Inicia Chrome en modo incógnito
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")  # Define el agente de usuario personalizado
    
    # Configuraciones adicionales para Chrome
    options.add_argument("--start-maximized")  # Maximiza la ventana de Chrome
    options.add_argument("--disable-web-security")  # Deshabilita la política del mismo origen
    options.add_argument("--disable-extensions")  # Deshabilita las extensiones de Chrome
    options.add_argument("--disable-notifications")  # Bloquea las notificaciones de Chrome
    options.add_argument("--ignore-certificate-errors")  # Ignora los errores de certificado
    options.add_argument("--no-sandbox")  # Deshabilita el modo sandbox
    options.add_argument("--log-level=3")  # Minimiza la salida de logs de ChromeDriver
    options.add_argument("--allow-running-insecure-content")  # Permite contenido inseguro
    options.add_argument("--no-default-browser-check")  # Evita el aviso de navegador por defecto
    options.add_argument("--no-first-run")  # Evita tareas de primera ejecución
    options.add_argument("--no-proxy-server")  # No usa un servidor proxy
    options.add_argument("--disable-blink-features=AutomationControlled")
    #parametros a omitir en el inicio de chrome
    exp_opt = [
        'enable-automation',#para que no muestre la notificacuion "un sofware esta automatizando este navegador"
        'ignore-certificate-errors',#para ignorar errores de certificado
        'enable-logging'#para que no se muestre en la terminal "devtools listening etc..."
    ]
    options.add_experimental_option("excludeSwitches",exp_opt)#
    #parametros que definen las preferencias de chrome
    prefs ={
        "profile.default_content_setting_values.notifications":2,#Notificaciones 0 = preguntar 1= permitir 2 = no permitir
        "intl.accept_languages":["es-ES","es"],#para deinifi el idioma del navegador
        "credentials_enable_service":False#para evitar que chrome nos pregunte si queremos guardar la contraseña al loguearnos
    }
    options.add_experimental_option("prefs",prefs)#
    
    # Instala y configura ChromeDriver
    ruta = ChromeDriverManager().install()
    service = Service(ruta)
    
    # Inicializa el WebDriver de Selenium con Chrome
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

if __name__ == '__main__':
    driver = iniciar_chrome()
    url = "https://www.gamestop.com/pc-gaming/keyboards/products/geeknet-star-wars-boba-fett-wired-gaming-keyboard-gamestop-exclusive/328167.html"
    print(f"Accediendo a la URL: {url}")
    driver.get(url)
    
    # Usar esperas explícitas para esperar a que el elemento esté presente
    try:
        nombre_producto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-name-section"))
        ).text
        print(nombre_producto)
    except Exception as e:
        print(f"Error al encontrar el elemento: {e}")
    
    driver.quit()
