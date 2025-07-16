import asyncio
import httpx

API_URL = "https://youdo.com/api/tasks/tasks/"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Referer": "https://youdo.com/tasks-all-opened-all",
    "X-Requested-With": "XMLHttpRequest",
    # можно добавить другие заголовки, если начнут блокировать
}

# Пример тела запроса (может быть другим — уточняется через DevTools → Payload)
PAYLOAD = {
    "page": 1,
    "page_size": 20,
    "ordering": "-publication_date",
    "status": "opened",
    "search": "",
    "location": None,
    "categories": [],
    "price_from": None,
    "price_to": None,
    "online": None,
}


async def fetch_tasks():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            API_URL,
            json=PAYLOAD,
            headers=HEADERS,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("ResultObject", []).get("Items", [])


async def main():
    tasks = await fetch_tasks()
    for task in tasks:
        print(
            {
                "title": task.get("Name"),
                "is_actual": task.get("IsActual"),
                "status_flag": task.get("StatusFlag"),
                "budget": task.get("BudgetDescription"),
                "category": task.get("CategoryFlag"),
                "deadline": task.get("DateTimeString"),
                "address": task.get("Address"),
                "link": f"https://youdo.com{task.get('Url')}",
            }
        )


async def get_jobs_by_category(category: str):
    tasks = await fetch_tasks()
    result = []
    for task in tasks:
        if task.get("CategoryFlag") == category:
            result.append(
                {
                    "title": task.get("Name"),
                    "is_actual": task.get("IsActual"),
                    "status_flag": task.get("StatusFlag"),
                    "budget": task.get("BudgetDescription"),
                    "category": task.get("CategoryFlag"),
                    "deadline": task.get("DateTimeString"),
                    "address": task.get("Address"),
                    "link": f"https://youdo.com{task.get('Url')}",
                }
            )
    return result


if __name__ == "__main__":
    asyncio.run(get_jobs_by_category(category="techrepair"))
