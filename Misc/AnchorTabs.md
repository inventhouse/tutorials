Taming My Browser Tabpocalypse
================================

For a long time, I would just open new tabs in any browser window that was convenient and look up whatever was on my mind.  I'd sometimes try to open a fresh window when I was starting something new, but later I'd find I had several different windows that each had some content for a particular thing.  Often, I wouldn't be able to find a tab I _knew_ I had open _somewhere_, so I'd have look it up again.  Tab Chaos.  There had to be a better way.

Anchor Tabs
-----------
_"1 weird trick" for managing browser tabs_

_(Note: I started doing this before "tab groups" became a thing in major browsers; it has continued to serve me well especially combined with my tabgrab script below, so I haven't really tried tab groups)_

**1.** Consider the first tab of each window the "anchor" for that topic / task; maybe use a relevant Wikipedia article, the ticket of the issue or feature, or the project's home page, something that serves to identify the "subject" of that window.

**2.** Be strict about using the right window; if a tab opens in a window where it doesn't belong, at _least_ pull it out; ideally put it where it belongs

**3.** _Always_ switch back to the first tab when minimizing the window (often just switch back to it anyway) so it shows up in the window list under a consistent name.  In most browsers `⌘1` (or whatever the "command" key for your platform is) will do that - `⌘1 ⌘M`, quick and easy!

**Bonus:** If you're on macOS, enable App Exposé (three-finger swipe down) in the Trackpad [System Settings](x-apple.systempreferences:) (sorry, can't link to that specific pane.)  Try to minimize windows you're not using (`⌘1 ⌘M`!) to keep the number of active windows around a half-dozen to a dozen; it's _much_ easier to scan a handful of browser windows than all windows for all apps.

This technique has worked very well for me, I'm able to go back to things I worked on weeks ago and find the query I cooked up for it or whatever I'm looking for.

Tabpocalypse II
---------------
It worked _too_ well; _SO_ many windows with so much great context, and I never knew which would be useful or not so I kept them minimized but had no way cull or archive them - Over 800 tabs in more than 300 windows at one point!

I experimented with bookmarking groups of them, but the workflow was slow and the bookmarks were browser-specific, I didn't have a good way to extract them.

So I Wrote a Script
-------------------
[Tabgrab](https://github.com/inventhouse/BenBin/blob/master/tabgrab) works with Safari or Chrome to collect links for all those tabs _and_ it preserves the Anchor Tab and window grouping.  Here is the full usage:

```
usage: tabgrab [-h|--help] [-c|--copy] [BROWSER]
       Collect tabs from all windows as a markdown list of links with
       the first tab of each window as the parent of the remaining tabs.
       BROWSER defaults to the BROWSER_APP environment variable, otherwise
       the default handler for 'https' is used to guess the system browser.

       -c, --copy    Copies the list to the pasteboard

       -n, --num-windows N
                     Collects tabs from the first N windows, defaults to
                     all windows

       -h, --help    Print this message and exit
```

How I Use Tabgrab
-----------------
When the tabs and windows proliferate too much, or I'm going to reboot for a software update, I make a new tabdump file:
```sh
tabgrab > pensive/Notes/Tabdumps/Tabs-`hostname | sed -e 's/\\.local//'`_`date "+%Y-%m-%d"`.md
```

...and then _I close them **all**_; in Safari: Window > Merge All Windows, then close that mega-window, in Chrome, open the File menu and press the `option` key, "Close Window" becomes "Close All".

I check the tabdumps into a private repo I call my "pensieve" (it's a [Harry Potter reference](https://www.wizardingworld.com/writing-by-jk-rowling/pensieve); here is a [template repo](https://github.com/inventhouse/pensieve?tab=readme-ov-file#making-your-own-pensieve) if you want to make your own.)  GitLab/GitHub/Gitea/etc all render Markdown files automatically, so from the newly pushed file I can re-open any tabs I actually _am_ using, and I can search in that directory to find links again.
  I even use it as automatic bookmarking: if I see an interesting link and think I even _might_ want to find it again someday, I'll open it in its own window and minimize it; it'll get collected and saved along with everything else 😁
