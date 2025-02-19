import requests
import matplotlib.pyplot as plt


whitebox = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=484&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=%&charttitel=Performance_von_Whitebox_seit_Mai_2016&dateformat=m.Y&chartart=linie").json()
quirion = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=193&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_quirion_seit_Mai_2015&dateformat=m.Y&chartart=linie&steps=10&minwert=-12&maxwert=45").json()
bevestor = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=4195&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_bevestor_seit_Mai_2018&dateformat=m.Y&chartart=linie&steps=1").json()
estably = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=4487&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Estably_seit_Mai_2020&dateformat=m.Y&chartart=linie").json()
solidvest = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=2585&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Solidvest_seit_Mai_2018&dateformat=m.Y&chartart=linie&minwert=-2&maxwert=29&steps=2").json()
growney = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=2184&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_growney_seit_Mai_2017&dateformat=m.Y&chartart=linie").json()
cominvest = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=2573&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_cominvest_seit_Mai_2018&dateformat=m.Y&chartart=linie&minwert=-15&maxwert=20&steps=1").json()
oskar = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=5923&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Oskar_seit_Mai_2021&dateformat=m.Y&chartart=linie&minwert=-8&maxwert=18&steps=1").json()
smavesto = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=6048&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Smavesto_seit_Mai_2022&dateformat=m.Y&chartart=linie&steps=2").json()
Scalable_Capital = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=6969&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Scalable_Capital_seit_Mai_2024&dateformat=m.Y&chartart=linie&minwert=-5&maxwert=12&steps=1").json()
fidelity = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=4488&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Fidelity_Wealth_Expert_seit_Mai_2020&dateformat=m.Y&chartart=linie").json()
visual_vest = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=2192&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_VisualVest_seit_Mai_2017&dateformat=m.Y&chartart=linie&minwert=-6&maxwert=38&steps=1").json()
WeltSparen = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=2589&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=%&charttitel=Performance_von_WeltSparen_seit_Mai_2018&dateformat=m.Y&chartart=linie").json()
vividam = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=4505&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_vividam_seit_November_2019&dateformat=m.Y&chartart=linie").json()
Gerd_Kommer_Capital = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=5916&apikey=4c4f68fd96f16cec&width=100%&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Gerd%20Kommer%20Capital_seit_Mai_2021&dateformat=m.Y&chartart=linie&steps=1").json()
zeedin = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=5937&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Zeedin_seit_Mai_2021&dateformat=m.Y&chartart=linie&minwert=-6&maxwert=8&steps=1").json()
digital_invest = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=3659&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Digital_Invest_Assets_seit_Mai_2019&dateformat=m.Y&chartart=linie").json()
minveo = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=4495&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Minveo_seit_Mai_2020&dateformat=m.Y&chartart=linie&steps=1").json()
peningar = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=4498&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_peningar_seit_Mai_2020&dateformat=m.Y&chartart=linie").json()
warburg = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=3657&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Warburg_Navigator_seit_Mai_2019&dateformat=m.Y&chartart=linie").json()
inno_invest = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=6764&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_Inno_Invest_seit_Mai_2023&dateformat=m.Y&chartart=linie").json()
icm = requests.get("https://diagramme.finanzrechner.org/nuapis/request?id=6762&apikey=4c4f68fd96f16cec&width=655&height=250&displayrangeselector=true&displayannotations=true&suffix=&charttitel=Performance_von_ICMsuite_seit_Juni_2023&dateformat=m.Y&chartart=linie").json()

items = {
    "whitebox": whitebox,
    "quirion": quirion,
    "bevestor": bevestor,
    "estably": estably,
    "solidvest": solidvest,
    "growney": growney,
    "cominvest": cominvest,
    "oskar": oskar,
    "smavesto": smavesto,
    "Scalable_Capital": Scalable_Capital,
    "fidelity": fidelity,
    "visual_vest": visual_vest,
    "WeltSparen": WeltSparen,
    "vividam": vividam,
    "Gerd_Kommer_Capital": Gerd_Kommer_Capital,
    "zeedin": zeedin,
    "digital_invest": digital_invest,
    "minveo": minveo,
    "peningar": peningar,
    "warburg": warburg,
    "inno_invest": inno_invest,
    "icm": icm,
}

for j, i in items.items():
    labels = i['data']['labels']
    performance_data = i['data']['datasets'][0]['data']
    title = i['data']['parameters']['title']
    label = i['data']['parameters']['label']


    plt.figure(figsize=(12, 6))
    plt.plot(labels, performance_data, label='Performance', color='#2f5e37', marker='o')

    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Percent')

    plt.xticks(labels[::4], rotation=45, ha='right', fontsize=10)
    plt.grid(True)
    plt.legend()

    plt.figtext(0.99, 0.01, label, horizontalalignment='right', verticalalignment='bottom', fontsize=8, color='gray')

    plt.subplots_adjust(bottom=0.2)

    plt.tight_layout()
    plt.savefig(f'{j}.png', bbox_inches='tight')
    # plt.show()

