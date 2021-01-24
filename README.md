# piMDB

A Python IMDB Parser and BBCode Generator. This little tool is useful for posting nice torrent announces on various torrent sites that allow BBCode. It uses IMDBPy as the scraper and retrieves various objects. It also creates a folder in the current working directory of the film name and downloads all the posters on IMDB to that folder - useful for adding art to your psot. 

# Requirements 

- Python 3
- bs4 (BeautifulSoup 4)
- IMDbPY [link](https://imdbpy.github.io/)
- urllib3 (for poster retrieval) 


# Scraped Articles
- Title
- Rating 
- Directors, Writers, Cinematographers, Producers
- Runtime
- 3 random reviews
- Plot
- Awards (if any)
- IMDB Recommendations
- Keywords
- Goofs
- Quotes
- Actor / Role (entire list)
- And others if IMDB has it 

# Note
Imdb is currently in the processing of updating their site and IMDbPY may stop working soon (as of 2021-01-24). If that's the case, hang tight while the IMDbPY team work out the kinks. There should be no loss of information in **pimdb** after IMDbPY is updated. Currently everything works. 

# Example 

To run **pimdb** and download all posters, execute the following at your shell:

> pimdb.py -p https://www.imdb.com/title/tt####### 

or

> pimdb.py https://www.imdb.com/title/tt#######

To just get the scraped objects and BBCode formatting.

## Screenshot

![](https://i.imgur.com/t68Bmhz.jpg)


# Donations

## PayPal
Coding is very time consuming and if you are obliged in offering a donation please click on the following PayPal link

[![paypal](https://i.imgur.com/KSkRsgR.png)](https://www.paypal.com/donate?hosted_button_id=6LXBPHPTDDX56)

## Bitcoin
If you wish to remain anonymous and want to donate via Bitcoin, please send any amount to the following address:

**1QC91r396jYffu1VGBn2TiBAMsYFN5aRq2**

## Monero

**87WZEYd2gcKjp5JhMS15PmH1HTxr7az5h3EYMVrMmZ5Qjp8n7m2622tW97UfqHYWd4apyVXDPXLeMAzkAYAPs2jSHsVzaTj**

