from autoscraper import AutoScraper

scraper = AutoScraper()
url = 'https://example.com'  

wanted_list = ['Your Target Data Here']  

scraper.build(url, wanted_list)

results = scraper.get_result_similar(url, group_by_alias=True)

print(results)
