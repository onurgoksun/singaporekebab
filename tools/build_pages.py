"""Builds the service landing pages for singaporekebab.com.

Run:  python3 tools/build_pages.py   (from the repo root)
Edit the PAGES content below, then run again.
"""
import html, json, os

ROOT = os.path.join(os.path.dirname(__file__), "..", "docs")
SITE = "https://singaporekebab.com"
WA = "6596352294"

WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm4.5 12.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.7-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>')


def img(name, alt, sizes="(max-width: 900px) 100vw, 50vw", lazy=True, h=600):
    big = 1400 if name in ("live-station", "office", "weddings") else (1024 if name == "hero" else 900)
    return (f'<img src="../images/{name}-800.webp" srcset="../images/{name}-800.webp 800w, ../images/{name}-1400.webp {big}w" '
            f'sizes="{sizes}" width="800" height="{h}" alt="{html.escape(alt)}"' + (' loading="lazy"' if lazy else ' fetchpriority="high"') + '>')


HEADER = f'''<header>
  <div class="wrap nav">
    <a class="brand" href="../">Singapore Kebab</a>
    <nav class="nav-links" aria-label="Main">
      <a href="../live-kebab-station/">Live kebab station</a>
      <a href="../office-catering/">Office catering</a>
      <a href="../wedding-catering/">Weddings</a>
      <a href="../menu/">Menu &amp; prices</a>
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
        <a class="brand" href="../">Singapore Kebab</a>
        <p>Turkish kebab catering in Singapore: live kebab stations, office catering and weddings.</p>
      </div>
      <div><h4>Catering</h4><ul><li><a href="../live-kebab-station/">Live kebab station</a></li><li><a href="../office-catering/">Office catering</a></li><li><a href="../wedding-catering/">Wedding catering</a></li></ul></div>
      <div><h4>Order</h4><ul><li><a href="../plan/">Plan my menu</a></li><li><a href="../menu/">Menu and prices</a></li><li><a href="../#faq">FAQ</a></li></ul></div>
      <div><h4>Contact</h4><ul><li><a class="js-wa" href="#" data-msg="Hi Singapore Kebab, I have a question.">WhatsApp +65 9635 2294</a></li></ul></div>
    </div>
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
    "slug": "live-kebab-station",
    "service": "live",
    "title": "Live Kebab Station Singapore | Turkish Kebab Catering",
    "desc": "Hire a live Turkish kebab station in Singapore. Our kebab master carves chicken and lamb kebab to order at your party, launch or wedding.",
    "crumb": "Live kebab station",
    "h1": "Live kebab station catering in Singapore",
    "lead": "A kebab master, a vertical spit and fresh bread at your venue. Every wrap and plate is carved to order in front of your guests.",
    "img": ("live-station", "Guests queuing at a live kebab station at an evening event in Singapore"),
    "serviceType": "Live kebab station catering",
    "sections": [
      ("What's included", [
        "<p>A live kebab station brings the theatre of a Turkish kebab shop to your event. Our kebab master sets up the vertical spit, carves the meat thin and builds each wrap or plate fresh, so the food is hot and the queue becomes part of the fun.</p>",
        "<ul><li>Kebab master and carving station at your venue</li><li>Chicken and lamb kebab, carved to order</li><li>Warm wraps, pita and rice pilaf</li><li>Shepherd's salad, garlic yoghurt and chilli sauce</li><li>Vegetarian falafel for guests who don't eat meat</li></ul>",
        "<p>You can add Turkish extras such as hummus, baklava, kunafa, ayran or Turkish tea to make it a full Turkish table.</p>",
      ]),
      ("Great for", [
        "<p>Company parties, product launches, open houses, birthdays, engagements, weddings and festive gatherings. A live station works indoors at office pantries and event spaces, and outdoors on rooftops and terraces when there's shelter.</p>",
      ]),
      ("Live stations for smaller groups too", [
        "<p>Many live stations in Singapore only take large events. Tell us your guest count in the planner and we'll suggest the best format for it, from a team celebration to a large reception.</p>",
      ]),
      ("What we need at your venue", [
        "<p>We confirm the details with you before the day: the space for the station, access to power, ventilation, set-up time and serving time. Let us know about loading bays, lifts or building rules in the planner notes.</p>",
      ]),
    ],
    "faq": [
      ("How much does a live kebab station cost?", "It depends on your guest count, menu and serving time. Use the planner to tell us your numbers and budget per guest, and we'll reply with a clear per-guest price."),
      ("How many guests can a live station serve?", "Our kebab master carves to order, so we plan the number of stations and serving time around your guest count. Tell us your numbers and we'll recommend the right set-up."),
      ("Can you cater vegetarian guests at a live station?", "Yes. We serve falafel wraps and plates, hummus and salads alongside the kebab."),
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
        "<p>For team celebrations and company events, bring a <a href=\"../live-kebab-station/\">live kebab station</a> to the office and let your team watch the kebab carved fresh.</p>",
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
    "desc": "Turkish wedding catering in Singapore: a live kebab station, meze, pilav, baklava, kunafa and Turkish tea for your guests and celebrations.",
    "crumb": "Wedding catering",
    "h1": "Turkish wedding catering in Singapore",
    "lead": "A live kebab station and a full Turkish table for weddings, engagements and family celebrations.",
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
      ("Can we mix a live station with a buffet?", "Yes. Many couples pair a live kebab station with a buffet of meze, pilav and desserts. Tell us what you have in mind in the planner."),
      ("Can you cater for guests with dietary needs?", "Yes. Tell us about vegetarian guests, allergies and any other requirements in the planner, and we'll confirm what we can provide in your quote."),
      ("How early should we book for a wedding?", "As early as possible, especially for weekend dates. Send your date through the planner and we'll confirm availability."),
    ],
  },
]

RELATED = [
  ("live-kebab-station", "Live kebab station", "Carved to order at your venue.", "live-station"),
  ("office-catering", "Office catering", "Meal boxes and buffets for teams.", "office"),
  ("wedding-catering", "Wedding catering", "A full Turkish table for your day.", "weddings"),
]


def build(p):
    url = f"{SITE}/{p['slug']}/"
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
       "provider": {"@type": "FoodEstablishment", "name": "Singapore Kebab", "url": SITE + "/", "telephone": "+65 9635 2294", "servesCuisine": "Turkish"}},
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
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
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


if __name__ == "__main__":
    for p in PAGES:
        build(p)
