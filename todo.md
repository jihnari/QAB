you should, but for some reason you haven't:
- hey bro did you ever fix chisaki's LINE user name
- probably go back through and fix up tweets before ch10
- - guess what i didnt do
- youtube template/css is ugly. does that bother you enough to rewrite it into something legible?
- i think some 100 width somewhere is still screwing things up with ao3
- - this is still happening. 
- - - i think this was gmail and i think its fixed
- i changed dm-container to have a max of 100 and a min of 97 and i think that messed things up but
- - actually this is fine maybe
- - i dont think it fixed the issue tho
- - - it did not 
- did mei's name get changed everywhere
- ~~fix twitter skin (span to p) (also the new icon bar, the spacing is inconsistent)~~
- ~~make templates for twitter search and... something else but i forget~~
- - ~~we did this but where did it go~~
- ~~change out the new twitter icons for real images, not discord images. also ~~consider making them transparent~~ make them transparent. that would be real uggo as is on a black bg.~~
- kazuho's line name is inconsistent; gotta choose between "Kazuho" and "Kazuho Haneyama", and im thinking the second
- totally forgot about the "read #" on line group convos, gotta add that back (edit: did several of these)
- TWITTER USES SEP, NOT SEPT. UGH. **might ignore this 
- ~~twitter header is broken in most places~~
- litter in custom emotes
- you have fixed code for the vertical twitter line, so use it (gotta  figure out what its called/how to format, but its in the qcon chapter a lot) **i think i did this
- ~~new parser update breaks all twitter, ch3 and ch14? are fixed but nothing else.~~
- ~~have to remove all 'shift-up' from discord sections now due to change in ao3 margin handling; also may need to delete extra empty paragraphs, ao3 is nbsp-ing those on its own now~~
- ~~ch4 twitter broke (lightly); also is not in figure which might (re) break yt~~
- check soho chapter; signal is being weird and fat there 
- figure out if you can make a table overflow hidden ("new" twitter icons being fat)
- **bro you have two different versions of "this tweet is no longer" floating around. fix that. 
- consider fixing signal just-emotes to be like discord just-emotes. or to, in fact, just be dc-just-emotes bc we have no more space in the css. would require several/many edits and maybe one extra class(invisible signal box) but would look better
- ~~standardize kirishima. i thought i did this but no i didnt? capitalize his Is i think, give him quote marks (some mistakes (autocorrect first option)), no caps unless autocorrect catches it ~~
- ~~GMAIL UPDATE. figure out a non sucky semi automatic way. shouldnt be that hard except the dates are variable, so we'll have to do the first half and the second half, for every party involved. probably just four replacements, and the replacements can be reused in future chapters if the parties are the same.~~
-- chapters: 
-- qab1: 
--- 2, 9, 10
-- qab2: 
--- 6, 8, 10, 13 (33 and 34 are done) 
-- see notepad++, new 14
- (gmail is all fixed now) (hopefully)


i THINK i already:
- did the change from "dc-name-color" to "dc-name dc-color"
- all the dc elbows (did not verify that they all worked tho so here's hoping nothing broke )
- cleaned the code for new twitter icons with viewable impressions

i DID already:
- ch7, switch juzo and awata 


***update twitter sections. done on:
8??
12
14
15
18
19
20
21
haha guess what, you have to redo all of these now. :)
i think i got through chapter 14? 15? and then got tired. im sure you'll find them again. 
at some point i fixed all of the twitter headers and a lot of the names and re-uploaded. i didnt finish this process tho, because i just found a chapter that was un-finished (ch12)


error reports:
[chapter 1]
- Is crawler's handle supposed to be on the same line as the "<- Tweet"? Because it appears so on my phone (android). Same with Enon's tweet later in the chapter
  - this is a android > firefox issue im pretty sure. i dont know why its happening tho
  - ok this is an issue with float + spans. i would probably have to rewrite it entirely to fix it, which is doable but then fixing everywhere would suck. i definitely feel like ive done this already tho? like with the qcon chapters i remember mei's name being long and not behaving properly so i made it do the ellipsis thing? oh yeah they're in stay-blocks, thats why. ugh. hm. ugh.
- Blood Love's first message on the discord, her name overlaps with the discord header
[chapter ?]
- "overlapping lines with twitter in previous chapters"
  - this should be fixed, it was the ao3 update in december of 22. 
