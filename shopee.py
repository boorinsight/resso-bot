#Load semua library yang dibutuhkan
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time 

def scrap (brand, first_page, last_page):
#menyiapkan dataset yang nanti akan berisi data hasil scraping
    dataset = pd.DataFrame(columns=['SKU', 'Harga', 'Jumlah_Penjualan', 'Halaman'])
    #Setting webdriver versi chrome
    s = Service('/home/alfian/Downloads/chromedriver_2/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(5)
    #Fungsi looping untuk mengekstrak informasi yang dibutuhkan dari setiap halaman
    for pg in range(first_page,last_page): #Halaman yang mau di scrape
        page_num = str(pg)
        shopee_url = 'https://shopee.co.id/search?keyword={}&page='.format(brand)+page_num
        driver.get(shopee_url)
    
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        #Informasi-informasi yang dibutuhkan
        nama = driver.find_elements(By.XPATH, '//div[@class="_10Wbs- _5SSWfi UjjMrh"]')
        harga = driver.find_elements(By.XPATH, '//span[@class="_1d9_77"]')
        penjualan = driver.find_elements(By.XPATH, '//div[@class="_2VIlt8"]')
        
        time.sleep(10)

        #Membuat list data nama, harga dan penjumlahan untuk menampung data hasil scraping
        nama_list = []
        for p in range(len(nama)):
            try : nama_list.append(nama[p].text)
            except : nama_list.append("0")

        harga_list = []
        for x in range(len(harga)):
            try : harga_list.append(harga[x].text.replace('.', ''))
            except : harga_list.append("0")

        penjualan_list = []
        for z in range(len(penjualan)):
            try : penjualan_list.append(penjualan[z].text.split()[0].replace('RB','000').replace(',',''))
            except : penjualan_list.append("0")

        #menyusun semua list yang sudah didapat menjadi dataset 
        data_tuples = list(zip(nama_list[1:], harga_list[1:], penjualan_list[1:]))
        temp_data = pd.DataFrame(data_tuples, columns=['SKU', 'Harga', 'Jumlah_Penjualan'])
        temp_data['Halaman'] = pg+1
        dataset = dataset.append(temp_data)
    driver.close()
    return (dataset)

#Memanggil fingsi scrap
konichiwa = scrap("konichiwa", 0, 2)
# rockbros = scrap("rockbros", 0, 1)
# matoa = scrap("matoa", 0, 5)

#Menjadikan dalam satu dataframe
dataframe = [konichiwa, rockbros, matoa]
dataset = pd.concat(dataframe)

df = pd.DataFrame(dataset)

#merubah tipe data harga dan jumlah penjualan menjadi integer
df['Harga'] = df['Harga'].astype('int')
df['Jumlah_Penjualan'] = df['Jumlah_Penjualan'].astype('int')

#Estimasi GMV (harga * jumlah penjualan)
df['GMV'] = df['Harga'] * df['Jumlah_Penjualan']

print(df.head())