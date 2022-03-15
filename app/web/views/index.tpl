% include('header.tpl', tags=tags)

<div id="content" class="mui-container-fluid">

	<div class="mui-row">
		<div class="mui-col-sm-10 mui-col-sm-offset-1">

			<div class="mui--text-dark-secondary mui--text-body2">
				<h1>
					DAILY PYTHON TIPS ({{ len(tweets) }})
					% if filter:
						<small>&nbsp;(<a href="/">show all</a>)</small>
					% end
				</h1>
			</div>
			<div class="mui-divider"></div>
			% for tweet in tweets:
				<div class='tweet'>
					<pre>{{ !tweet.text }}</pre>
					<div class="mui--text-dark-secondary"><strong>{{ tweet.likes }}</strong> Likes / <strong>{{ tweet.retweets }}</strong> RTs / {{ tweet.created }} / <a href="https://twitter.com/wwt_inc/status/{{ tweet.tweetid }}" target="_blank">Share</a></div>
				</div>
			% end

		</div>
	</div>

</div>

% include('footer.tpl')