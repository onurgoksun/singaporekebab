"""Builds the /guides/ section of singaporekebab.com.

Run:  python3 tools/build_guides.py   (from the repo root)
Edit GUIDES below and run again. Remember to keep sitemap.xml in sync (this script rewrites it).
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_pages import HEADER, FOOTER, SITE, ROOT, WA_ICON, PXU

PUBLISHED = "2026-10-25"

# Each body is trusted HTML written by us. Keep claims factual; cite sources in "sources".
GUIDES = [
  {
    "slug": "what-is-kebab",
    "title": "What Is Turkish Kebab? The Story of Döner, from Bursa to Singapore",
    "h1": "What is Turkish kebab? The story behind the spit",
    "desc": "Where döner kebab comes from, what the name means, how real Turkish kebab is made, and how to spot a good one in Singapore.",
    "img": "hero",
    "card": "Where döner kebab comes from, what the name means and how it's made.",
    "body": """
<p>Ask for a kebab in Singapore and you'll usually get thin slices of meat carved from a tall rotating spit, wrapped in bread with salad and sauce. That dish has a Turkish name, <em>döner kebap</em>, and a story that goes back more than 150 years.</p>
<h2>What the name means</h2>
<p><em>Kebab</em> is a broad word for roasted or grilled meat that travelled through Arabic, Persian and Turkish. <em>Döner</em> comes from the Turkish verb <em>dönmek</em>, "to turn". So döner kebab simply means "turning roast": meat that slowly rotates next to the heat while the outside is carved off.</p>
<h2>From a horizontal spit to a vertical one</h2>
<p>Stacks of seasoned meat were roasted on horizontal spits in the Ottoman Empire for centuries. The big change came in the 19th century, when cooks stood the spit upright. A vertical spit takes less space, lets the fat baste the meat as it turns, and makes it easy to shave off thin, crisp slices.</p>
<p>Two cooks are usually credited: <strong>İskender Efendi of Bursa</strong>, whose family says he came up with the idea in the mid-1800s, and <strong>Hamdi Usta of Kastamonu</strong>, who may have done it even earlier. Bursa is still the city most people link with döner, and İskender's name lives on in <a href="../types-of-turkish-kebab/">iskender kebab</a>: döner over pide bread with tomato sauce, melted butter and yoghurt.</p>
<h2>How kebab travelled the world</h2>
<ul>
<li><strong>Istanbul</strong> made döner a city favourite in the 20th century, and it was sold as a sandwich there by the 1960s.</li>
<li><strong>Greece</strong> got its own version, <em>gyros</em>, which also means "turn". <a href="../kebab-vs-shawarma-vs-gyros/">See how they differ</a>.</li>
<li><strong>The Arab world</strong> developed <em>shawarma</em>, a name that also comes from a Turkish word for turning.</li>
<li><strong>Berlin</strong> turned döner into fast food in the early 1970s, when Turkish workers started selling it in bread with lots of salad and sauce. Kadir Nurman is often named as the man who popularised the sandwich in 1972, though other people have made similar claims.</li>
</ul>
<h2>How real Turkish kebab is made</h2>
<p>Traditional döner is built by hand. Thin slices of marinated meat are stacked layer by layer onto the spit, sometimes with minced meat between them, and roasted slowly beside the heat. The cook shaves off thin slices only when the outside is browned and crisp, then lets the next layer cook.</p>
<p>Kebab shops can also buy factory-made cones, which are cheaper but often taste the same everywhere. That's why the best kebab tastes different from shop to shop: the meat, the marinade and the way it's carved all matter.</p>
<h2>How to spot good kebab in Singapore</h2>
<ul>
<li><strong>Thin slices, crisp edges.</strong> Good döner is carved thin, with caramelised edges and a juicy middle.</li>
<li><strong>Carved when you order.</strong> Meat that sits in a tray after carving dries out quickly.</li>
<li><strong>Fresh bread and simple sides.</strong> Warm pide or wraps, crunchy salad, garlic yoghurt and a bit of chilli are enough.</li>
<li><strong>A real spit.</strong> Kebab from a vertical spit beats meat that's been pan-fried from frozen strips.</li>
</ul>
<p>Want to see it carved fresh at your next event? <a href="../../live-kebab-carving/">Live kebab carving</a> brings the spit to your venue.</p>
""",
    "faq": [
      ("What does döner mean?", "Döner comes from the Turkish verb dönmek, which means to turn. Döner kebab means turning roast, after the vertical spit that rotates next to the heat."),
      ("Where was döner kebab invented?", "Döner kebab comes from the Ottoman Empire. The vertical spit is usually credited to cooks in Bursa and Kastamonu in the 19th century."),
      ("Is kebab the same as shawarma?", "They're close relatives. Both are carved from a vertical spit, but döner is the Turkish version and shawarma the Arab one, with different spices, sauces and bread."),
    ],
    "sources": [
      ("Doner kebab, Wikipedia", "https://en.wikipedia.org/wiki/Doner_kebab"),
      ("What is Turkish doner kebab, National Geographic", "https://www.nationalgeographic.com/travel/article/what-is-turkish-doner-kebab"),
    ],
  },
  {
    "slug": "kebab-vs-shawarma-vs-gyros",
    "title": "Kebab vs Shawarma vs Gyros: What's the Difference?",
    "h1": "Kebab vs shawarma vs gyros: what's the difference?",
    "desc": "Döner kebab, shawarma and gyros are all carved from a vertical spit. Here's how they differ in origin, meat, sauce and bread.",
    "img": "doner",
    "card": "Three spit-roasted cousins, and how to tell them apart.",
    "body": """
