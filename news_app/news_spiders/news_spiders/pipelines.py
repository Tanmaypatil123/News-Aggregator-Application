# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from main.models import News_data

import logging, coloredlogs
logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)

class NewsSpidersPipeline:
    def process_item(self, item, spider):
        try:
            News_data.objects.create(heading=item['heading'], img=item['img'],url=item['url'],content =item['content'],date = item["date"],category = item['category'])
            print("\n")
            logger.warn("Loaded news {}".format(item['heading']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error("\nFailed to load news, Reason For Failure:{}".format(e))
            print(item)
        return item
