const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
	entry: [
		'jquery',
		'./src/js/index.js'
	],
	mode: 'development',
	output: {
		//filename: '[name].[contenthash].js', #for dev
		filename: '[name].js',
		path : __dirname + '/app/static/js'
	},
	optimization: {
		splitChunks: {
			chunks: 'all',
			name: 'vendors',
		},
	},

	module: {
		rules: [
			{
				test: /\.(scss)$/,
				use: [
					MiniCssExtractPlugin.loader,
					'css-loader',
					'sass-loader'
				]
			}
		]
	},
	plugins: [
		new MiniCssExtractPlugin({
			filename: '../css/index.css',
			chunkFilename: "../css/[name].css"
		}),
		new webpack.ProvidePlugin({
		    $: 'jquery',
		    jQuery: 'jquery',
		    "window.jQuery": 'jquery'
		})
	]
}