<p>In Singapore you'll see all three names on menus, sometimes for the same thing. They are related: each is meat roasted on a vertical spit and carved into slices. But they come from different places and taste different.</p>
<h2>The short answer</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Döner kebab</th><th>Shawarma</th><th>Gyros</th></tr></thead>
<tbody>
<tr><th>From</th><td>Turkey</td><td>The Levant and wider Arab world</td><td>Greece</td></tr>
<tr><th>Usual meat</th><td>Chicken, lamb or beef</td><td>Chicken, lamb or beef</td><td>Pork or chicken</td></tr>
<tr><th>Sauce</th><td>Garlic yoghurt and chilli, or none</td><td>Garlic sauce (toum) or tahini</td><td>Tzatziki</td></tr>
<tr><th>Bread</th><td>Pide, flatbread or thin lavash wrap</td><td>Thin flatbread</td><td>Thick pita</td></tr>
</tbody></table></div>
<h2>Döner kebab</h2>
<p>The Turkish original. The meat is stacked by hand, slow-roasted and shaved off in very thin slices. In Turkey it's served on a plate with rice, in half a loaf of bread, or as a <em>dürüm</em> wrap. Iskender kebab, döner over bread with tomato sauce, butter and yoghurt, is one of its best-known forms. <a href="../what-is-kebab/">Read the history of döner</a>.</p>
<h2>Shawarma</h2>
<p>The Arab version, popular from Lebanon to the Gulf. Its name also comes from a Turkish word for "turning". Shawarma marinades often use warm spices, and it's usually wrapped in thin bread with garlic sauce or tahini, pickles and sometimes fries.</p>
<h2>Gyros</h2>
<p>The Greek version, whose name also means "turn". Gyros is usually pork or chicken, served in a thick pita with tomato, onion, fries and tzatziki.</p>
<h2>So which one are you eating in Singapore?</h2>
<p>Many shops in Singapore use "kebab" and "shawarma" interchangeably. If the meat is thinly carved from a spit and served with garlic yoghurt in pide or a wrap, it's closest to Turkish döner. If it comes with toum, pickles and fries, it's shawarma style.</p>
<p>At Singapore Kebab we serve the Turkish way: chicken and lamb kebab carved thin, with warm bread, salad, garlic yoghurt and chilli. See every dish on our <a href="../../menu/">menu</a>.</p>
""",
    "faq": [
      ("Is shawarma the same as kebab?", "Not exactly. Both come from a vertical spit, but döner kebab is Turkish and usually carved thinner, while shawarma is the Arab version with its own spices and garlic or tahini sauce."),
      ("Is gyros Greek or Turkish?", "Gyros is the Greek version of spit-roasted meat. Its name, like döner, means turn."),
    ],
    "sources": [
      ("Doner vs Shawarma vs Gyro, Yummy Istanbul", "https://yummyistanbul.com/doner-vs-shawarma-vs-gyro/"),
      ("Doner kebab, Wikipedia", "https://en.wikipedia.org/wiki/Doner_kebab"),
    ],
  },
  {
    "slug": "types-of-turkish-kebab",
    "title": "7 Types of Turkish Kebab to Try: Döner, Iskender, Adana, Beyti and More",
    "h1": "7 types of Turkish kebab to try",
    "desc": "A quick guide to Turkish kebabs: döner, iskender, adana, beyti, şiş, köfte and ali nazik, and which ones work best for catering.",
    "img": "weddings",
    "card": "Döner, iskender, adana, beyti and more, explained.",
    "body": """
