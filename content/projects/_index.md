---
title: projects
---

{{< projects.inline >}}
  <div class="container">
    <!-- TODO combine code and scripts, loop over all projects -->
    {{ range $.Site.Data.projects.code }}
      <div class="row text-inc">
        {{ $link := or .link (path.Join "projects/" .name | relURL) }}
        <div class="col-lg-4 text-lg-right"><a href="{{ $link }}">{{ .name }}</a></div>
        <div class="col-lg-6"><a href="{{ $link }}" class="italic-off text-primary">{{ .desc }}</a></div>
      </div>
    {{ end }}
    <h2 class="heading pt-4">SCRIPTS</h2>
    {{ range $.Site.Data.projects.scripts }}
      {{ $gist := getJSON "https://api.github.com/gists/" .id }}
      {{ $link := path.Join "projects/" .name | relURL }}
      <div class="row text-inc">
        <div class="col-lg-4 text-lg-right"><a href="{{ $link }}">{{ .name }}</a></div>
        <div class="col-lg-6"><a href="{{ $link }}" class="italic-off text-primary">{{ $gist.description }}</a></div>
      </div>
    {{ end }}
  </div>
{{< /projects.inline >}}
