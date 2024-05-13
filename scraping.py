import requests
from bs4 import BeautifulSoup
import re
#colores
azul = "\33[1;36m"
gris = "\33[0;37m"
blanco = "\33[0;37m"

def datos_page(url):
    d ={}
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
    
    print(f'{azul}REalizo la peticion: {blanco}{url}{gris}')
    req = requests.get(url, headers=headers, timeout=10)
    print(f'{azul}Codigo  de respuesta ......: {blanco}{req.status_code}{req.reason}{gris}')
    if req.status_code != 200:
        return {"ERROR": f"{req.reason}","statust_code":f"{req.status_code}"}
    d["url"] = req.url
    d["id"] = d["url"].split("/")[-1]
    soup = BeautifulSoup(req.text, "html.parser")
    d["nombre_producto"]=soup.find("h1", class_= "product-title").text.string()
    d["url_imagen"] = soup.find("img", id = "product-conver").attrs.get("src")
    objs_plat = soup.find("dd").find_all("a")
    d["plataformas"]=[]
    for item in objs_plat:
        d["plataformas"].append(item.text.strip())
        
    try:
        c_point = soup.find("a",class_="reviews-point ")
        




# URL del sitio web desde el que queremos raspar datos
url = "https://es.wikipedia.org/wiki/Wikipedia_en_espa%C3%B1ol"

# Definimos el header con el User-Agent para simular una solicitud desde un navegador

try:
    # Realizamos la solicitud GET
    res = requests.get(url, headers=headers, timeout=10)
    
    # Verificamos que la solicitud fue exitosa
    print( res.raise_for_status()) 

except requests.RequestException as e:
    # Manejo de excepciones si la solicitud falla
    print("Ocurrió un error al hacer la solicitud:", e)