<p>In Turkey, kebab doesn't mean one dish. It's a whole family of grilled and roasted meats, and every region has its own. Here are seven you'll meet on Turkish menus, including ours.</p>
<h2>1. Döner kebab</h2>
<p>Marinated meat stacked on a vertical spit, slow-roasted and carved into thin slices. Served in a wrap, in bread or on a plate with rice. <a href="../what-is-kebab/">Its history</a>.</p>
<h2>2. Iskender kebab</h2>
<p>Named after İskender Efendi of Bursa. Döner is laid over cubes of pide bread, then topped with tomato sauce, melted butter and yoghurt on the side. Rich and comforting, and a favourite for sit-down dinners.</p>
<h2>3. Adana kebab</h2>
<p>From the southern city of Adana. Minced lamb mixed with red pepper is pressed onto a wide iron skewer and grilled over charcoal. It's usually spicier than other kebabs.</p>
<h2>4. Beyti kebab</h2>
<p>Today's beyti is usually minced meat, grilled, wrapped in thin lavash bread, sliced and served with tomato sauce and yoghurt. The dish is named after Beyti Güler, a well-known Istanbul restaurateur, whose 1960s original used lamb fillet.</p>
<h2>5. Şiş kebab</h2>
<p>Cubes of marinated chicken or lamb grilled on a skewer. Simple, juicy and easy to share.</p>
<h2>6. Köfte</h2>
<p>Turkish meatballs or patties, grilled and served with rice, salad and bread. Every region has its own recipe.</p>
<h2>7. Ali nazik</h2>
<p>Smoky grilled eggplant mashed with yoghurt and garlic, topped with meat. A south-eastern Turkish classic that pairs creamy and savoury.</p>
<h2>Which kebabs work best for catering?</h2>
<ul>
<li><strong>For live carving:</strong> döner, carved to order. It's the most theatrical and the fastest to serve a queue.</li>
<li><strong>For office lunches:</strong> kebab over rice, wraps and köfte boxes travel well and are easy to eat at a desk.</li>
<li><strong>For dinners and weddings:</strong> iskender and beyti add a sit-down feel, with meze and baklava to finish.</li>
</ul>
<p>See which of these we serve, with photos and prices, on our <a href="../../menu/">menu</a>.</p>
""",
    "faq": [
      ("What is the most popular Turkish kebab?", "Döner kebab is the best known worldwide. In Turkey, iskender, adana and şiş kebab are also very popular."),
      ("What is the difference between adana and döner kebab?", "Adana kebab is spiced minced meat grilled on a wide skewer, while döner is layered meat roasted on a vertical spit and carved into thin slices."),
    ],
    "sources": [
      ("Doner kebab, Wikipedia", "https://en.wikipedia.org/wiki/Doner_kebab"),
      ("What is Turkish doner kebab, National Geographic", "https://www.nationalgeographic.com/travel/article/what-is-turkish-doner-kebab"),
    ],
  },
  {
    "slug": "how-much-food-per-person",
    "title": "How Much Food to Order for an Office Event in Singapore",
    "h1": "How much food to order per person for an office event",
    "desc": "A simple guide to catering quantities in Singapore: how much food per guest for lunches, parties and buffets, plus food safety tips from SFA.",
    "img": "office",
    "card": "Simple quantities per guest, plus SFA food safety tips.",
    "body": """
