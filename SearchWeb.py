import urllib.request



main = 'http://www.devx.com/opensource/archives/'
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
years = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

search_str = 'pack'

for i in range(len(years)):
    for j in range(len(months)):
        url = main + str(years[i]) + str(months[j])
        html_content = urllib.request.urlopen(url).read()
        loc = html_content.find(search_str.encode())
        print(url)
        print(loc)

