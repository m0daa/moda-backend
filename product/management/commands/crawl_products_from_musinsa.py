import asyncio
import aiohttp
from django.core.management.base import BaseCommand
from product.models import Product


class Command(BaseCommand):
    help = "Crawl products from musinsa and save to database asynchronously"

    async def fetch_data(self, session, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        async with session.get(url, headers=headers) as response:
            return await response.json()

    async def process_data(self, url):
        async with aiohttp.ClientSession() as session:
            response = await self.fetch_data(session, url)
            return response

    def handle(self, *args, **kwargs):
        outer_url = "https://api.musinsa.com/api2/hm/v2/pans/ranking?storeCode=musinsa&sectionId=200&categoryCode=002000&contentsId=&gf=A"
        top_url = "https://api.musinsa.com/api2/hm/v2/pans/ranking?storeCode=musinsa&sectionId=200&categoryCode=001000&contentsId=&gf=A"
        bottom_url = "https://api.musinsa.com/api2/hm/v2/pans/ranking?storeCode=musinsa&sectionId=200&categoryCode=003000&contentsId=&gf=A"
        shoes_url = "https://api.musinsa.com/api2/hm/v2/pans/ranking?storeCode=musinsa&sectionId=200&categoryCode=103000&contentsId=&gf=A"
        bag_url = "https://api.musinsa.com/api2/hm/v2/pans/ranking?storeCode=musinsa&sectionId=200&categoryCode=004000&contentsId=&gf=A"
        accessories = "https://api.musinsa.com/api2/hm/v2/pans/ranking?storeCode=musinsa&sectionId=200&categoryCode=101000&contentsId=&gf=A"

        urls = [top_url, bottom_url, outer_url, shoes_url, bag_url, accessories]

        async def crawl():
            tasks = [self.process_data(url) for url in urls]
            return await asyncio.gather(*tasks)

        results = asyncio.run(crawl())

        category_map = {
            top_url: "top",
            bottom_url: "bottom",
            outer_url: "outer",
            shoes_url: "shoes",
            bag_url: "bag",
            accessories: "accessories",
        }

        for url, response in zip(urls, results):
            category = category_map.get(url, "accessories")
            for i in range(3, 100):
                for j in range(0, 3):
                    item = response["data"]["modules"][i]["items"][j]
                    brand_name = item["info"].get("brandName")
                    product_name = item["info"].get("productName")
                    price = item["info"].get("finalPrice")
                    image_url = item["image"].get("url")

                    if brand_name:
                        product, created = Product.objects.update_or_create(
                            name=product_name,
                            defaults={
                                "brand": brand_name,
                                "category": category,
                                "price": price,
                                "image_url": image_url,
                            },
                        )

        self.stdout.write(self.style.SUCCESS("Crawling completed!"))
