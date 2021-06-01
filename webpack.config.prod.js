const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
	entry: [
		'jquery',
		'./src/js/index.js'
	],
	mode: 'production',
	output: {
		filename: '[name]-prod.[contenthash].js', //for dev
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
		}),
		new webpack.ProvidePlugin({
		    $: 'jquery',
		    jQuery: 'jquery',
		    "window.jQuery": 'jquery'
		})
	]
}