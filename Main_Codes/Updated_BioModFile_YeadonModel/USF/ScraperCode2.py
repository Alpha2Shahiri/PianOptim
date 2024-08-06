from scholarly import scholarly
import csv
import time


def search_articles(keywords, num_results=10, pages=3):
    articles = []
    for keyword in keywords:
        query = f"{keyword}"
        search_query = scholarly.search_pubs(query)

        for page in range(pages):
            try:
                for i in range(num_results):
                    article = next(search_query)
                    articles.append({
                        'keyword': keyword,
                        'title': article['bib'].get('title', ''),
                        'abstract': article['bib'].get('abstract', ''),
                        'year': article['bib'].get('pub_year', ''),
                        'url': article.get('pub_url', '')
                    })
                    time.sleep(2)  # Delay to avoid overwhelming the service
            except StopIteration:
                break
            except Exception as e:
                print(f"An error occurred on page {page + 1}: {e}")
                continue

    return articles


def save_to_csv(articles, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['keyword', 'title', 'abstract', 'year', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for article in articles:
                writer.writerow(article)
        print(f"Results successfully saved to {filename}")
    except Exception as e:
        print(f"Failed to save results to CSV: {e}")


# Keywords based on the consolidated list
keywords = [
    "toughening mechanism elytra beetle",
    "Mechanical properties of the beetle elytron"
]

articles = search_articles(keywords, num_results=10, pages=3)
save_to_csv(articles, '/home/alpha/Desktop/Code/results.csv')
