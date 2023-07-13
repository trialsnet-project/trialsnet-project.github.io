---
permalink: /uc-gallery/
layout: single
collection: usecases
news: posts
entries_layout: grid
title: TrialsNet Use Cases
filter: wp5
toc: true
classes:
  - landing
  - dark-theme
  - wide-post

---

13 Use Cases have been designed and will be implemented in TrialsNet as forerunners for the 6G activities. The Use Cases address three main domains\: Infrastructure, Transportation and Security \& Safety (ITSS), eHealth \& Emergency, and Culture, Tourism \& Entertainment.
{: .text-justify}


### Infrastructure, Transportation and Security \& Safety  

Infrastructure, Transportation and Security \& Safety (ITSS) represent key domains of the urban ecosystems in Europe. ITSS Use Cases (UCs) target improving the “liveability” of the urban environment in the ITSS domain, by decreasing the negative effects (congestion, sprawl, pollution, inequality, etc.) of collapsing metropolises, as it is of utmost importance to ensure that cities are safe, affordable, and sustainable for all. Also, the UCs will have positive impacts on Societal Values such as Trust, Resilience, Security, Sustainability, Trustworthiness, Automation, and Service Availability. In this context, five different UCs have been designed, as described in the following.
{: .text-justify}


{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp3' %}
</div>

### eHealth \& Emergency  

eHealth is certainly one of the most promising fields in which new technologies will play a fundamental role. In particular, SNS and future network technologies can benefit telemedicine, remote monitoring, control of prostheses, and emergency management. In this context, four different UCs have been designed, as described in the following.
{: .text-justify}

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp4' %}
</div>

### Culture, Tourism \& Entertainment  

Trials in this domain will be based on various technologies such as robots, metaverse, sensors, and cameras, covering the relevant domain of the urban ecosystems in Europe, focusing on the Culture, Tourism, and Entertainment aspects. In this context, the following four UCs have been designed.
{: .text-justify}

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp5' %}
</div>
