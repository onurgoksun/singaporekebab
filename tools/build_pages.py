"""Builds the service landing pages for singaporekebab.com.

Run:  python3 tools/build_pages.py   (from the repo root)
Edit the PAGES content below, then run again.
"""
import html, json, os

ROOT = os.path.join(os.path.dirname(__file__), "..", "docs")
SITE = "https://singaporekebab.com"
WA = "6596352294"
HALAL_A = "Yes. All our food is halal. Everything is prepared in our MUIS halal-certified kitchen in Little India, so you can serve it to all your guests with confidence."
ADDRESS = "665 Buffalo Road, Little India, Singapore 210665"
MAPS = "https://www.google.com/maps/search/?api=1&query=665+Buffalo+Road+Singapore+210665"
POSTAL = {"@type": "PostalAddress", "streetAddress": "665 Buffalo Road", "addressLocality": "Singapore",
          "postalCode": "210665", "addressCountry": "SG"}

WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm4.5 12.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.7-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>')


def img(name, alt, sizes="(max-width: 900px) 100vw, 50vw", lazy=True, h=600):
    big = 1400 if name in ("live-station", "office", "weddings") else (1024 if name == "hero" else 900)
    return (f'<img src="../images/{name}-800.webp" srcset="../images/{name}-800.webp 800w, ../images/{name}-1400.webp {big}w" '
            f'sizes="{sizes}" width="800" height="{h}" alt="{html.escape(alt)}"' + (' loading="lazy"' if lazy else ' fetchpriority="high"') + '>')


HEADER = f'''<header>
  <div class="wrap nav">
    <a class="brand" href="../" aria-label="Singapore Kebab home"><img src="../images/logo-160.webp" width="82" height="80" alt="Singapore Kebab logo"></a>
    <nav class="nav-links" aria-label="Main">
      <a href="../live-kebab-carving/">Live kebab carving</a>
      <a href="../office-catering/">Office catering</a>
      <a href="../wedding-catering/">Weddings</a>
      <a href="../menu/">Menu &amp; prices</a>
      <a href="../guides/">Guides</a>
      <a href="../about/">About</a>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-wa js-wa" href="#" data-msg="Hi Singapore Kebab, I have a question about catering.">{WA_ICON} WhatsApp</a>
      <a class="btn btn-red" href="../plan/">Plan my menu</a>
    </div>
  </div>
</header>'''

FOOTER = f'''<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="brand" href="../" aria-label="Singapore Kebab home"><img src="../images/logo-320.webp" width="163" height="160" alt="Singapore Kebab logo" loading="lazy"></a>
        <p>Halal Turkish kebab catering in Singapore: live kebab carving, office catering and weddings. Prepared in a MUIS halal-certified kitchen.</p>
      </div>
      <div><h4>Catering</h4><ul><li><a href="../live-kebab-carving/">Live kebab carving</a></li><li><a href="../office-catering/">Office catering</a></li><li><a href="../wedding-catering/">Wedding catering</a></li></ul></div>
      <div><h4>Order</h4><ul><li><a href="../plan/">Plan my menu</a></li><li><a href="../menu/">Menu and prices</a></li><li><a href="../guides/">Catering guides</a></li><li><a href="../about/">About us</a></li><li><a href="../#faq">FAQ</a></li></ul></div>
      <div><h4>Contact</h4><ul><li><a class="js-wa" href="#" data-msg="Hi Singapore Kebab, I have a question.">WhatsApp +65 9635 2294</a></li><li><a href="mailto:hello@singaporekebab.com">hello@singaporekebab.com</a></li><li><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}</a></li></ul></div>
    </div>
    <div class="foot-halal"><img src="../images/muis-halal.webp" width="64" height="64" alt="MUIS Halal Singapore logo" loading="lazy"><p>All our food is halal. Prepared in our MUIS halal-certified kitchen at 665 Buffalo Road, Singapore.</p></div>
    <p class="copy">© <span id="year"></span> Singapore Kebab</p>
  </div>
</footer>
<a class="wa-float js-wa" href="#" data-msg="Hi Singapore Kebab, I'd like a catering quote." aria-label="WhatsApp us">{WA_ICON} WhatsApp</a>
<script>
var WHATSAPP_NUMBER = "{WA}";
document.querySelectorAll("a.js-wa").forEach(function(a){{
  a.href = "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(a.getAttribute("data-msg"));
  a.target = "_blank"; a.rel = "noopener";
}});
document.getElementById("year").textContent = new Date().getFullYear();
</script>'''

