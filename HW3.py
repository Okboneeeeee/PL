import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def crawl_ptt_nba():
    url = "https://www.ptt.cc/bbs/NBA/index.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("div", class_="r-ent")
        
        titles = []
        authors = []
        dates = []
        for article in articles:
            title = article.find("div", class_="title").text.strip()
            author = article.find("div", class_="author").text.strip()
            date = article.find("div", class_="date").text.strip()
            
            titles.append(title)
            authors.append(author)
            dates.append(date)
            
        return titles, authors, dates
    else:
        print("Failed to retrieve PTT NBA")

def create_dataframe(titles, authors, dates):
    df = pd.DataFrame({'Title': titles, 'Author': authors, 'Date': dates})
    return df

def create_dict(titles, authors, dates):
    data_dict = [{'Title': title, 'Author': author, 'Date': date} for title, author, date in zip(titles, authors, dates)]
    return data_dict

if __name__ == "__main__":
    titles, authors, dates = crawl_ptt_nba()
    
    # Create DataFrame
    df = create_dataframe(titles, authors, dates)
    print("DataFrame:")
    print(df)

    # Create dictionary
    data_dict = create_dict(titles, authors, dates)
    print("\nDictionary:")
    print(data_dict)

# Save dictionary as JSON
    with open('ptt_nba.json', 'w') as json_file:
        json.dump(data_dict, json_file)

    # Save DataFrame as CSV
    df.to_csv('ptt_nba.csv', index=False)