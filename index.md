---
layout: single
title: Course Overview
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
author_info: true
---

# Information for CSE 431

**CSE 431: Algorithm Engineering**

Below are the documents and links needed for Fall 2021.

**[Syllabus](https://nahumj.github.io/CSE-431/syllabus)** - provides basic information about the course including how you will be graded.

**[Piazza](https://piazza.com/class/kst3t6l9dxi6t0)** a place for asynchronous discussions and Q&A sessions.

Below are the week-by-week topics that will be covered.  Links will be added at least 24 hours before the first class each week (and often sooner).  The current week will be in bold in the directory on the left of this page.


# Due dates

- Weekly Lecture Review, every Friday at 10pm
- Homework: Certain Thursdays at 10pm
- Exams: Individualy scheduled during the week of 2021-10-25 and the week of 2021-12-13.

# Help Room
- Offered from 5pm-7pm on Mondays, Tuesdays, Wednesdays, and Thursdays in [https://msu.zoom.us/j/91416543573](https://msu.zoom.us/j/91416543573).



# Current course content

{% for post in site.weeks %}

  {% assign this_week = "now" | date: "%W" | minus: 1 %}
  {% assign last_week = "now" | date: "%W" | minus: 2 %}
  {% assign next_week = "now" | date: "%W" | plus: 0 %}

  {% assign postWeek = post.date | date: "%W" | minus: 0 %}

  {% if postWeek == last_week %}
   <h2>Last week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}

  {% if postWeek == this_week %}
   <h2>This week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}

 {% if postWeek == next_week %}
   <h2>Next week: <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
  {% endif %}


{% endfor %}
