import requests

# Predefine some lists
scam_urls = []
complete_list = []

# download latest list of domains
url = 'https://raw.githubusercontent.com/BuyMyMojo/discord-scam-links/steam-free-nutro_ru_com/list.txt'
discord_scam_list = requests.get(url).text
scam_links_1 = discord_scam_list.split("\n")  # Turn into list

# For each url in list get the domain from before the '.'
for scam_url in scam_links_1:
    if scam_url != '':
        scam_urls.append(scam_url.partition('.')[0])

# Remove duplicates caused by the last process
no_dupe_list = list(dict.fromkeys(scam_urls))

# Download an up-to-date list of all available top level domains AKA the things that come after the '.' in URLs
url2 = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
top_level_domains_text = requests.get(url2).text
top_level_domains1 = top_level_domains_text.split("\n")  # Turn into list
top_level_domains1.pop(0)  # remove the first line of text

# For every top level domain create a new url based of the previous list
for TLD in top_level_domains1:
    if TLD != '':
        for base_URL in no_dupe_list:
            full_url = base_URL + '.' + TLD
            complete_list.append(full_url)

# remove any duplicates just in case and sort alphabetically
all_scam_urls = sorted(list(dict.fromkeys(complete_list)))

# Write list to a separate txt file for manual merging
textfile = open("list-all-TLD.txt", "w")
for element in all_scam_urls:
    textfile.write(element + "\n")
textfile.close()

