import requests
import pandas as pd
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup

searchterms = [#list of terms to search
]
# Insert search terms here. These are no case sensitive.

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
# Headers required for requests module appear as a legitimate IP making a request against the server

def searchterms_change(searchterms):
    # changes the searchterms to lowercase, then appends uppercase, and titlecase to terms
    searchterms = [term.lower() for term in searchterms]
    capital = [term.title() for term in searchterms]
    upper = [term.upper() for term in searchterms]

    [searchterms.append(i) for i in capital]
    [searchterms.append(i) for i in upper]
    return searchterms


def csv(csvfile):
    # Opens CSV and returns list of domains
    with open(csvfile, 'r') as csv_file:
        domains = [str(domain).strip() for domain in csv_file]
    return domains

def search(newsoup):
    # checks if the search terms are found within the source code of the
    found = ''
    for item in searchterms:
        if item in newsoup and item not in found:
            if not found:
                found += item
            else:
                found += ', ' + item

    return found or 'Nothing found'

def bs4_status(domains=None):
    # takes list of domains and runs a requests check for status codes
    results = []
    codes = []
    for domain in domains:
        try:
            if 'https://' not in domain:
                r = requests.get('https://' + domain, headers=headers, timeout=10.0)
            else:
                r = requests.get(domain, headers=headers, timeout=10.0)

            status_code = r.status_code
            codes.append(status_code)

            # beautiful soup request for HTML, CSS, and JS code

            soup = BeautifulSoup(r.content, 'html.parser')
            newsoup = soup.prettify()
            results.append(search(newsoup))

        except requests.exceptions.ReadTimeout:
            codes.append('Timeout Error')
        except requests.exceptions.TooManyRedirects:
            codes.append('Too many redirects')
        except requests.exceptions.ConnectionError:
            codes.append('Connection Error')
        except Exception as ex:
            codes.append(ex)
        finally:
            # default value to ensure arrays are same length
            if len(results) < len(codes):
                results.append('No search made')
    return domains, codes, results


def panda_out(domains, codes, results):
    today = date.today()
    domain_res = pd.DataFrame(
        {'Domains': domains,
         'Status': codes,
         'Search Terms': results
        })
    domain_res.to_csv(f'output_{today}.csv')
    return domain_res

if __name__ == "__main__":
    start_time = datetime.now()
    searchterms_change(searchterms)
    domains = csv(csvfile='#csvfile to take domain list from')
    domains, codes, results = bs4_status(domains)
    print(panda_out(domains, codes, results))
    print("Script finished!")
    time_taken = datetime.now() - start_time
    print(f"This script took: {time_taken} to complete")


"""
Created by Joe Attwood, 17/04/2020
"""
