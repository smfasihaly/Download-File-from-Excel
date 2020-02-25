import requests
import pandas as pd
df = pd.read_csv('Agreements.csv')  
def download(f,name):
    try:
        print('Beginning file download with requests')

        url = f
        r = requests.get(url)
        a = r.headers['content-disposition']
        with open('downloads/'+name+'.pdf', 'wb') as f:
            f.write(r.content)
        
        # Retrieve HTTP meta-data
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        return 'downloads/'+name+'.pdf'
    except:
        pass

urls = df["ECHOSIGN_DEV1__SIGNEDPDF__C"].values.tolist()
names =  df["NAME"].values.tolist()
folders =  df["folder"].values.tolist()

i=0
for url,name,folder in zip(urls,names,folders):
    
    folders[i] = download(url,name+'f'+str(i))
    df["folder"]= folders
    df.to_csv("result.csv", sep=',', encoding='utf-8')
    print(i)
    i+=1

