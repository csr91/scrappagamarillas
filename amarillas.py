# CODIGO BASE PARA SCRAPPING DE PAGINAS AMARILLAS CON OBTENCION DE TOKEN Y PAGINADO
# SE PUEDE UTILIZAR PARA CUALQUIER BUSQUEDA DENTRO DE LA PAGINA PREVIA REALIZACIÖN DEL MAPPING
# HAY UN ERROR DE ENCOLUMNADO EN EL ARMADO DEL CSV


import csv
import requests

# Paso 1: Obtener el token
token_url = "https://keycloak.gurusoluciones.com/auth/realms/Comunidad/protocol/openid-connect/token"
token_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "97",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "keycloak.gurusoluciones.com",
    "Origin": "https://www.paginasamarillas.com.ar",
    "Referer": "https://www.paginasamarillas.com.ar/",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

token_data = {
    "grant_type": "client_credentials",
    "client_id": "guru-pacom",
    "client_secret": "DxdgQ9d292kYEM9ZoYCqMueg9fChB6AO"
}

token_response = requests.post(token_url, headers=token_headers, data=token_data)
token = token_response.json().get("access_token")

# Paso 2: Realizar bucle a través de las páginas y escribir en un archivo CSV
csv_filename = "resultados.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    # Definir el encabezado del CSV
    csv_writer = csv.writer(csv_file)
    header = ["id", "name", "accountId", "hasaddress", "infoempresa", "web", "addressLocality", "streetName",
              "streetNumber", "floor", "latitude", "longitude", "localityToShow", "phoneToShow", "freeCallNumber", "emails"]
    csv_writer.writerow(header)

    # Realizar bucle a través de las páginas
    for page in range(1, 49):
        # URL de búsqueda para cada página
        search_url = f"https://solr.paginasamarillas.com.ar/advertisements?searchWord=arquitectos&locationWord=buenos-aires&page={page}&size=15"

        # Headers del request de búsqueda
        search_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7",
            "Authorization": f"Bearer {token}",
            "Connection": "keep-alive",
            "Host": "solr.paginasamarillas.com.ar",
            "Origin": "https://www.paginasamarillas.com.ar",
            "Referer": "https://www.paginasamarillas.com.ar/",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        # Realizar la solicitud GET con el token en el encabezado de autorización
        search_response = requests.get(search_url, headers=search_headers)

        # Procesar los resultados
        results = search_response.json().get("results", [])

        for result in results:
            # Extraer la información específica que necesitas
            info_to_keep = [
                result.get("id"),
                result.get("name"),
                result.get("accountId"),
                result.get("hasAddress"),
                result.get("infoEmpresa"),
                "|".join(result.get("contactMap", {}).get("WEB", [])),  # Convertir la lista a cadena separada por '|'
                result.get("mainAddress", {}).get("addressLocality"),
                result.get("mainAddress", {}).get("streetName"),
                result.get("mainAddress", {}).get("streetNumber"),
                result.get("mainAddress", {}).get("floor"),
                result.get("mainAddress", {}).get("latitude"),
                result.get("mainAddress", {}).get("longitude"),
                result.get("mainAddress", {}).get("localityToShow"),
                result.get("mainAddress", {}).get("allPhonesList", [])[0].get("phoneToShow", ""),
                result.get("mainAddress", {}).get("allPhonesList", [])[0].get("freeCallNumber", ""),
                "|".join(result.get("emails", [])),  # Convertir la lista a cadena separada por '|'
            ]

            # Escribir la información en el archivo CSV
            csv_writer.writerow(info_to_keep)

print(f"La información se ha guardado en el archivo CSV: {csv_filename}")