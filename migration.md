Links like /learn are also accessible with /learn/ or /learn.html

## Improvements
* Sitemap /sitemap.xml (VERY important for SEO)
* RSS feed /feed.xml 
* SEO tags (structured data for Google, Open Graph for facebook, Twitter cards)
* More favicons 
* SEO Subfolders probably better than subdomains

## perl.org
### Migration
* https://perl.org/about.html -> /
* https://perl.org/learn.html -> /learn (merged with http://learn.perl.org)
* https://www.perl.org/community.html -> /community
* https://www.perl.org/cpan.html -> /cpan
* https://www.perl.org/books/library.html -> /books
* https://www.perl.org/get.html -> /get

When possible, link to external websites :
* Playground => https://perlbanjo.com/
* Foundation => https://www.perlfoundation.org/
* Version 5.32.0 => https://www.cpan.org/src/README.html

### Removal
* https://perl.org/ -> redundant (a menu actually)
* https://www.perl.org/docs.html -> redundant (link perldoc in menu)
* https://www.perl.org/media.html -> outdated (perlcast 2010, books amazon is just a "search perl" on amazon, slideshare is "tag perl on slideshare, $foo seems great but german, perl.com/perlsphere/perl iron man already mentionned)

## grants.perlfoundation.org
### Migration
* http://grants.perlfoundation.org/ => http://127.0.0.1:4000/grants-proposals

All other (a bit less community driven) grants pages are still https://www.perlfoundation.org/grants.html

## learn.perl.org
### Migration
* https://learn.perl.org/ -> /learn (merged with https://perl.org/learn.html)
* https://learn.perl.org/modules/ -> /learn/modules
* https://learn.perl.org/examples/ -> /learn/examples
* https://learn.perl.org/examples/email.html -> /learn/examples#email
* https://learn.perl.org/examples/email_valid.html -> /learn/examples#validate-email
* https://learn.perl.org/examples/directory_list.html -> /learn/examples#directory-list
* https://learn.perl.org/examples/read_write_file.html -> /learn/examples#read-write-file
* https://learn.perl.org/examples/spreadsheet_read.html -> /learn/examples#spreadsheet
* https://learn.perl.org/examples/configuration_files.html -> /learn/examples#configuration-files
* https://learn.perl.org/examples/static_server.html -> /learn/examples#static-server
* https://learn.perl.org/examples/dns.html -> /learn/examples#dns
* https://learn.perl.org/docs/ -> /learn/docs (WIP)
* https://learn.perl.org/books/ -> /books
* https://learn.perl.org/installing/ -> /get

### Deleted
* https://learn.perl.org/first_steps/ -> ??

## news.perlfoundation.org
### Migration
* https://news.perlfoundation.org/ -> /blog
* https://news.perlfoundation.org/post/* -> /blog/*

### Removal
* https://news.perlfoundation.org/tags
* https://news.perlfoundation.org/categories
* https://news.perlfoundation.org/authors

### Removal
* https://learn.perl.org/faq/ -> Completely redundant
* https://learn.perl.org/docs/keywords.html -> ?? (link to perldoc instead?)

## lists.perl.org
### Migration
* https://lists.perl.org/ -> /lists
* https://lists.perl.org/all.html -> /lists
* https://lists.perl.org/lists/* -> /list/* (WIP) 

### Removal
* https://lists.perl.org/tag/beginners.html
* https://lists.perl.org/tag/os.html
* https://lists.perl.org/tag/db.html
* https://lists.perl.org/tag/modules.html
* https://lists.perl.org/tag/web.html
* https://lists.perl.org/tag/science.html
* https://lists.perl.org/siteinfo.html

## dev.perl.org
### Migartion
* https://dev.perl.org/ -> /dev
* https://dev.perl.org/perl5/lists.html -> /list/perl5-changes and list/perl5-porters

