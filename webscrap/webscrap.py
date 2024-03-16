from autoscraper import AutoScraper
Puma_url="https://in.puma.com/in/en/mens"

wanted_list=["4,559","Aviator Unisex Running Shoes"]

scraper=AutoScraper()
result=scraper.build(Puma_url,wanted_list)

print(scraper.get_result_similar(Puma_url,grouped=True))


