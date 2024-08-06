from scholarly import scholarly
import time


def search_articles(keywords, num_results=10):
    articles = []
    for keyword in keywords:
        query = f"{keyword} air travel accessibility"
        search_query = scholarly.search_pubs(query)

        for i in range(num_results):
            try:
                article = next(search_query)
                bib = article['bib']
                authors = " and ".join(bib.get('author', []))
                articles.append({
                    'keyword': keyword,
                    'title': bib.get('title', ''),
                    'abstract': bib.get('abstract', ''),
                    'year': bib.get('pub_year', ''),
                    'url': article.get('pub_url', ''),
                    'volume': bib.get('volume', ''),
                    'issue': bib.get('issue', ''),
                    'start_page': bib.get('start_page', ''),
                    'end_page': bib.get('end_page', ''),
                    'authors': authors,
                    'doi': article.get('doi', '')  # Add DOI field
                })
                time.sleep(2)  # Delay to avoid overwhelming the service
            except StopIteration:
                break

    return articles


def save_to_ris(articles, filename):
    with open(filename, 'w', encoding='utf-8') as risfile:
        for article in articles:
            risfile.write("TY  - JOUR\n")  # Assuming all are journal articles
            risfile.write(f"AU  - {article['authors']}\n")
            risfile.write(f"TI  - {article['title']}\n")
            risfile.write(f"AB  - {article['abstract']}\n")
            risfile.write(f"PY  - {article['year']}\n")
            risfile.write(f"VL  - {article['volume']}\n")
            risfile.write(f"IS  - {article['issue']}\n")
            risfile.write(f"SP  - {article['start_page']}\n")
            risfile.write(f"EP  - {article['end_page']}\n")
            risfile.write(f"UR  - {article['url']}\n")
            risfile.write(f"DO  - {article['doi']}\n")  # Add DOI to RIS file
            risfile.write("ER  - \n\n")  # End of the record


# Keywords based on the consolidated list
# keywords = [
#     "Wheelchair damage", "Air travel", "Washroom accessibility", "Manual handling", 
#     "Negative attitudes", "Manual lifting", "Aircraft size", "Wait times", "Emotional distress",
#     "Disability", "Anxiety", "Staff training", "Mobility impairment", "Complexity", 
#     "Transfers", "Aircraft seats", "Wheelchairs", "In-cabin securements", "Tourism",
#     "Barriers", "Mobility disability", "Physical difficulities", "Rural airports",
#     "International airports", "Mobility device damage", "Assistive devices damage",
#     "Discrimination", "Insurance", "People with disabilities", "Prisma protocol",
#     "Environmental barriers", "Caregiver", "Travel agents", "Booking", "Solutions",
#     "Special assistance", "Special accomodation", "Satisfaction", "Disatisfaction",
#     "Scheduling model", "Escorts model", "Egress", "Reduced mobility",
#     "Airport employee", "Airline employees", "Training", "Mobility devices", "Communication (attitude)",
#     "Social difficulties", "Invisible disability", "Dementia", "Security (TCA checkpoints)", "Deafblind", 
#     "Travel associations", "Social model", "Spinal cord injury", "Public transportation", "Booking websites", "Autism spectrum disorder",
#     "airline staff", "damage repair", "safe securement", "securement point", "securement bracket", "wheelchair safety", 
#     "handling checklist", "restraint systems", "wheelchair standards", "mobility aid design", "wheelchair design", "boarding",
#     "disassembly", "reassembly", "onboard assistance", "limits of liability"
# ]

keywords = ["beetle", "elytra"]

articles = search_articles(keywords, num_results=10)
save_to_ris(articles, 'test.ris')