<p>Order too little and the last guests go hungry. Order too much and you're throwing food away at 3pm. Here's a simple way to get the quantity right for office lunches and events in Singapore.</p>
<h2>A starting point per guest</h2>
<p>Catering guides commonly suggest about <strong>225 to 450 g of food per person</strong> for a buffet meal, with around <strong>170 to 225 g of main protein</strong> per person. For a kebab menu, that works out roughly as:</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Per guest, as a guide</th></tr></thead>
<tbody>
<tr><th>Office lunch (meal boxes)</th><td>1 box: kebab or falafel, rice or wrap, salad and sauce</td></tr>
<tr><th>Lunch buffet</th><td>1 main portion of kebab, a scoop of pilav, salad, bread, 1 dessert piece</td></tr>
<tr><th>Live kebab carving</th><td>1 to 2 wraps or plates, depending on what else is served</td></tr>
<tr><th>Dinner or wedding</th><td>Main kebab plus 2 to 3 sides or meze and dessert</td></tr>
</tbody></table></div>
<p>These are starting points, not rules. Your quote will be built around your actual guests.</p>
<h2>What changes the numbers</h2>
<ul>
<li><strong>Time of day.</strong> Lunch portions are lighter than dinner.</li>
<li><strong>Length of the event.</strong> Longer events need more snacks or a second serving.</li>
<li><strong>Who's coming.</strong> A young, active team eats more than a client seminar.</li>
<li><strong>Other food.</strong> If there are canapés or a dessert table, reduce the main course.</li>
<li><strong>No-shows.</strong> Office events often see a few people drop out. Confirm the headcount a few days before.</li>
</ul>
<h2>Plan for mixed diets</h2>
<p>Singapore teams are diverse. Ask your guests early about vegetarian, no-beef and allergy needs, and count them separately. A good rule is to order vegetarian portions for every vegetarian guest plus a few extra, because non-vegetarians often try them too.</p>
<h2>Food safety tips from SFA</h2>
<p>The Singapore Food Agency's guidelines for ordering catered meals recommend:</p>
<ul>
<li><strong>Eat within 4 hours.</strong> Catered food shouldn't sit at room temperature for more than 4 hours from cooking to eating, including delivery and set-up.</li>
<li><strong>Check the "consume by" time</strong> on each box or buffet table, and discard food after it. Caterers must label it, and removing or changing the label is an offence.</li>
<li><strong>Time the delivery.</strong> Ask for delivery no more than 1 hour before the meal.</li>
<li><strong>Keep hot food hot</strong> (above 60°C) and cold food cold (below 5°C).</li>
<li><strong>Use an SFA-licensed caterer.</strong> SFA publishes a list of licensed caterers.</li>
</ul>
<p>Not sure about your numbers? Tell us your guests and event in the <a href="../../plan/">menu planner</a> and we'll suggest the right quantities.</p>
""",
    "faq": [
      ("How much food per person for a buffet?", "Catering guides commonly suggest about 225 to 450 g of food per person in total, with around 170 to 225 g of main protein. Adjust for time of day, event length and appetite."),
      ("How long can catered food stay out in Singapore?", "SFA guidelines say catered food shouldn't be left at room temperature for more than 4 hours from cooking to eating, so follow the consume-by time on the label."),
    ],
    "sources": [
      ("Guidelines for ordering catered meals for functions and events, Singapore Food Agency", "https://sfa.gov.sg/docs/default-source/food-retail/guidelines-for-ordering-catered-meals-for-functions-and-events.pdf"),
      ("A guide to catering portion sizes, WebstaurantStore", "https://www.webstaurantstore.com/article/1013/catering-portion-size-guide.html"),
    ],
  },
  {
    "slug": "when-to-book-catering",
    "title": "When to Book Catering in Singapore: A Planning Timeline",
    "h1": "When should you book catering in Singapore?",
    "desc": "How far ahead to book office lunches, live carving and wedding catering in Singapore, which seasons get busy, and a simple planning timeline.",
    "img": "live-station",
    "card": "How far ahead to book, busy seasons, and a simple timeline.",
    "body": """