PAGES = [
  {
    "slug": "live-kebab-carving",
    "service": "live",
    "title": "Live Kebab Carving Singapore | Halal Turkish Kebab Catering",
    "desc": "Book halal live kebab carving in Singapore. Our kebab master carves chicken and lamb kebab to order at your party, launch or wedding.",
    "crumb": "Live kebab carving",
    "h1": "Live kebab carving for events in Singapore",
    "lead": "A kebab master, a vertical spit and fresh bread at your venue. Every wrap and plate is carved to order in front of your guests.",
    "img": ("live-station", "Guests queuing for freshly carved kebab at an evening event in Singapore"),
    "serviceType": "Live kebab carving catering",
    "sections": [
      ("What's included", [
        "<p>Live kebab carving brings the theatre of a Turkish kebab shop to your event. Our kebab master sets up the vertical spit, carves the meat thin and builds each wrap or plate fresh, so the food is hot and the queue becomes part of the fun.</p>",
        "<ul><li>Kebab master and carving station at your venue</li><li>Chicken and lamb kebab, carved to order</li><li>Warm wraps, pita and rice pilaf</li><li>Shepherd's salad, garlic yoghurt and chilli sauce</li><li>Vegetarian falafel for guests who don't eat meat</li></ul>",
        "<p>You can add Turkish extras such as hummus, baklava, kunafa, ayran or Turkish tea to make it a full Turkish table.</p>",
      ]),
      ("Great for", [
        "<p>Company parties, product launches, open houses, birthdays, engagements, weddings and festive gatherings. Live carving works indoors at office pantries and event spaces, and outdoors on rooftops and terraces when there's shelter.</p>",
      ]),
      ("Live carving for smaller groups too", [
        "<p>Many live carving in Singapore only take large events. Tell us your guest count in the planner and we'll suggest the best format for it, from a team celebration to a large reception.</p>",
      ]),
      ("What we need at your venue", [
        "<p>We confirm the details with you before the day: the space for the station, access to power, ventilation, set-up time and serving time. Let us know about loading bays, lifts or building rules in the planner notes.</p>",
      ]),
    ],
    "faq": [
      ("How much does live kebab carving cost?", "It depends on your guest count, menu and serving time. Use the planner to pick your dishes and see an estimate at menu prices, and we'll reply with a clear quote including the station set-up."),
      ("How many guests can one kebab chef serve?", "Our kebab master carves to order, so we plan the number of stations and serving time around your guest count. Tell us your numbers and we'll recommend the right set-up."),
      ("Can you cater vegetarian guests at live carving?", "Yes. We serve falafel wraps and plates, hummus and salads alongside the kebab."),
      ("How far in advance should I book?", "As early as you can, especially for weekends and festive seasons. Send your date through the planner and we'll confirm availability."),
    ],
  },
  {
    "slug": "office-catering",
    "service": "boxes",
    "title": "Office Lunch Catering Singapore | Kebab Meal Boxes",
    "desc": "Office lunch catering in Singapore: hot Turkish kebab meal boxes and buffet trays for team lunches and meetings. Invoices and POs on request.",
    "crumb": "Office catering",
    "h1": "Office lunch catering in Singapore",
    "lead": "Hot Turkish kebab meal boxes and buffet trays for team lunches, meetings and training days, delivered at the time you set.",
    "img": ("office", "A team in a Singapore office sharing kebab meal boxes with Marina Bay in the background"),
    "serviceType": "Corporate and office catering",
    "sections": [
      ("Two easy formats", [
        "<h3>Meal boxes</h3><p>One box per person with kebab or falafel, rice pilaf or wraps, salad and sauces. Easy to hand out in meetings and trainings, with no queue and no mess.</p>",
        "<h3>Buffet trays</h3><p>Kebab, pilav, salads, bread and sauces in trays for sharing. Good for team lunches, town halls and celebrations in the pantry.</p>",
      ]),
      ("Made for admin and HR teams", [
        "<ul><li>Clear per-guest pricing in your quote</li><li>Vegetarian options and dietary labels on every order</li><li>Delivered at the time you set</li><li>Invoices and purchase orders on request</li><li>One WhatsApp chat for the whole order</li></ul>",
      ]),
      ("Popular office menus", [
        "<p>Chicken kebab over rice pilaf, kebab wraps with garlic yoghurt, falafel boxes for vegetarians, shepherd's salad and hummus. Add baklava or kunafa for a sweet finish. See every dish with photos and prices on our <a href=\"../menu/\">menu page</a>.</p>",
      ]),
      ("Want something more memorable?", [
        "<p>For team celebrations and company events, bring <a href=\"../live-kebab-carving/\">live kebab carving</a> to the office and let your team watch the kebab carved fresh.</p>",
      ]),
    ],
    "faq": [
      ("Is there a minimum order for office catering?", "We cater small team lunches as well as large company events. Tell us your number in the planner and we'll suggest the best format."),
      ("Can you deliver to my office?", "Tell us your building or postal code in the planner. We'll confirm delivery time and any delivery fee in your quote."),
      ("Do you provide invoices for companies?", "Yes. Mention that you need an invoice or a purchase order in the planner notes and we'll include the details in your quote."),
      ("Can you cater for vegetarian colleagues?", "Yes. We have falafel, hummus, salads and veggie moussaka, and every order comes with clear dietary labels."),
    ],
  },
  {
    "slug": "wedding-catering",
    "service": "live",
    "title": "Turkish Wedding Catering Singapore | Singapore Kebab",
    "desc": "Turkish wedding catering in Singapore: live kebab carving, meze, pilav, baklava, kunafa and Turkish tea for your guests and celebrations.",
    "crumb": "Wedding catering",
    "h1": "Turkish wedding catering in Singapore",
    "lead": "Live kebab carving and a full Turkish table for weddings, engagements and family celebrations.",
    "img": ("weddings", "A Turkish wedding table with baklava, Turkish tea and meze in front of Gardens by the Bay"),
    "serviceType": "Wedding and celebration catering",
    "sections": [
      ("The full Turkish table", [
        "<p>Give your guests something they'll talk about. Our kebab master carves chicken and lamb kebab live, served with warm bread, rice pilaf, meze and salads, followed by baklava, kunafa and Turkish tea.</p>",
        "<ul><li>Live kebab carving station</li><li>Iskender, meze, hummus and fresh pide</li><li>Rice pilaf and shepherd's salad</li><li>Baklava and kunafa</li><li>Turkish tea service and ayran</li></ul>",
      ]),
      ("For every kind of celebration", [
        "<p>Weddings, solemnisations, engagements, anniversaries, birthdays and family gatherings, at hotels, event venues, community spaces or at home.</p>",
      ]),
      ("Planned around your day", [
        "<p>Tell us your guest count, date, venue and dietary needs, and we'll build a menu for your budget. We'll work out the serving time and set-up with you or your planner before the day.</p>",
      ]),
    ],
    "faq": [
      ("Can we mix live carving with a buffet?", "Yes. Many couples pair live kebab carving with a buffet of meze, pilav and desserts. Tell us what you have in mind in the planner."),
      ("Can you cater for guests with dietary needs?", "Yes. Tell us about vegetarian guests, allergies and any other requirements in the planner, and we'll confirm what we can provide in your quote."),
      ("How early should we book for a wedding?", "As early as possible, especially for weekend dates. Send your date through the planner and we'll confirm availability."),
    ],
  },
]

