import requests
from bs4 import BeautifulSoup
import time

def scrape_jobs_with_relocation(url, keyword, max_pages=5):
    try:
        for page in range(1, max_pages + 1):
            page_url = f"{url}?page={page}"
            response = requests.get(page_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                job_links = soup.select('div.job-list-items a.JobListItems__anchor')

                if not job_links:
                    print(f"No job links found on page {page}. Exiting.")
                    break

                print(f"Checking for '{keyword}' in job links on page {page}:")
                for link in job_links:
                    job_url = link.get('href')
                    job_title = link.text.strip()

                    # Check if the keyword is present in the job title or URL
                    if keyword.lower() in job_title.lower() or keyword.lower() in job_url.lower():
                        print(f"Keyword found in job: '{job_title}' ({job_url})")

                time.sleep(2)  # Adding a delay to avoid rate limits

            else:
                print(f"Failed to retrieve page {page}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    job_listing_url = 'https://picnic.app/careers/all-jobs'
    keyword_to_check = 'assortiment'  # Change this to the keyword you are looking for

    try:
        max_pages_to_scrape = 5  # Set the maximum number of pages to scrape
        scrape_jobs_with_relocation(job_listing_url, keyword_to_check, max_pages_to_scrape)

    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
