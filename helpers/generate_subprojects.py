import yaml
from datetime import datetime
import pandas as pd

subp_list = [ 
"Connected Rails: Evaluating 5G for Autonomous Tram Operations",
"5G-enabled Secure Surveillance System (5GS3)",
"SkyLink Vision",
"CITY4ALL",
"AI/ML-based Preventive and Reactive Emergency handling  (AI-PREMSET-MCX)",
"MILESTONE - A REAL-TIME AI-ENABLED WORKER SAFETY PRESERVATION SYSTEM",
"Automated Tele-Operated Sustainable (ATOS) driving",
"Intelligent control of interconnected manufacturing infrastructures (i-CNC)",
"AdaptoFlow",
"AI4RTC: AI applications for Real-time Charging Load Management",
"Cities Without Barriers",
"COMO5: COntinuous MOnitoring of patients with chronic disease via 5G",
"METACLINIC",
"MediVision-5G (eHealth)",
"Remote Coordination and Interworking of First Responders in Emergency Situations",
"5GVIREH: Virtual Reality Enhanced Rehabilitation",
"Beyond 5G Football Stadium",
"Turin5Games",
"Torino 4U: 10 things to see around you",
"6GVision: Improvement of the 5GOpen testbed at imec with vision-aided mmW gNB",
"DREAMPARK",
"5G AUGMENTED REALITY TOUR FOR THE UNESCO SITE “HISTORICAL CENTER OF NAPLES”",
"“Remember Ascari”: MR in MAUTO – Immersive MR Experience in F1 (MAUTO)",
"Mobile Augmented Reality for Outdoor PoI Enrichment",
]


df = pd.read_csv('../supbweb.csv')

abstracts = df['Abstract'].values
topics = df['Topic'].values
countries = df['Country'].values
companies = df['Company Name'].values

for i in range(len(subp_list)):
    uc_data = {}
    uc_data["title"]=f"{subp_list[i]}"
    uc_data["excerpt"]=f"{subp_list[i]}"
    uc_data["header"]={"teaser":"https://via.placeholder.com/200x200.png"}
    uc_data["sidebar"]=[{"title": "Factsheet","image": "https://via.placeholder.com/350x250.png","image_alt": "logo","text": f"Lead Company Name: {companies[i]} Country: {countries[i]} Topic: {topics[i]}"}]
    uc_data["order"]=i
    now = datetime.now()
    uc_data["date"]= now.strftime('%y-%m-%d %H:%M:%S.%f')
    with open(f"../_subprojects/Sub-Project-{i+1}.md", 'w') as yaml_file:
        yaml_file.write("---\n")
        yaml.dump(uc_data, yaml_file)
        yaml_file.write("---\n")
        yaml_file.write(abstracts[i])
        yaml_file.write("\n")
        yaml_file.write("{: .text-justify}\n")
        yaml_file.write("\n")