<p>The short answer: the bigger and more special the event, the earlier you should book. Here's a simple guide for planning catering in Singapore.</p>
<h2>How far ahead to book</h2>
<div class="table-wrap"><table>
<thead><tr><th>Type of event</th><th>Book at least</th><th>Ideally</th></tr></thead>
<tbody>
<tr><th>Office lunch or meeting</th><td>2 to 3 days ahead</td><td>1 week ahead</td></tr>
<tr><th>Company party or launch</th><td>1 to 2 weeks ahead</td><td>3 to 4 weeks ahead</td></tr>
<tr><th>Live kebab carving</th><td>1 to 2 weeks ahead</td><td>3 to 4 weeks ahead</td></tr>
<tr><th>Wedding or large celebration</th><td>1 to 2 months ahead</td><td>3 months or more</td></tr>
</tbody></table></div>
<p>Singapore caterers often ask for at least two days' notice for buffets, and live carving needs extra time to plan staff, equipment and the venue. These are general guides: send your date through the planner and we'll confirm what's possible.</p>
<h2>Busy seasons in Singapore</h2>
<p>Book earlier for events around these periods, when caterers fill up fast:</p>
<ul>
<li><strong>November to December:</strong> year-end parties, Christmas and team celebrations</li>
<li><strong>Chinese New Year:</strong> lo hei lunches and open houses in January or February</li>
<li><strong>Hari Raya and Deepavali:</strong> open houses and office celebrations</li>
<li><strong>Weekends and public holidays:</strong> especially for weddings and live carving</li>
</ul>
<h2>A simple planning timeline</h2>
<ol class="timeline">
<li><strong>4 to 6 weeks before:</strong> set your date, rough headcount and budget per guest. Book your caterer for big events.</li>
<li><strong>2 to 3 weeks before:</strong> choose your menu and service style: live carving, buffet or meal boxes. Check venue access, space and power.</li>
<li><strong>1 week before:</strong> collect dietary needs and confirm the serving time and delivery address.</li>
<li><strong>2 to 3 days before:</strong> confirm your final headcount and any changes.</li>
<li><strong>On the day:</strong> keep someone reachable for delivery, check the consume-by labels and serve on time.</li>
</ol>
<h2>What to have ready when you ask for a quote</h2>
<ul>
<li>Date and serving time</li>
<li>Number of guests and any dietary needs</li>
<li>Live carving, buffet or meal boxes</li>
<li>Venue address, and notes on lifts, loading bays or building rules</li>
<li>Budget per guest and whether you need an invoice or PO</li>
</ul>
<p>Our <a href="../../plan/">menu planner</a> asks for exactly these, so you can send a complete request in about a minute.</p>
""",
    "faq": [
      ("How many days in advance should I order catering in Singapore?", "For office lunches, aim for at least 2 to 3 days. For live carving and parties, 1 to 2 weeks or more. For weddings, 1 to 3 months. Book earlier in busy seasons like December and Chinese New Year."),
      ("When should I confirm the final headcount?", "Two to three days before the event is a good rule, so the caterer can prepare the right quantities."),
    ],
    "sources": [
      ("Guidelines for ordering catered meals for functions and events, Singapore Food Agency", "https://sfa.gov.sg/docs/default-source/food-retail/guidelines-for-ordering-catered-meals-for-functions-and-events.pdf"),
    ],
  },
  {
    "slug": "live-food-station-ideas",
    "title": "Live Food Station Ideas for Events in Singapore",
    "h1": "Live food station ideas for your next event",
    "desc": "Why live food stations work for office parties, launches and weddings in Singapore, how to plan one, and what your venue needs.",
    "img": "live-station",
    "card": "Why live carving work, and how to plan one well.",
    "body": """
