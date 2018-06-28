const VueLoaderPlugin = require('vue-loader/lib/plugin')
let mix = require('laravel-mix');

mix
	.setPublicPath('dingen_pyramid/static')
	.setResourceRoot('/static/')
	.ts('dingen_pyramid/resources/ts/app.ts', 'js')
	.sass('dingen_pyramid/resources/sass/app.scss', 'css')
	.webpackConfig({
		plugins: [
			new VueLoaderPlugin()
		],
	})
	.version()
