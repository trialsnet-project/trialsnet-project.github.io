---
permalink: /uc-gallery/
layout: single
collection: usecases
news: posts
entries_layout: grid
title: UC Gallery
filter: wp5
toc: true
classes:
  - landing
  - dark-theme
  - wide-post

---

TBC
{: .text-justify}


### Infrastructure 

TBC
{: .text-justify}


{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp3' %}
</div>

### eHealth 

TBC
{: .text-justify}

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp4' %}
</div>

### Entertainment 

TBC
{: .text-justify}

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}-ucrow">
  {% include documents-uc-collection.html collection=page.collection sort_by=page.sort_by sort_order=page.sort_order type=entries_layout filter='wp5' %}
</div>