<p>A buffet feeds people. Live carving gives them something to talk about. Watching food made in front of them gets guests mingling, and the food is as fresh as it gets.</p>
<h2>Why live carving work</h2>
<ul>
<li><strong>Freshness.</strong> Food is cooked or carved to order, so it doesn't sit in a tray.</li>
<li><strong>A natural meeting point.</strong> Queues become conversations, which helps at networking events and company parties.</li>
<li><strong>Great for photos and video.</strong> A carving station looks good on social media and in event recaps.</li>
<li><strong>Easy for mixed diets.</strong> Guests choose what goes on their plate.</li>
</ul>
<h2>Ideas for different events</h2>
<ul>
<li><strong>Office celebrations:</strong> live kebab carving with wraps, pilav and salads, plus Turkish tea.</li>
<li><strong>Product launches:</strong> a carving station near the stage keeps guests close to the action.</li>
<li><strong>Festive open houses:</strong> pair live carving with a dessert table of baklava and kunafa.</li>
<li><strong>Weddings:</strong> combine live carving with a sit-down Turkish feast for an evening guests remember.</li>
</ul>
<h2>How to plan live carving</h2>
<ol class="timeline">
<li><strong>Know your numbers.</strong> Headcount and serving window decide how many stations and chefs you need.</li>
<li><strong>Pick the spot.</strong> Somewhere guests can queue without blocking doors or the stage.</li>
<li><strong>Check the venue.</strong> Space for the station, access to power, ventilation and building rules on cooking equipment.</li>
<li><strong>Plan the flow.</strong> Put plates, sauces and drinks after the station so the queue keeps moving.</li>
<li><strong>Add sides.</strong> Salads, bread and dips on a side table let guests start while the chef carves.</li>
</ol>
<h2>Live kebab carving or buffet?</h2>
<p>You don't have to choose. Many events pair live kebab carving with a small buffet of sides and desserts. Guests get fresh carved kebab, and nobody waits long for food.</p>
<p>See what's included in our <a href="../../live-kebab-carving/">live kebab carving</a>, or start planning in the <a href="../../plan/?service=live">menu planner</a>.</p>
""",
    "faq": [
      ("What is a live food station?", "A live food station is a counter where a chef cooks or carves food to order in front of guests, instead of serving it from pre-filled trays."),
      ("What does a venue need for live kebab carving?", "Space for the station and a queue, access to power, ventilation and permission to use cooking equipment. The caterer should confirm these with you before the day."),
    ],
    "sources": [],
  },
]


def page(head_title, desc, canonical, body, schema, depth, og_img="live-station"):
    pre = "../" * depth
    hdr = HEADER.replace('href="../', f'href="{pre}').replace('src="../', f'src="{pre}')
    ftr = FOOTER.replace('href="../', f'href="{pre}').replace('src="../', f'src="{pre}')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(head_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{pre}favicon.ico" sizes="any">
<link rel="icon" href="{pre}favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(head_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{PXU(og_img, 1200)}">
<meta name="theme-color" content="#FBF8F3">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/site.css?v=20261029">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
{hdr}
<main>
{body}
</main>
{ftr}
</body>
</html>
'''


def gimg(name, pre, alt="", lazy=True, sizes="(max-width: 900px) 100vw, 33vw"):
    h = 1200 if name == "hero" else 600
    return (f'<img src="{PXU(name, 800)}" srcset="{PXU(name, 800)} 800w, {PXU(name, 1400)} 1400w" '
            f'sizes="{sizes}" width="800" height="{h}" alt="{html.escape(alt)}"' + (' loading="lazy"' if lazy else ' fetchpriority="high"') + '>')


def build_article(g):
    url = f"{SITE}/guides/{g['slug']}/"
    pre = "../../"
    faq_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in g["faq"])
    src_html = ""
    if g["sources"]:
        src_html = '<section class="sources"><h2>Sources</h2><ul>' + "".join(
            f'<li><a href="{u}" rel="noopener" target="_blank">{html.escape(t)}</a></li>' for t, u in g["sources"]) + "</ul></section>"
    more = "".join([
        f'<a class="svc" href="../{o["slug"]}/">{gimg(o["img"], pre)}<div class="b"><h3>{html.escape(o["h1"])}</h3><p>{html.escape(o["card"])}</p><span class="go">Read guide</span></div></a>'
        for o in GUIDES if o["slug"] != g["slug"]][:3])
    body = f'''
  <div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{pre}">Home</a> / <a href="../">Guides</a> / <span aria-current="page">{html.escape(g["h1"])}</span></nav></div>
  <article class="wrap article">
    <header class="art-head">
      <h1>{html.escape(g["h1"])}</h1>
      <p class="lead">{html.escape(g["desc"])}</p>
      <p class="meta">By Singapore Kebab. Updated <time datetime="{PUBLISHED}">25 October 2026</time></p>
    </header>
    <figure class="art-img">{gimg(g["img"], pre, alt="", lazy=False, sizes="(max-width: 900px) 100vw, 900px")}</figure>
    <div class="prose art-body">{g["body"]}</div>
    <aside class="ex art-cta">
      <h3>Planning an event?</h3>
      <p class="muted">Tell us your guests, date and dishes. Your request opens in WhatsApp, ready to send.</p>
      <div style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn btn-red" href="{pre}plan/">Plan my menu</a><a class="btn btn-line" href="{pre}menu/">See menu and prices</a></div>
    </aside>
    <section class="faq art-faq"><h2>Quick answers</h2>{faq_html}</section>
    {src_html}
  </article>
  <section style="padding-top:48px">
    <div class="wrap">
      <div class="sec-head"><h2>More guides</h2></div>
      <div class="related">{more}</div>
    </div>
  </section>
'''
    schema = [
      {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"], "url": url,
       "image": PXU(g['img'], 1200).replace("&amp;", "&"), "datePublished": PUBLISHED, "dateModified": PUBLISHED,
       "author": {"@type": "Organization", "name": "Singapore Kebab", "url": SITE + "/"},
       "publisher": {"@type": "Organization", "name": "Singapore Kebab", "url": SITE + "/"}},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides/"},
        {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]},
    ]
    out = os.path.join(ROOT, "guides", g["slug"])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(g["title"] + " | Singapore Kebab" if len(g["title"]) < 45 else g["title"], g["desc"], url, body, schema, 2, g["img"]))


def build_index():
    url = f"{SITE}/guides/"
    pre = "../"
    cards = "".join(
        f'<a class="svc" href="{g["slug"]}/">{gimg(g["img"], pre)}<div class="b"><h3>{html.escape(g["h1"])}</h3><p>{html.escape(g["card"])}</p><span class="go">Read guide</span></div></a>'
        for g in GUIDES)
    body = f'''
  <div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{pre}">Home</a> / <span aria-current="page">Guides</span></nav></div>
  <section class="lp-hero" style="padding-bottom:40px">
    <div class="wrap">
      <h1 style="max-width:14ch">Kebab and catering guides</h1>
      <p class="lead" style="font-size:20px;color:var(--muted);max-width:52ch;margin-top:18px">Everything about Turkish kebab, and practical tips for planning catering in Singapore: how much to order, when to book and how to run live carving.</p>
    </div>
  </section>
  <section style="padding-top:0">
    <div class="wrap"><div class="guides-grid">{cards}</div></div>
  </section>
  <section class="final">
    <div class="wrap">
      <h2>Ready to plan your menu?</h2>
      <p>Answer a few questions and get your quote on WhatsApp. No commitment.</p>
      <div class="actions"><a class="btn btn-red" href="{pre}plan/">Plan my menu</a></div>
    </div>
  </section>
'''
    schema = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Kebab and catering guides", "url": url,
              "hasPart": [{"@type": "Article", "headline": g["h1"], "url": f"{SITE}/guides/{g['slug']}/"} for g in GUIDES]}
    out = os.path.join(ROOT, "guides")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(page("Kebab and Catering Guides | Singapore Kebab",
                     "Guides to Turkish kebab and catering in Singapore: kebab history, kebab vs shawarma, how much food to order, when to book and live carving ideas.",
                     url, body, schema, 1))


def build_sitemap():
    urls = ["", "live-kebab-carving/", "office-catering/", "wedding-catering/", "menu/", "plan/", "about/", "guides/"] + [f"guides/{g['slug']}/" for g in GUIDES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{PUBLISHED}</lastmod></url>\n" for u in urls)
    xml += "</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


if __name__ == "__main__":
    for g in GUIDES:
        build_article(g)
    build_index()
    build_sitemap()
    print("built", len(GUIDES), "guides + index + sitemap")
