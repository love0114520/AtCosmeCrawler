from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from AtCosmeCrawler.spiders.brands_spider import BrandsSpider
from AtCosmeCrawler.spiders.products_spider import ProductsSpider

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(BrandsSpider)
    process.crawl(ProductsSpider)
    process.start()  # the script will block here until the crawling is finished
