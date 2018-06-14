#!/bin/bash
scrapy crawl empik

#urls = 
#scrapy shell 

#ksiazka = response.css("div.search-list-item")[0]
#autor = ksiazka.css("a.smartAuthor::text").extract_first()
# autor = autor.encode('ascii', 'replace') # ?
#tytul = ksiazka.css("a.seoTitle strong::text").extract_first()
# tytul = tytul=.encode('ascii', 'replace') # ?
#cena = ksiazka.css("div.price::text").extract_first()
#cena = cena.encode('ascii', 'replace').strip()[:-3] # żeby się pozbyć końcówki "zł"

jsonoutput=empik.json

if [ -f $jsonoutput ];
    then rm -r $jsonoutput
else
    scrapy crawl empik -o empik.json
fi
