neighbors = {
    'adana':['Hatay', 'Osmaniye', 'Kahramanmaras', 'Kayseri', 'Nigde', 'Mersin'],
    'adiyaman':['Sanliurfa', 'Diyarbakir', 'Malatya', 'Kahramanmaras', 'Gaziantep'],
    'afyonkarahisar':['Isparta', 'Konya', 'Eskisehir', 'Kutahya', 'Usak', 'Denizli', 'Burdur'],
    'agri':['Van', 'Igdir', 'Kars', 'Erzurum', 'Mus', 'Bitlis'],
    'amasya':['Yozgat', 'Tokat', 'Samsun', 'Corum'],
    'ankara':['Konya', 'Aksaray', 'Kirsehir', 'Kirikkale', 'Cankiri', 'Bolu', 'Eskisehir', 'afyonkarahisar'],
    'antalya':['Mersin', 'Karaman', 'Konya', 'Isparta', 'Burdur', 'Mugla'],
    'artvin':['Rize', 'Erzurum', 'Ardahan'],
    'aydin':['Mugla', 'Denizli', 'Manisa', 'Izmir'],
    'balikesir':['Izmir', 'Manisa', 'Kutahya', 'Bursa', 'Canakkale'],
    'bilecik':['Kutahya', 'Eskisehir', 'Bolu', 'Sakarya', 'Bursa'],
    'bingol':['Diyarbakir', 'Mus', 'Erzurum', 'Erzincan', 'Tunceli', 'Elazig'],
    'bitlis':['Siirt', 'Van', 'Agri', 'Mus', 'Batman'],
    'bolu':['Eskisehir', 'Ankara', 'Cankiri', 'Zonguldak', 'Duzce', 'Sakarya', 'Bilecik'],
    'burdur':['Mugla', 'Antalya', 'Isparta', 'afyonkarahisar', 'Denizli'],
    'bursa':['Balikesir', 'Kutahya', 'Bilecik', 'Sakarya', 'Kocaeli', 'Yalova'],
    'canakkale':['Balikesir', 'Tekirdag', 'Edirne'],
    'cankiri':['Ankara', 'Kirikkale', 'Corum', 'Kastamonu', 'Zonguldak', 'Bolu', 'Karabuk'],
    'corum':['Yozgat', 'Amasya', 'Samsun', 'Sinop', 'Kastamonu', 'Cankiri', 'Kirikkale'],
    'denizli':['Mugla', 'Burdur', 'afyonkarahisar', 'Usak', 'Manisa', 'Aydin'],
    'diyarbakir':['Sanliurfa', 'Mardin', 'Batman', 'Mus', 'Bingol', 'Elazig', 'Malatya', 'Adiyaman'],
    'edirne':['Canakkale', 'Tekirdag', 'Kirikkale'],
    'elazig':['Diyarbakir', 'Bingol', 'Tunceli', 'Erzincan', 'Malatya'],
    'erzincan':['Elazig', 'Tunceli', 'Bingol', 'Erzurum', 'Bayburt', 'Gumushane', 'Giresun', 'Sivas', 'Malatya'],
    'erzurum':['Bingol', 'Mus', 'Agri', 'Kars', 'Ardahan', 'Artvin', 'Rize', 'Trabzon', 'Bayburt', 'Erzincan'],
    'eskisehir':['afyonkarahisar', 'Konya', 'Ankara', 'Bolu', 'Bilecik', 'Kutahya'],
    'gaziantep':['Kilis', 'Sanliurfa', 'Adiyaman', 'Kahramanmaras', 'Osmaniye', 'Hatay'],
    'giresun':['Gumushane', 'Trabzon', 'Erzincan', 'Sivas', 'Ordu'],
    'gumushane':['Erzincan', 'Bayburt', 'Trabzon', 'Giresun'],
    'hakkari':['Van', 'Sirnak'],
    'hatay':['Kilis', 'Gaziantep', 'Osmaniye', 'Adana'],
    'isparta':['Antalya', 'Konya', 'afyonkarahisar', 'Burdur'],
    'mersin':['Adana', 'Nigde', 'Konya', 'Karaman', 'Antalya'],
    'istanbul':['Kocaeli', 'Tekirdag', 'Kirklareli'],
    'izmir':['Aydin', 'Manisa', 'Balikesir'],
    'kars':['Agri', 'Igdir', 'Ardahan', 'Erzurum'],
    'kastamonu':['Corum', 'Sinop', 'Cankiri', 'Bartin', 'Karabuk'],
    'kayseri':['Adana', 'Kahramanmaras', 'Sivas', 'Yozgat', 'Nevsehir', 'Nigde'],
    'kirklareli':['Edirne', 'Tekirdag', 'Istanbul'],
    'kirsehir':['Nevsehir', 'Yozgat', 'Kirikkale', 'Ankara', 'Aksaray'],
    'kocaeli':['Yalova', 'Istanbul', 'Bursa', 'Bilecik', 'Sakarya'],
    'konya':['Antalya', 'Karaman', 'Mersin', 'Nigde', 'Aksaray', 'Ankara', 'Eskisehir', 'afyonkarahisar', 'Isparta'],
    'kutahya':['Manisa', 'Usak', 'afyonkarahisar', 'Eskisehir', 'Bilecik', 'Bursa', 'Balikesir'],
    'malatya':['Kahramanmaras', 'Adiyaman', 'Diyarbakir', 'Elazig', 'Erzincan', 'Sivas'],
    'manisa':['Izmir', 'Aydin', 'Denizli', 'Usak', 'Kutahya', 'Balikesir'],
    'kahramanmaras':['Gaziantep', 'Adiyaman', 'Malatya', 'Sivas', 'Kayseri', 'Adana', 'Osmaniye'],
    'mardin':['Sanliurfa', 'Diyarbakir', 'Batman', 'Siirt', 'Sirnak'],
    'mugla':['Antalya', 'Burdur', 'Denizli', 'Aydin'],
    'mus':['Diyarbakir', 'Batman', 'Bitlis', 'Agri', 'Erzurum', 'Bingol'],
    'nevsehir':['Nigde', 'Kayseri', 'Yozgat', 'Kirsehir', 'Aksaray'],
    'nigde':['Nevsehir', 'Kayseri', 'Adana', 'Mersin', 'Konya', 'Aksaray'],
    'ordu':['giresun','tokat','sivas','samsun'],
    'rize':['Artvin', 'Erzurum', 'Bayburt', 'Trabzon'],
    'sakarya':['Duzce', 'Bolu', 'Bilecik', 'Bursa', 'Kocaeli'],
    'samsun':['Ordu', 'Tokat', 'Amasya', 'Corum', 'Sinop'],
    'siirt':['Van', 'Bitlis', 'Batman', 'Mardin', 'Sirnak'],
    'sinop':['Samsun', 'Corum', 'Kastamonu'],
    'sivas':['Kayseri', 'Kahramanmaras', 'Malatya', 'Erzincan', 'Giresun', 'Ordu', 'Tokat', 'Yozgat'],
    'tekirdag':['Istanbul', 'Kirklareli', 'Edirne', 'Canakkale'],
    'tokat':['Sivas', 'Ordu', 'Samsun', 'Amasya', 'Yozgat'],
    'trabzon':['Rize', 'Bayburt', 'Gumushane', 'Giresun'],
    'tunceli':['Elazig', 'Bingol', 'Erzincan'],
    'sanliurfa':['Gaziantep', 'Adiyaman', 'Diyarbakir', 'Mardin'],
    'usak':['Manisa', 'Denizli', 'afyonkarahisar', 'Kutahya'],
    'van':['Hakkari', 'Sirnak', 'Siirt', 'Bitlis', 'Agri'],
    'yozgat':['Kayseri', 'Sivas', 'Tokat', 'Amasya', 'Corum', 'Kirikkale', 'Kirsehir', 'Nevsehir'],
    'zonguldak':['Bartin', 'Cankiri', 'Bolu', 'Duzce', 'Karabuk'],
    'aksaray':['Nigde', 'Nevsehir', 'Kirsehir', 'Ankara', 'Konya'],
    'bayburt':['Erzincan', 'Erzurum', 'Rize', 'Trabzon', 'Gumushane'],
    'karaman':['Mersin', 'Konya', 'Antalya'],
    'kirikkale':['Kirsehir', 'Yozgat', 'Corum', 'Cankiri', 'Ankara'],
    'batman':['Mardin', 'Siirt', 'Bitlis', 'Mus', 'Diyarbakir'],
    'sirnak':['Mardin', 'Siirt', 'Van', 'Hakkari'],
    'bartin':['Kastamonu', 'Zonguldak', 'Karabuk'],
    'ardahan':['Kars', 'Erzurum', 'Artvin'],
    'igdir':['Agri', 'Kars'],
    'yalova':['Kocaeli', 'Bursa'],
    'karabuk':['Zonguldak', 'Bartin', 'Kastamonu', 'Cankiri'],
    'kilis':['Gaziantep', 'Hatay'],
    'osmaniye':['Gaziantep', 'Kahramanmaras', 'Adana', 'Hatay'],
    'duzce':['Zonguldak', 'Bolu', 'Sakarya'],
}
