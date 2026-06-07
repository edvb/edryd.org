---
title: {{title}}
layout: gallery
---

<!-- Cover photo -->
<section id="cover" style="background: url('/{{cover}}') center/cover;">
  <a href="https://edryd.org" class="top-link">edryd</a>

  <div class="cover-content">
    <div>
      <h1>{{title}}</h1>
      <time>{{date}}</time>
    </div>
    <a href="#gallery" class="scroll-button">See Gallery</a>
  </div>
</section>

<!-- Gallery of photos -->
<section id="gallery">
  {{#images}}
    <a href="/{{ . }}" data-lightbox="gallery">
        <img src="/{{ . }}" alt="image"/>
    </a>
  {{/images}}
</section>
