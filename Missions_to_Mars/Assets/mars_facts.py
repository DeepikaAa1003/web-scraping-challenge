import pandas as pd

# ### Mars Facts

def mars_facts():

    url = 'https://space-facts.com/mars/'


    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description', 'Value']
    df.head()
    df = df.set_index('Description')
    html_table = df.to_html(classes="table table-striped")
    html_table.replace('\n', '')
    df.to_html('table.html')
    print(html_table)
    return html_table