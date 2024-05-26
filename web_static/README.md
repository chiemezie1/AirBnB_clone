# **In a nutshell**

# **HTML in a nutshell**

HTML is a markup language, which you are expected to be acquainted with from your level 2 project. If you feel like you need a mind-refresher, feel free to check out some tutorials, such as this one: [http://learn.shayhowe.com/html-css/](https://intranet.alxswe.com/rltoken/tex5mon7CRmLiifb8ega1A)

The breadth of HTML is actually not very large, as it is not meant to include advanced features; getting acquainted on each relevant tag and attribute doesn’t take much time, because there aren’t that many. The part of HTML that is trickiest to go over is probably forms, because there are quite a few possible components (text fields, checkboxes, text areas, … even sliders and color pickers in the most recent HTML specifications!)

The promise of HTML is that you should keep your document as properly structured and semantic as you can; and if you do, it should remain easily accessible to the browsers that will exist in 20 years, while also making it easier to keep your code accessible, performant, and optimized for search engines through time. See: [http://vanseodesign.com/web-design/semantic-html/](https://intranet.alxswe.com/rltoken/afy6DLTmHklXhKpOFeXcwA)

# **CSS in a nutshell**

CSS (Cascading Style Sheets) were invented by Bert Bos and Håkon Wium Lie, because HTML was getting less and less semantic, and more and more about presentation, which would make it less future-proof and more verbose.

For instance, you could write that:

`<center><p><font color="red">Hello to <b>all</b> of my visitors!</font></p></center>`

The fact that a text should be centered, have a certain color, and be represented in bold is part of presentation, and shouldn’t be in the HTML. The fact that it’s a paragraph, however, is part of the structure, and therefore is semantic information.

Also, if you needed to make a whole page red, you needed to write `<font color="red">` at every single line.

CSS enforces not only semantics in the HTML, but also mutualization of the presentation layer, and therefore less code.

Now, `<center>`, `<font>` and `<b>` are banned in HTML, and we got some more semantic tags, like `<strong>`, `<em>`, and more recently, `<article>`, `<section>`, `<aside>`, …

Wondering about the difference between `<strong>` and `<b>`? –> [http://www.html-5-tutorial.com/strong-and-b-elements.htm](https://intranet.alxswe.com/rltoken/uS6_oicaLH2H7zD40oJpfQ)

# **Web development tools**

Before diving into your first front-end development project, you should take some time to learn to use the web development tools that are embedded into all modern browsers. Search online how to access the ones for the browser you wish to be using.

Those tools are typically more powerful than just for HTML/CSS development, and also cover JavaScript debugging, tracking HTTP requests, even some performance diagnostic tools sometimes. The HTML/CSS pane usually displays the HTML code as the browser interprets it, on the left (as a tree that you can deploy or fold back), and the CSS rules to the right, which you can edit in place. Of course, all of the edits you’re doing in there are being done in the browser’s memory. If you want to keep these changes, you’ll have to do them in your source code.

!https://intranet.alxswe.com/images/contents/higher_level_programming/concepts/browser_tool.png

# **Block or inline? Absolute or relative?**

One key notion to CSS is in the difference between the `block` and `inline` values to the `display` statement, and also `inline-block`. The most basic `display` values:

- `none`, hides the HTML element.
- `block` means it will be fluid (take up the entire width of the browser’s window) and will stack up vertically (top to bottom). It is the default behavior of `<p>`, `<ul>`, `<li>`, `<h1>`, `<div>` … You can add margins and paddings to those.
- `inline` means it will be inside the textual flow of the block. It is the default behavior of `<a>`, `<strong>`, `<em>`, `<img>`, `<span>`, … You can not add margins and paddings to those.
- `inline-block` is a mix of both: the element will be inside the textual flow of the block, but it will also accept margins, paddings, …

Another key notion is the `position` statement:

- `static` is the one by default, so you’ll rarely have to explicit it. An element is positioned where it is expected that it should be.
- `relative` will help you position the element relatively to its expected position, for instance 2px higher, or 5px to the left, etc.
- `absolute` will remove the element from the flow of the page, and position it relatively to another block, most often the entire page. For instance, before you change anything else, it will often be at the top left of the page, “flying ” over the rest of your HTML document.
- `fixed` will do the same thing as `absolute`, but will behave differently when you scroll up or down: absolute elements will scroll with the rest of the page, while fixed ones won’t, and will stay right at the same spot in front of you. More about positions here: [http://www.w3schools.com/css/css_positioning.asp](https://intranet.alxswe.com/rltoken/HHAcZsrOc7YI_J8yjco0kA)

# **CSS Layouts**

Because CSS was never meant to be to do complex layouts, but was meant for “flat” documents, CSS layout went through a bit of history.

# **Tables and images**

Initially, web designers and brands wanted websites to offer “pixel-perfect” like on print. However, this was very difficult to achieve as CSS did not render similarly across browsers, and fonts rendered very differently depending on the OS (which is still the case today, actually). Therefore, the very first “visual” websites were mostly images ordered together in border-less tables. This was obviously a nightmare in performance (huge images + very verbose HTML did not fare well with slow web connections) and in accessibility/SEO (tables are meant for tabular data and are recognized as such semantically, and texts in images were not recognized at text; for instance, they couldn’t be copy-pasted).

HTML frames were also very used at the time, but they fell out of fashion for those same reasons: performance because you’re loading many webpages instead of one, accessibility because it was near impossible to navigate the user from one frame to the other (with the keyboard, for instance), SEO because the URL of a webpage didn’t change when navigating, so some composite pages didn’t even have a navigable URL.

# **Early web standards**

In the late 90s, a group of web developers and designers (most of them were a bit of both) started to evangelize about how it was entirely possible to make built great websites entirely with standards. The “Standard Web Project” was created in 1998 by Jeffrey Zeldman, who subsequently wrote his breakthrough book “Designing with Web Standards”. The book was a list of practical tricks to get each browsers to do what you need them to do.

Keep in mind that each browser still had a very, very different interpretation of CSS back then, so you basically had to develop one CSS per browser. Eventually, browser got more mature, and most code could gradually be mutualized for all browsers. Today, websites that don’t leverage the web standards are very rare.

Some key links from that time:

- The Dao of Web Design is an article written in 2000 on A List Apart, the blog Jeffrey Zeldman founded for front-end experts to share their tricks. While most articles from back then have aged pretty badly, since browsers changed so much over the last few years, this one is still very current. It teaches people to let go of pixel-perfect, in order to embrace the goodies contained in web standards. Read it here: [http://alistapart.com/article/dao](https://intranet.alxswe.com/rltoken/gmmBwe4B-dzIJeOPRI4tlg)
- CSS Zen Garden was created by Dave Shea to showcase what CSS can do. It is basically a single HTML file, on which any one can contribute an original CSS stylesheet, to make it do interesting things. Check it out here: [http://www.csszengarden.com](https://intranet.alxswe.com/rltoken/_GZP4aII3C67DhIdb7AvjQ)

# **Float layout**

As we’ve discussed, natively, HTML stacks fluid blocks vertically. People wanted to stack blocks horizontally too (next to each other), but except for positioning them as absolute (which breaks the flow of the page), the only other way to do it was to make them “float”.

The `float` statement, which takes `left` or `right` (or the default value `none`) was designed to make medias (like images) float the left or right of the text; and the text would nicely “go around” the image. But people found ways to “abuse” the `float` statement in order to build complex layouts. The `clear` statement is `float`‘s antagonist: it makes an element avoid to float by its previous elements.

More about `float` and `clear`: [http://www.w3schools.com/css/css_float.asp](https://intranet.alxswe.com/rltoken/4tFR069hhsUBTdkGrESwNQ)

Because more recent options are not entirely mature yet, a lot of websites are still being made with floating layout.

# **CSS Display Table**

It took long years for the W3C to have consensus on some layout specifications, and display table is one of the first ones that made it maturity. The idea is to take some HTML that doesn’t contain the `<table>` element, but make it behave like tables just with CSS.

It had been moderately popular, but it never rose to widespread uses, because one could not manage every layout use case this way.

# **CSS Flexbox**

As a far more powerful alternative to CSS Display Table, CSS Flexbox has huge support from the browsers and the industry, despite the implementations in browsers not being 100% consistent in all cases. Many websites and web applications in the industry use CSS Flexbox: some mentors working at Salesforce confirmed that all applications are now built using it; another mentor working on Google Photos confirmed that it is what is being used there too. And for widespread adoption, the most used CSS frameworks are now switching to Flexbox, one by one.

Here is an excellent and fun tutorial for learning Flexbox: [http://flexboxfroggy.com](https://intranet.alxswe.com/rltoken/V4akKyBG-FJC8HXMdnCLQw)

# **The other ones?**

Other CSS layout specifications are in the work at the W3C, such as CSS Grid; but none of them seem near maturity at all at this point. And it can be argued that the support CSS Flexbox is getting could actually be detrimental to them, since the industry seems gradually happy with it.

# **CSS Media Queries and Responsive Web Design**

Another recent interesting piece of recent CSS history is the introduction of the CSS Media Queries, and the concept of Responsive Web Design.

Media queries allow to express that certain CSS rules should only be executed when certain conditions are in place (such as based on the screen’s resolution, or the number of colors a graphics card can handle). But the one condition that started to get very used, is the one allowing to only execute some CSS depending on the browser’s width. As you may have understood, this allows a single CSS codebase for a website regardless of the size of the browser, enabling and disabling some CSS rules when it passes certain width thresholds.

Do you remember Jeffrey Zeldman? (He’s the guy who founded A List Apart, the Web Standards Project, and wrote Designing with Web Standards) He’s part of the people who actually came up with the notion of Responsive Web Design, the idea to use media queries to make a single website adapt depending on the browser’s width.

# **Media query syntax**

It looks like this:

```
@media screen and (min-width:600px) {
  nav {
    float: left;
    width: 25%;
  }
  section {
    margin-left: 25%;
  }
}

```

The above CSS rules will only apply when the browser displays the webpage on a screen (as opposed to printed on paper, for instance), and the browser’s window is at least 600px wide.

More about media queries: [http://www.w3schools.com/css/css_rwd_mediaqueries.asp](https://intranet.alxswe.com/rltoken/sszKefXZLcbYaoVj59CvMg)

# **Viewport**

Feature phones (the things that came before smartphones) didn’t “zoom pages out” when displaying a non-mobile webpage so that you could see the whole page; you would simply see a corner of the webpage that was the size of your phone’s screen, and had to swipe around to see the rest.

When Apple introduced the iPhone in 2007, it introduced the notion of viewport: the width of the phone would, by default, not be displaying the same small width of the webpage; it would display 1024px on a device that really is 320px wide. Instead of swiping around to see each bit of the webpage, you would have to zoom in to read texts. Soon, all other smartphones adopted the same behavior.

The way to describe it is: although the screen is 320px wide, its viewport (what it really displays of a webpage) is 1024px wide.

But this would create problems with responsive websites, as you actively want them to display the real width of the screen. Therefore, Apple introduced a HTML tag to override the viewport the browser, which all other browsers implemented later too. This is what developers typically set it as for fluid designs such as responsive web designs:

```
<meta name="viewport" content="width=device-width, initial-scale=1">

```

More about the viewport: [https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag](https://intranet.alxswe.com/rltoken/p8zx6KM7nBRLmfkoLFqqbA)

# **Some links**

- Many of the CSS concepts on this page are introduced and demoed on this very visual and well-polished website: [http://learnlayout.com](https://intranet.alxswe.com/rltoken/TXR1AzFVk9kr-SbYgahG3w)
- “Like the CSS spec, but readable”, according to Kaelig (one of your mentors who is a front-end engineer at Salesforce): [http://book.mixu.net/css/](https://intranet.alxswe.com/rltoken/EBwMi32IlfoF_xWeZc45_Q)




# **The trinity of front-end quality**

*Have you noticed that this concept does not contain any link? By now, you should be able to find your own sources, based on the proper technical terms we’ll keep giving you in the concepts, usually introduced **in bold font**.*

When talking about front-end quality, there are 3 main end goals that front-end developers keep striving for:

- **Accessibility**
- **Performance**
- **SEO**

# **SEO**

**SEO (Search Engine Optimization)** refers to making sure your website is ranked relevantly high on search engines’s **SERPs** , like Google’s.

Because the exact rules checked by search engines are not entirely public, and competition for popular **queries** is so fierce, SEO is often referred to as black magic… and well, sometimes it does feel like it is! But there are very clear best practices to apply to be respected and taken seriously by Google and its friends.

Of course, making your markup as semantic as you can will help the search engine understand your webpage; but by now, most websites do that right, so it is definitely not going to be enough.

More current strategies involve the content you put in your website, the URLs, the internal and/or external linking, the website’s performance, … The list of things that can be done to improve one’s SEO is endless!

To monitor SEO results, people usually use monitoring tools, which are going to keep track of search engine rankings continuously for them in various countries. Most of those tools are paid, but you’ll find a few free ones with the most limited features. Many of those tools also meant to help define the right SEO strategy in the first place, when you try to figure out which queries you should be optimizing for (a step called **keyword research** ). For instance, if the tool tells you that a query doesn’t involve many competitors fighting for it, and yet Google Trends tells you it is a query that is heavily being ran by Google users, then you might be sitting on a goldmine!

Another important note to keep in mind is that a SEO strategy will of course contain the **targeted queries** of someone actively looking for you (for instance, Safeway probably works hard to be ranked high on the “safeway” query), but also the **untargeted queries** of someone who is not specifically looking for you, but whose attention you seek (for instance, Safeway probably works even harder to be ranked high on the “san francisco grocery store” query, or one even more competitive: just “grocery store”, if it’s relevant for them). Deciding which queries make sense to pursue is a critical component of SEO strategy.

# **Accessibility**

Stéphane Deschamps is a mentor and a hardcore internationally recognized web accessibility expert. He once told me the story of how he starts his accessibility training sessions.

First thing: he’d start by asking everyone to stand up. Then he’d ask people wearing glasses to sit down; then people who had back pain sometimes; then people who already had had a broken arm; etc. At the end of his list, he’d tell the people still standing that they could ignore the next few hours, because they will be about all of the other people in the room. The catch is that by then, there would only be at most one person standing, most often none. He now had the room’s attention.

In real life, it is estimated that a website may lose as high as 15% of its visitors to bad accessibility. Think: someone with poor eyesight who couldn’t read the menu button properly because of their low contrast, and gave up; or someone who worked hard with their hands today, and can’t handle the mouse anymore to fill in a long form, and the keyboard navigation won’t work, etc.

Having a semantic and valid HTML markup will already go a long way to make one’s website accessible; but it is definitely not enough, and issues are hidden in the details (images, colors, …).

Also, for complex applications for which you feel like some bits of the page should be more explicit in their purpose, you can give that extra information with **WAI-ARIA**  (often referred to as just “ARIA”).

# **The specific case of network fault-tolerance**

Another kind of loss of accessibility is when resources (such as CSS files, images, JavaScript files) are inaccessible, such as for network reasons. Without CSS, without JavaScript, without images, your website should still work. It may not have as much styling and interactivity, but people must still be able to post that micro-blogging status, for instance.

Browsers often have built-in tools (or plugins) that allow you to see your website without images, without CSS, without JS, …

# **Front-end performance**

Did you know that over 90% of the time spent by a user waiting for your webpage is happening in the front-end, rather than the back-end? The reasons are pretty obvious when you think about it: you can host your code on faster servers, or scale it on a higher number of them; but there’s nothing you can do to make the user’s browser environment better. To ensure all browsers can interpret it, you have to send your user code that respects web standards (which are sometimes verbose), and you can’t make that code smaller than the standards allow. It has to go through the network, be entirely loaded and run by the browser, you can’t have the browser “preload” anything. Well, actually…

There are many pitfalls and tricks to address web performance. All ways attempt to either make each file smaller, or to lower the number of files (it is magnitudes more expensive to download two files of 50kB each, than one file of 100kB).

Some pitfalls:

- Forgetting to enable GZip and set Cache expirations on your web server’s configuration
- Using many external JS libraries, including some you absolutely didn’t need
- Using huge images displayed smaller
- Leaving the metadata in your images
- Etc…

Some tricks:

- Images sprites
- No CSS or JS inside the HTML (.js and .css files will be cached on first call, won’t have to be downloaded next time).
- Ajax calls that can be done with GET HTTP verb should use it (that way, they are cached)
- CSS and JS files are concatenated into one single file each
- CSS and JS files are “minified”
- Images are recompressed

As usual with quality, you will want to measure. But there are many ways to measure a front-end’s load time. Should it be the **Time To First Byte**? **Page Load Time**? **Time To First Paint**? You should define your strategy, and monitor the measures you feel are relevant.

Typically, the way measures are done is:

- The cache is cleared, the page is loaded, and the measurements are noted. The operation is done 3 times. If one is very significantly apart to the others, it is removed, to account for potential network issues unrelated to the website. The final result is the average of remaining calls.
- The page is loaded without clearing the cache, and the measurements noted. Again, 3 times, removing very significantly wrong measures, and the final result is the average. How to measure, you say? Just use the performance measuring tools that are likely to be in your browser.

!https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/6/54b6264a88145d2d88e07da5ad9c9f5977881031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240526%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240526T165548Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=40b17bfdb05d176c423ac11874f04239ac1d2d17165852af9aae297bf0a6b306

*This is Google Chrome’s diagnostic of the stackoverflow.com website, with cache cleared. As you can see, the back-end performance of generating the HTML page is 180ms (actually way less, if you remove the round-trip the data is doing) out of 1.30s to finish. Load time is 1.11s, which is not too bad!*