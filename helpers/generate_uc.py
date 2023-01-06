#!/bin/python3
import yaml
from datetime import datetime

uc_list = [ "Smart Crowd Monitoring",
"Proactive Public Infrastructure Assets Management",
"Autonomous APRON",
"Smart Traffic Management",
"Control Room in Metaverse",
"MCI and Emergency Rescue in Populated Area",
"Remote Proctoring",
"Smart Ambulance",
"Adaptive Control of Hannes Prosthetic Device",
 "Immersive Fan Engagement",
 "Service Robots for Enhanced Passengers' Experience",
 "City Parks in Metaverse",
 "Extended XR Museums Experience"]


for i in range(len(uc_list)):
    uc_data = {}
    uc_data["title"]=f"Use Case {i+1}"
    uc_data["excerpt"]=f"{uc_list[i]}"
    uc_data["header"]={"teaser":"https://via.placeholder.com/200x200.png"}
    uc_data["sidebar"]=[{"title": "Objective","image": "https://via.placeholder.com/350x250.png","image_alt": "logo","text": "Here we discuss the Objective of the UC"}]
    uc_data["order"]=i
    now = datetime.now()
    uc_data["date"]= now.strftime('%y-%m-%d %H:%M:%S.%f')
    with open(f"../_usecases/UC{i+1}.md", 'w') as yaml_file:
        yaml_file.write("---\n")
        yaml.dump(uc_data, yaml_file)
        yaml_file.write("---")