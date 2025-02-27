---
permalink: /uc-gallery/
layout: single
collection: usecases
news: posts
entries_layout: grid
title: Project's Use Cases
filter: wp5
toc: true
classes:
  - landing
  - dark-theme
  - wide-post

---

TrialsNet will design and implement 13 representative use cases as forerunners for the transition towards 6G covering the three relevant domains of i) Infrastructure, Transportation, Security & Safety, ii) eHealth & Emergency, and iii) Culture, Tourism & Entertainment
{: .text-justify}


### Infrastructure, Transportation, and Security & Safety  

Infrastructure, Transportation, and Security & Safety (ITSS) represent one of the key domains of the urban ecosystems in Europe. ITSS use cases target improving the “liveability” of the urban environment by decreasing the negative effects (congestion, sprawl, pollution, inequality, etc.) of collapsing metropolises, as it is of utmost importance to ensure that cities are safe, affordable, and sustainable for all.
{: .text-justify}


{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp3' %}
</div>

### eHealth & Emergency  

eHealth is certainly one of the most promising fields in which new technologies will play a fundamental role. In particular, SNS and future network technologies can benefit (i) telemedicine, allowing to transmit data about a patient’s health to healthcare professionals in real time, even in mobility situations, permitting pre-hospital identification of the correct diagnosis, (ii) remote monitoring, allowing even in areas not equipped with departments for certain medical specializations, to be assisted by the specialized medical doctors, especially in the surgical field, (iii) control of prostheses, allowing to connect a prosthetic device control system with AI technologies for reducing the need for explicit control by the user and thus their cognitive load for driving it, and making the movements of the wearer more natural, and (iv) emergency, allowing flexibility to address different dynamic plans and guidelines over standard predefined Emergency Action Plans.
{: .text-justify}

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp4' %}
</div>

### Culture, Tourism & Entertainment  

Trials in this domain will be based on various 6G candidate technologies such as robots, metaverse, advanced sensors and cameras, focusing on the Culture, Tourism and Entertainment aspects.
{: .text-justify}

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp5' %}
</div>
