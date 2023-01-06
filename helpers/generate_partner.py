#!/bin/python3
import yaml
from datetime import datetime

partner_list = [
{"short_name":"TEI","name":"ERICSSON TELECOMUNICAZIONI SPA"},
{"short_name":"TIM","name":"TELECOM ITALIA SPA"},
{"short_name":"ORO","name":"ORANGE ROMANIA SA"},
{"short_name":"NXW","name":"NEXTWORKS"},
{"short_name":"WINGS","name":"WINGS ICT SOLUTIONS INFORMATION & COMMUNICATION TECHNOLOGIES IKE"},
{"short_name":"UC3M","name":"UNIVERSIDAD CARLOS III DE MADRID"},
{"short_name":"IMEC","name":"INTERUNIVERSITAIR MICRO-ELECTRONICA CENTRUM"},
{"short_name":"YBVR","name":"YERBA BUENA VR EUROPE SL"},
{"short_name":"CNIT","name":"CONSORZIO NAZIONALE INTERUNIVERSITARIO PER LE TELECOMUNICAZIONI"},
{"short_name":"TID","name":"TELEFONICA INVESTIGACION Y DESARROLLO SA"},
{"short_name":"ERC","name":"ERICSSON ESPANA SA"},
{"short_name":"IIT","name":"FONDAZIONE ISTITUTO ITALIANO DI TECNOLOGIA"},
{"short_name":"AIA","name":"ATHENS INTERNATIONAL AIRPORT S.A"},
{"short_name":"SSSA","name":"SCUOLA SUPERIORE DI STUDI UNIVERSITARI E DI PERFEZIONAMENTO S ANNA"},
{"short_name":"PIIU","name":"PROMOZIONE PER L INNOVAZIONE FRA INDUSTRIA E UNIVERS ASSOCIAZIONE"},
{"short_name":"COTO","name":"COMUNE DI TORINO"},
{"short_name":"TUIASI","name":"UNIVERSITATEA TEHNICA GHEORGHE ASACHI DIN IASI"},
{"short_name":"PROS","name":"PROSEGUR COMPANIA DE SEGURIDAD SA"},
{"short_name":"CROSSM","name":"CROSSMEDIA BELGIQUE"},
{"short_name":"DAEM","name":"DIMOS ATHINAION EPICHEIRISI MICHANOGRAFISIS"},
{"short_name":"CNR","name":"CONSIGLIO NAZIONALE DELLE RICERCHE"},
{"short_name":"FTGM","name":"FONDAZIONE TOSCANA GABRIELE MONASTERIO PER LA RICERCA MEDICA E DI SANITA PUBBLICA"},
{"short_name":"RW","name":"REAL WIRELESS LIMITED"},
]


for i in range(len(partner_list)):
    uc_data = {}
    uc_data["Title"]=f"{partner_list[i]['short_name']}"
    uc_data["excerpt"]=f"{partner_list[i]['name']}"
    uc_data["header"]={"teaser":"https://via.placeholder.com/200x200.png"}
    uc_data["sidebar"]=[{"title": "Role","image": "https://via.placeholder.com/350x250.png","image_alt": "logo","text": "TBC"}]
    uc_data["order"]=i
    now = datetime.now()
    uc_data["date"]= now.strftime('%y-%m-%d %H:%M:%S.%f')
    with open(f"../_consortium/{partner_list[i]['short_name']}.md", 'w') as yaml_file:
        yaml_file.write("---\n")
        yaml.dump(uc_data, yaml_file)
        yaml_file.write("---")