RELATED = [
  ("live-kebab-carving", "Live kebab carving", "Carved to order at your venue.", "live-station"),
  ("office-catering", "Office catering", "Meal boxes and buffets for teams.", "office"),
  ("wedding-catering", "Wedding catering", "A full Turkish table for your day.", "weddings"),
]


def build(p):
    url = f"{SITE}/{p['slug']}/"
    p = dict(p, faq=[("Is your food halal?", HALAL_A)] + list(p["faq"]))
    faq_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in p["faq"])
    sections = ""
    for title, blocks in p["sections"]:
        sections += f'<section class="lp-sec" style="padding:0 0 48px"><div class="prose"><h2>{html.escape(title)}</h2>{"".join(blocks)}</div></section>\n'
    related = "".join(
        f'<a class="svc" href="../{s}/">{img(im, "", sizes="(max-width: 900px) 100vw, 33vw")}<div class="b"><h3>{t}</h3><p>{d}</p><span class="go">Learn more</span></div></a>'
        for s, t, d, im in RELATED if s != p["slug"])
    schema = [
      {"@context": "https://schema.org", "@type": "Service", "name": p["h1"], "serviceType": p["serviceType"],
       "description": p["desc"], "url": url, "areaServed": {"@type": "Country", "name": "Singapore"},
       "provider": {"@type": "FoodEstablishment", "name": "Singapore Kebab", "url": SITE + "/", "telephone": "+65 9635 2294", "servesCuisine": "Turkish", "address": POSTAL, "logo": SITE + "/images/logo-512.png"}},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    im, alt = p["img"]
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p["title"])}</title>
<meta name="description" content="{html.escape(p["desc"])}">
<link rel="canonical" href="{url}">
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="icon" href="../favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(p["title"])}">
<meta property="og:description" content="{html.escape(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/{im}-1400.webp">
<meta name="theme-color" content="#FBF8F3">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/site.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
{HEADER}
<main>
  <div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> / <span aria-current="page">{html.escape(p["crumb"])}</span></nav></div>
  <section class="lp-hero">
    <div class="wrap hero-grid">
      <div>
        <span class="halal-pill"><img src="../images/muis-halal.webp" width="34" height="34" alt="MUIS Halal Singapore logo">100% halal · MUIS halal-certified kitchen</span>
        <h1>{html.escape(p["h1"])}</h1>
        <p class="lead" style="font-size:20px;color:var(--muted);max-width:44ch;margin:22px 0 30px">{html.escape(p["lead"])}</p>
        <div class="actions" style="display:flex;flex-wrap:wrap;gap:12px">
          <a class="btn btn-red" href="../plan/?service={p["service"]}">Plan my menu in 60 seconds</a>
          <a class="btn btn-wa js-wa" href="#" data-msg="Hi Singapore Kebab, I'd like a quote for {html.escape(p["crumb"].lower())}.">{WA_ICON} WhatsApp us</a>
        </div>
      </div>
      <div class="hero-photo">{img(im, alt, lazy=False).replace('<img ', '<img style="aspect-ratio:4/3" ')}</div>
    </div>
  </section>
  <div class="wrap">
    <div class="split">
      <div>{sections}</div>
      <aside class="lp-aside">
        <div class="ex" style="gap:14px">
          <h3>Get your quote</h3>
          <p class="muted" style="font-size:15.5px">Tell us your guests, date, dishes and area. Your request opens in WhatsApp, ready to send.</p>
          <a class="btn btn-red" href="../plan/?service={p["service"]}">Plan my menu</a>
          <a class="btn btn-line" href="../menu/">See menu and prices</a>
        </div>
      </aside>
    </div>
  </div>
  <section id="faq" style="padding-top:24px">
    <div class="wrap">
      <div class="sec-head"><h2>Questions about {html.escape(p["crumb"].lower())}</h2></div>
      <div class="faq">{faq_html}</div>
    </div>
  </section>
  <section style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><h2>More catering options</h2></div>
      <div class="related">{related}</div>
    </div>
  </section>
  <section class="final">
    <div class="wrap">
      <h2>Ready to plan your menu?</h2>
      <p>Answer a few questions and get your quote on WhatsApp. No commitment.</p>
      <div class="actions"><a class="btn btn-red" href="../plan/?service={p["service"]}">Plan my menu</a><a class="btn btn-wa js-wa" href="#" data-msg="Hi Singapore Kebab, I'd like a catering quote.">WhatsApp us</a></div>
    </div>
  </section>
