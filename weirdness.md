ao3 -
- cant have <p class=clear> some stuff </p>. its gotta be standalone i guess? wonder if thats gonna break something...
- cant have <p class="clear anything"></p>. its gotta be COMPLETELY standalone ig.
- the yt img is weird. its got a shadow and also its shifted off of the red bar? and the margin is diff now. may have to overwrite whatev the new ao3 default is?
- - is it that 'bottom 4'?
- line randomly breaks sometimes, but i THINK only when its the last section?? but adding a couple of div clears didnt help. anyway, the workaround is go to the problem section, close the p, open the p, close the p around THAT SECTION AND THAT SECTION ONLY, open the p right after that and usually that + cussing does the trick
- had to move yt-line-## from bottom 4px to ~~5px~~ 5.5px bc of the way ao3 renders images? unclear.
- ~~also, ao3 is randomly adding a box-shadow to ONLY the yt vid images?? why is it doing that. do i need to put a box around the image/style the image maybe? it might be the only img w/o a style... hm. might be the default style if u dont apply. hmmmm.~~ fixed
- yes hello ao3 has a style class called "wrapper" so ur not allowed to use that anymore. renamed to 'relative-wrapper'
- using the built in table stuff adds in some weird padding and idk where its coming from. id like to overwrite it but im sick of looking for it... maybe someday.
- update, sometimes your only option is to overwrite all the table properties bc ao3 is so aggressive about nesting divs. related, table-layout:fixed does some HORRIFIC STUFF after ao3 has sprinkled "p"s all over the place
- ao3 completely ignores tables? its very kind about ignoring all formatting inside the table and just keeping it like it was. so just. just write tables.
- oh so hey you can just overwrite that, whoops. i was dumb then, tables are doable and in-fact ao3 respects them EXTREMELY WELL bc the whole website relies on them, you just gotta overwrite them correctly first.
- regardless of what the documentation says about "a single line will be ignored by the parser" 1, it will not. 2, it SUPER will not if you nest divs. every div gets at least one p shoved in there. you can sometimes solve this with sibling selectors and margin:0-ing the p, but sometimes you cant ¯\_(ツ)_/¯
- regarding the twitter skin changes on 8/19/22: the last reply section in a tweet including the new sub-reactions bar WILL break for no reason. you can solve this by wrapping everything in a stay-block. i have not found any other solutions.
- - INCORRECT. IT BREAKS ANYWAY. the fix is, rewrite that section to be p instead of span. but later. do it later.
- <th> and <td> are by default, "vertical-align: top" due to ao3 and inheritance? setting the <table> to "vertical-align: middle" fixes this issue on most platforms. however, there's something weird about the inheritance rules on ios/safari because it defaults to "vertical-align: top" again. you can fix this by making the class for every cell/td/th (or just the thing thats holding the thing not laying properly) to include "vertical-align: middle".
- 1/12/23, ao3's new update breaks spans that aren't wrapped by <p> already. known breaks: twitter "left dot". fix is to throw it in the below <p> block. fixed ch14 but no others so far. honestly i should just update that base code bc its janky but. i didnt do that.
- 2/4/23, this isnt a new issue but it is an issue i am just now understanding. the twitter breaks from october(?) were because of the new parser deleting extra empty <p> tags. it doesnt matter if they have a class, if they're empty theyre deleted. gotta &nbsp; those suckers. also potentially you could wrap the entire chapter in <figure>, thats been fixing some of the parser update introduced bugs.
- same as above, another new issue is that empty or comment lines are being interpreted into <p><br/></p> which breaks. a lot of things. i have sent in a ticket but for now the fix is to condense everything to a single line. 
- on some platforms, the main twitter user handle falls into the dot. this can be fixed with a <span class="stay-block"> in the right place. see ch1 section1 for an example. 
- on safari, something is broke but i dont remember what it was and i lost the bug report. i looked at it and said "oh yeah ive seen that before, hope i wrote it down so i know how to fix it" but i cant find anything about it. will update here when that gets found. ideally, it's logged on discord, but it'll take some hunting. it had to do with a scroll bar appearing in a weird place i think. it was twitter initially, but its tumblr this time

allowed operators:
- lost again :/

reddit:
- there is no consistency in this land. idk whats going on here but i dont like it. im just choosing elements and running w them bc there appears to be no internal logic.

twitter:
- back icon is suddenly not correctly aligned. i think i just swapped out the file for a transparent png and forgot/the final file dimensions were different, but its still weird that it happened.

notepad++:
- for testing purposes, add the following to html files
<link rel="stylesheet" href="css/qab2.css">

atom:
- hey STUPID, you gotta STAGE THE CHANGES, COMMIT TO MAIN and THEN you gotta push that push button at the very bottom of the window that you CANT SEE BC YOU ALWAYS SQUISH UR WINDOWS. anyway yes its a 3 step process, not 2. gl. godspeed.
- so hey when the package manager is "broken" go into settings > URI handling > click that button that lets it handle URIs. idk why it keeps resetting on you, but its annoying as heck
- theres also just an "install" option *right there in settings* lolol
- literally nothing is stopping you from doing multiple commit messages per push?? um????? why have you done this, why have you lived your life this way

html:
- if you set a bg-image for an img object, theres a weird gray border you cant do anything about. if you switch it to a p, that border magically goes away.
- bg-image: the bg image has to be set BEFORE the bg size is declared? or the other way around. apparently order matters, and not just on ao3.

github's free webpage:
- for some reason it doesnt like rel links if theyre global? (ie, the github hosted css file.) it insists on it being an actual relative link in the same file structure it's in. super annoying.
- code code doesnt work, only non-code code. (so no javascript.)
