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


    dust_region = []
    for i in dust_region_information:
        i.string
        dust_region.append(i.text)

    dust_region.remove('관측지점')
    dust_region.remove('현재')
    dust_region.remove('오전예보')
    dust_region.remove('오후예보')
    print(dust_region)

    dust_figure = []
    dust_figure_information = dust.find_all('span')
    for i in dust_figure_information:
        k = i.get_text()
        dust_figure.append(k)
    figure = []
    for j in range(len(dust_figure)):
        if j%3 == 0:
            figure.append(dust_figure[j])
    print(figure)



    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.title('지역별 미세먼지 농도')
    plt.bar(x, figure)
    plt.xticks(x, dust_region)
    plt.show()