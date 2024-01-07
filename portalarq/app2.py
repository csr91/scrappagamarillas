from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuración para ejecutar Chrome en modo sin cabeza
chrome_options = Options()
chrome_options.add_argument('--headless')  # Ejecuta en modo sin cabeza (sin interfaz gráfica)

# Ruta al driver de Chrome (descárgalo de https://sites.google.com/chromium.org/driver/)
chrome_driver_path = '/ruta/al/chromedriver'

# URL a la que deseas realizar la solicitud
url = "https://www.portaldearquitectos.com//estudios/argentina/buenos-aires/estudios/granz-srl"

# Inicializar el navegador
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Realizar la solicitud al sitio web
driver.get(url)

# Esperar a que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)
driver.implicitly_wait(10)

# Obtener el contenido HTML después de las cargas dinámicas
html_content = driver.page_source

# Guardar el contenido HTML en un archivo
with open('output.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

# Cerrar el navegador
driver.quit()

print("Contenido HTML guardado en 'output.html'.")
