<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//cdn.muicss.com/mui-0.9.28/css/mui.min.css" rel="stylesheet" type="text/css" />
    <link href="static/css/style.css" rel="stylesheet" type="text/css" />
    <script src="//cdn.muicss.com/mui-0.9.28/js/mui.min.js"></script>
    <title>Daily Python Tip</title>
  </head>
  <body>

  <div id="sidebar">

    <div class="mui--text-light mui--text-display1 mui--align-vertical">
      <a href="https://twitter.com/wwt_inc" target="_blank">
        <img class="logo" src='https://pbs.twimg.com/profile_images/1356688746939363332/B9cUoIhf_400x400.jpg' alt='PyBites'>
      </a>
    </div>

	<form action="/" method="GET" class="mui-form">
		<div class="mui-textfield">
    % if filter:
			<input type="text" name="hashtag" placeholder="Hashtag Search" value="{{ filter }}">
    % else:
      <input type="text" name="hashtag" placeholder="Hashtag Search" value="">
    % end
		</div>
	</form>

	% for hashtag in hashtags:
	  <a style="font-size: {{ hashtag.count/10 + 1 }}em;" href="/{{ hashtag.name }}">#{{ hashtag.name }}</a>&nbsp;&nbsp;
	% end
	<br>
	<br>
	<a href="https://wwt.com" target="_blank">
		<button class="mui-btn mui-btn--primary">WWT Digital Platform</button>
	</a>
	<div class="mui-dropdown">
	<button class="mui-btn mui-btn--primary" data-mui-toggle="dropdown">
		About
		<span class="mui-caret"></span>
	</button>
	<ul class="mui-dropdown__menu">
		<li><a href="https://twitter.com/wwt_inc" target="_blank">World Wide Technology on Twitter</a></li>
		<li><a href="https://wwt.com/atc" target="_blank">World Wide Technology Advanced Technology Center</a></li>
		<li><a href="https://github.com/timothyhull/ww_tweeter" target="_blank">Star / fork the Github repo</a></li>
	</ul>
	</div>

  </div>