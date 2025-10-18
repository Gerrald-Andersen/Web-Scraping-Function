import requests
from bs4 import BeautifulSoup
from typing import List, Tuple

def decode_message(url: str) -> None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table')
        if not table:
            print("Table not found.")
            return

        data: List[Tuple[int, str, int]] = []
        max_x, max_y = 0, 0

        for row in table.find_all('tr')[1:]:
            cells = row.find_all(['td', 'th'])
            if len(cells) != 3:
                continue
            try:
                x = int(cells[0].get_text(strip=True))
                char = cells[1].get_text(strip=True)
                y = int(cells[2].get_text(strip=True))
                data.append((x, char, y))
                max_x = max(max_x, x)
                max_y = max(max_y, y)
            except ValueError:
                continue

        if not data:
            print("There is no valid data to process.")
            return

        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for x, char, y in data:
            grid[y][x] = char

        for row in grid:
            print(''.join(row))

    except requests.RequestException as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

decode_message('https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub')