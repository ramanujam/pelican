Date: 2012-10-01
Title: Static blog using pelican and github pages

Over the last six years, i have blogged in many different places both for fun and profit. It helped me meet many interesting folks through blog meets and various conferences and in the journey i also made some great friends. In the recent times, i completely stopped writing and publishing my thoughts. Thanks to twitter, there was always a place to express one's thoughts in a short and fast manner. Even though i had a couple of dormant blogs, i didn't feel like publishing there when i wanted to. Hopefully, this new setup will change that. After spending some time and exploring a few different options, i decided to go with [Pelican](http://pelican.notmyidea.org/).

I knew i wanted a static blog and also one than ran on python rather than ruby. So, that eliminated the more popular static blog generators like Jekyll, Octopress framework and many more. There are a few other python based static blog generators that work well out of the box and are more popular than Pelican but i liked the configurability of Pelican and the ease of writing a custom theme using Jinja templates.

These were the basic requirements that i had

- Write posts in Markdown
- Easy templating and theming
- Basic command line tools
- Setup the blog as a local git repository and push to github
- Easy publishing to S3, Github or Heroku

I created two git repositories, one to hold all the scripts and setup files from Pelican and the other to hold the static content. Currently i am publishing the static blog to the free and wonderful Github Pages. If you create a username.github.com repo in your account, github will automatically generate and publish the content in the master branch. I used [Fabric](http://docs.fabfile.org/en/1.4.3/index.html) to completely automate this process. Whenever, i write a new post or make changes to the theme, all i have to do is type in 'fab publish' and it does a few sequential steps and pushes the master branch to origin.

I used the templates from the base theme and made a custom theme. Thanks to media queries, the site is now responsive and is readable on tablets and touch phones. I still have to make some more tweaks and refinements in that department though. The thing i like about this setup is it wouldn't be very hard to switch over to a different static blog generator in the future if i want to. Eventhough it took a good amount of time to get the blog up and running, it was definitely a satisfying experience. 

References 

1. [Pelican docs](http://pelican.notmyidea.org/en/3.0/index.html#documentation) 
2. [A good intro to publishing with pelican](http://martinbrochhaus.com/2012/02/pelican.html)
3. [Github pages](https://help.github.com/categories/20/articles)
