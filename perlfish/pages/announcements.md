---
layout: default
title: "Blog"
permalink: /announcements
---

{% include header.html 
   title="News" 
%}

<section id="posts" class="green">
   <div class="w-100 mw-none ph3 mw8-m mw9-l center f3">

    <table class="post-list collapse w-100 f2-l f2-m f3-s">

      {% for post in site.posts %}
      <tr>
	<td class="bn">{{ post.date | date: '%Y-%m-%d' }}</td>
	{% if post.description %}
        <td class="bn"><a href="{{site.url}}{{post.url}}">{{post.description}}</a></td>
	{% else %}
        <td class="bn"><a href="{{site.url}}{{post.url}}">{{post.title}}</a></td>
	{% endif %}
      </tr>
      {% endfor %}

    </table>

  </div>
</section>
