let mix = require('laravel-mix');

mix
  .setPublicPath('dingen_pyramid/static')
  .setResourceRoot('/static/')
  .sass('dingen_pyramid/resources/sass/app.scss', 'css')
  //.js('dingen_pyramid/resources/app.js', 'js')
