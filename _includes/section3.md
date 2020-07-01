<section id="language-values" class="{{ include.color }}">
  <div class="w-100 mw-none ph3 mw8-m mw9-l center f3">
    <header class="pb0 cornered">
      <h2>
	{{ include.title }}
      </h2>
    </header>
    {% if include.description %}
    <div class="description">
      <p class="lh-copy f2">
        {{ include.description }}
      </p>
    </div>
    {% endif %}

    <div class="flex-none flex-l">
      <section class="w-100 pv2 pv0-l mt4">
	{% if include.left-title %}
	<h3 class="f2 f1-l">{{ include.left-title }}</h3>
	{% endif %}
        <p class="f3 lh-copy">
	  {{ include.left-content }}
        </p>
      </section>
      <section class="w-100 pv2 pv0-l mt4 mh5-l">
        {% if include.middle-title %}
	<h3 class="f2 f1-l">{{ include.middle-title }}</h3>
	{% endif %}
        <p class="f3 lh-copy">
	  {{ include.middle-content }}
        </p>

      </section>
      <section class="w-100 pv2 pv0-l mt4">
        {% if include.right-title %}
	<h3 class="f2 f1-l">{{ include.right-title }}</h3>
	{% endif %}
        <p class="f3 lh-copy">
	  {{ include.right-content }}
        </p>
      </section>
    </div>
  </div>
</section>
