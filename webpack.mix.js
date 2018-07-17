const VueLoaderPlugin = require('vue-loader/lib/plugin')
let mix = require('laravel-mix');

mix
  .setPublicPath('dingen_pyramid/static')
  .setResourceRoot('/static/')
  .copyDirectory('dingen_pyramid/resources/images', 'dingen_pyramid/static/images')
  .js('dingen_pyramid/resources/js/app.js', 'js')
  .sass('dingen_pyramid/resources/sass/app.scss', 'css')
	.webpackConfig({
		plugins: [
			new VueLoaderPlugin()
		]
	})
  .version()
