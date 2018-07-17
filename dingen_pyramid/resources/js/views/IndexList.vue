<template>
<div class="columns">

  <div class="column is-hidden-mobile">
      <div class="box is-hidden-mobile" v-for="n in 15">
        <div class="media">
          <div class="media-content">
            <div class="content">
              <h3 class="title is-4">
                <a class="has-text-primary" href="/es-ar/blog/show/5/">
                  ipsum consectetur ipsam nulla aliquid!!!!
                </a>
              </h3>
              <small>junio 15, 2017</small>
              <p>adipisicing magnam harum veritatis quod necessitatibus. officiis accusamus magni voluptates pariatur dicta! voluptates officiis omnis velit delectus necessitatibus. libero eum ...</p>
            </div>
            <div class="level is-mobile">
              <div class="level-left">

                <a class="level-item" href="/es-ar/blog/tag/1/tag1/">
                  #tag1
                </a>

                <a class="level-item" href="/es-ar/blog/tag/2/tag2/">
                  #tag2
                </a>

                <a class="level-item" href="/es-ar/blog/tag/4/tag4/">
                  #tag4
                </a>

              </div>
              <div class="level-right">
                <a class="level-item button is-small" href="#">
                  <span class="icon is-small">
                    <i class="fa fa-facebook"></i>
                  </span>
                </a>
                <a class="level-item button is-small" href="#">
                  <span class="icon is-small">
                    <i class="fa fa-twitter"></i>
                  </span>
                </a>
                <a class="level-item button is-small" href="#">
                  <span class="icon is-small">
                    <i class="fa fa-google-plus"></i>
                  </span>
                </a>
              </div>
            </div>
          </div>
          <figure class="media-right image is-128x128">
            <img src="https://lorempixel.com/128/128/">
          </figure>
        </div>
      </div>
  </div>

  <div class="column is-hidden-tablet">
      <div class="card" v-for="n in 10">
        <div class="card-image">
          <figure class="image is-2by1">
            <img src="http://bulma.io/images/placeholders/1280x960.png" alt="Image">
          </figure>
        </div>
        <div class="card-content">
          <div class="content">
            <h5 class="title is-5">
              <a class="has-text-primary" href="/es-ar/blog/show/5/">
                Ipsum consectetur ipsam nulla aliquid!!!!
              </a>
            </h5>
            <small>Junio 15, 2017</small>
            <p>
            Adipisicing magnam harum veritatis quod necessitatibus. Officiis accusamus magni voluptates pariatur dicta! Voluptates officiis omnis vel...
            </p>

            <a href="/es-ar/blog/tag/1/tag1/">#tag1</a>

            <a href="/es-ar/blog/tag/2/tag2/">#tag2</a>

            <a href="/es-ar/blog/tag/4/tag4/">#tag4</a>

            <br>
          </div>
        </div>
        <footer class="card-footer">
          <span class="card-footer-item">
            <a class="button is-small">
              <span class="icon is-small">
                <i class="fa fa-facebook"></i>
              </span>
            </a>
          </span>
          <span class="card-footer-item">
            <a class="button is-small">
              <span class="icon is-small">
                <i class="fa fa-twitter"></i>
              </span>
            </a>
          </span>
          <span class="card-footer-item">
            <a class="button is-small">
              <span class="icon is-small">
                <i class="fa fa-google-plus"></i>
              </span>
            </a>
          </span>
        </footer>
      </div>
  </div>
</div>
</template>
