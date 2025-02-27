---
permalink: /subprojects-gallery/
layout: single
collection: subprojects
news: posts
entries_layout: grid
title: Open Call's Use Cases
filter: wp5
toc: true
classes:
  - landing
  - dark-theme
  - wide-post

---

The TrialsNet [Open Call](/open-call/) selected 24 additional Use Cases related to the project topics. 
{: .text-justify}  


### Infrastructure, Transportation, and Security & Safety  


{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp3' %}
</div>

### eHealth & Emergency  


{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp4' %}
</div>

### Culture, Tourism & Entertainment  


{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp5' %}
</div>