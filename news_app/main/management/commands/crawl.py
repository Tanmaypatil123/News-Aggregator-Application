from django.core.management.base import BaseCommand
from news_spiders.news_spiders.spiders.news_spider import NewsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
from pathlib import Path
class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        django_path = Path(__file__).resolve().parent.parent.parent.parent
        os.chdir(str(django_path)+"/news_spiders")
        os.system("scrapy crawl news")

