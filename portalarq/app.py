from bs4 import BeautifulSoup

# Lee el contenido del archivo HTML
with open("html.txt", "r", encoding="utf-8") as file:
    html_content = file.read()

# Crea un objeto BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Encuentra todos los elementos <a> con la clase "text-decoration-none text-dark"
elements = soup.find_all("a", class_="text-decoration-none text-dark")

# Abre el archivo para escribir los enlaces
with open("hrefs.txt", "w", encoding="utf-8") as output_file:
    # Escribe cada enlace en una nueva línea
    for element in elements:
        href = element.get("href")
        if href:
            output_file.write(f"https://www.portaldearquitectos.com/{href}\n")