</main>
{FOOTER}
</body>
</html>
'''
    out = os.path.join(ROOT, p["slug"])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("built", p["slug"])


def build_about():
    url = f"{SITE}/about/"
    title = "About Singapore Kebab | Turkish Kebab Catering in Little India"
    desc = "Singapore Kebab is a halal Turkish kebab catering brand. Fresh kebab cooked daily in our MUIS halal-certified kitchen in Little India for offices, events and weddings across Singapore."
    schema = [
      {"@context": "https://schema.org", "@type": "AboutPage", "name": "About Singapore Kebab", "url": url, "description": desc},
      {"@context": "https://schema.org", "@type": "FoodEstablishment", "name": "Singapore Kebab", "url": SITE + "/",
       "telephone": "+65 9635 2294", "email": "hello@singaporekebab.com", "servesCuisine": "Turkish", "logo": SITE + "/images/logo-512.png", "image": SITE + "/images/logo-512.png",
       "address": POSTAL, "areaServed": {"@type": "Country", "name": "Singapore"}, "hasMap": MAPS},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "About", "item": url}]},
    ]
    values = [
      ("100% halal", "All our food is halal and prepared in our MUIS halal-certified kitchen in Little India. Every guest at your table can enjoy the same meal."),
      ("Real Turkish kebab", "Chicken and lamb kebab cooked on a vertical spit and carved to order, the way it is done in Turkey. Not generic shawarma."),
      ("Cooked fresh on the day", "Your order is prepared on the day of your event and delivered hot, or carved live at your venue."),
      ("Clear prices", "Our menu prices are on the website. The planner shows an estimate as you build your menu, so there are no surprises."),
      ("Something for every guest", "Falafel, hummus, salads and vegetarian pide sit next to the kebab, so mixed groups are covered."),
    ]
    def vcard(t, d):
        h = f'<h3>{html.escape(t)}</h3><p class="muted" style="font-size:15.5px">{html.escape(d)}</p>'
        if t == "100% halal":
            return ('<div class="ex" style="grid-column:1/-1;background:#E6F2E7;border-color:#BFDCC3;flex-direction:row;align-items:center;gap:20px">'
                    '<img src="../images/muis-halal.webp" width="96" height="96" alt="MUIS Halal Singapore logo" style="flex:none;border-radius:50%;background:#fff"><div>' + h + '</div></div>')
        return '<div class="ex">' + h + '</div>'
    vals = "".join(vcard(t, d) for t, d in values)
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="icon" href="../favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/live-station-1400.webp">
<meta name="theme-color" content="#FBF8F3">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/site.css">
<style>
.values{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
@media (max-width:700px){{.values{{grid-template-columns:1fr}}}}
.visit{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:24px;align-items:stretch}}
@media (max-width:900px){{.visit{{grid-template-columns:1fr}}}}
.map{{border:0;width:100%;min-height:340px;height:100%;border-radius:var(--r-lg);background:var(--soft)}}
.addr{{font-size:20px;font-weight:700;line-height:1.35}}
</style>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
{HEADER}
<main>
  <div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> / <span aria-current="page">About</span></nav></div>
  <section class="lp-hero">
    <div class="wrap hero-grid">
      <div>
        <span class="halal-pill"><img src="../images/muis-halal.webp" width="34" height="34" alt="MUIS Halal Singapore logo">100% halal · MUIS halal-certified kitchen</span>
        <h1>About Singapore Kebab</h1>
        <p class="lead" style="font-size:20px;color:var(--muted);max-width:44ch;margin:22px 0 30px">We bring real Turkish kebab to Singapore's office lunches, parties and weddings, cooked fresh every day in our MUIS halal-certified kitchen in Little India.</p>
        <div class="actions" style="display:flex;flex-wrap:wrap;gap:12px">
          <a class="btn btn-red" href="../plan/">Plan my menu</a>
          <a class="btn btn-wa js-wa" href="#" data-msg="Hi Singapore Kebab, I have a question.">{WA_ICON} WhatsApp us</a>
        </div>
      </div>
      <div class="hero-photo">{img("live-station", "A kebab chef carving kebab for guests at an event in Singapore", lazy=False).replace('<img ', '<img style="aspect-ratio:4/3" ')}</div>
    </div>
  </section>

  <div class="wrap">
    <section class="lp-sec" style="padding:0 0 48px"><div class="prose">
      <img src="../images/logo-320.webp" width="163" height="160" alt="Singapore Kebab logo: a smiling kebab chef next to a vertical kebab spit" loading="lazy" style="float:right;width:180px;height:auto;margin:0 0 12px 24px;shape-outside:circle(50%)">
      <h2>Our story</h2>
      <p>Singapore Kebab was started by Turks living in Singapore. We missed the kebab we grew up with: meat stacked on a vertical spit, carved thin while it is still crisp at the edges, and wrapped in fresh bread with a cool garlic yogurt sauce.</p>
      <p>Singapore already loves kebab, so we asked a simple question. Why not bring the real thing to the moments people here celebrate together, from a Friday team lunch to a product launch or a wedding?</p>
      <p>That is what we do. We cater Turkish kebab across Singapore, with live kebab carving at your venue or hot food delivered on time, ready to serve.</p>
    </div></section>

    <section class="lp-sec" style="padding:0 0 48px">
      <div class="sec-head"><h2>What we care about</h2></div>
      <div class="values">{vals}</div>
    </section>

    <section class="lp-sec" style="padding:0 0 48px"><div class="prose">
      <h2>What we cater</h2>
      <p><a href="../live-kebab-carving/">Live kebab carving</a> for parties, launches and weddings, where our chef carves to order in front of your guests. <a href="../office-catering/">Office catering</a> with buffet trays or individual meal boxes for team lunches and dinners. <a href="../wedding-catering/">Wedding catering</a> with a full Turkish table. You can also <a href="../menu/">order from our menu</a> for smaller groups.</p>
    </div></section>

    <section class="lp-sec" id="visit" style="padding:0 0 64px">
      <div class="sec-head"><h2>Our kitchen</h2></div>
      <div class="visit">
        <div class="ex" style="gap:14px">
          <p class="addr">665 Buffalo Road<br>Little India<br>Singapore 210665</p>
          <p class="muted" style="font-size:15.5px">Our kitchen is MUIS halal-certified. Your food is cooked here and sent out hot. Pickup orders are collected from this address. Message us on WhatsApp first so your order is ready when you arrive.</p>
          <a class="btn btn-line" href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a>
          <a class="btn btn-wa js-wa" href="#" data-msg="Hi Singapore Kebab, I'd like to arrange a pickup.">{WA_ICON} WhatsApp +65 9635 2294</a>
          <a class="btn btn-line" href="mailto:hello@singaporekebab.com">hello@singaporekebab.com</a>
        </div>
        <iframe class="map" title="Map of our kitchen at 665 Buffalo Road, Singapore" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=665+Buffalo+Road,+Singapore+210665&amp;output=embed"></iframe>
      </div>
    </section>
  </div>

  <section class="final">
    <div class="wrap">
      <h2>Ready to plan your menu?</h2>
      <p>Answer a few questions and get your quote on WhatsApp. No commitment.</p>
      <div class="actions"><a class="btn btn-red" href="../plan/">Plan my menu</a><a class="btn btn-wa js-wa" href="#" data-msg="Hi Singapore Kebab, I'd like a catering quote.">WhatsApp us</a></div>
    </div>
  </section>
</main>
{FOOTER}
</body>
</html>
'''
    out = os.path.join(ROOT, "about")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("built about")


if __name__ == "__main__" and True:
    for p in PAGES:
        build(p)
    build_about()
