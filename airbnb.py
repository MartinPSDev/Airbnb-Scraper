from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Ir a la URL de búsqueda de Airbnb
        await page.goto("https://www.airbnb.com.ar/s/Río-de-Janeiro--Brasil/homes?checkin=2025-02-13&checkout=2025-02-16&adults=2")

        # Esperar a que la página cargue completamente
        await page.wait_for_load_state("networkidle") 

        # Capturar TODO el texto visible en la página
        text = await page.inner_text("body")

        # Mostrar el contenido en la consola
        print(text)

        await browser.close()  # Cierra el navegador cuando termina

asyncio.run(main())
