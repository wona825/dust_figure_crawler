import matplotlib.pyplot as plt
import matplotlib
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%88%98%EC%B9%98+%ED%81%AC%EB%A1%A4%EB%A7%81&tqi=h5nGWwp0J1ZssEm7srNssssss3w-357383') as response:
    soup = BeautifulSoup(response,'html.parser')
    #print(soup)

    dust = soup.find('div',{'class':'tb_scroll'})
    #print(dust)
    dust_region_information = dust.select('th')
    print(dust_region_information)

    dust_region = []
    for i in dust_region_information:
        i.text
        dust_region.append(i.text)
    print(dust_region)
    dust_region.remove('관측지점')
    dust_region.remove('현재')
    dust_region.remove('오전예보')
    dust_region.remove('오후예보')
    print(dust_region)

    dust_figure_information = dust.select('td')
    print(dust_figure_information)
