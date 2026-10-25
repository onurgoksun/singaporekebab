"""Builds docs/assets/nutrition.js: ingredients, estimated nutrition and allergens
for every dish and option on the menu.

Nutrition is calculated from typical recipe weights (grams per portion) and
standard reference values per 100 g (USDA FoodData Central style figures for
cooked / prepared foods). These are estimates, not lab results. When the
kitchen weighs real portions, update the grams in RECIPES and rebuild.

Run: python3 tools/build_nutrition.py
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets" / "nutrition.js"

# name: (kcal, protein, carbs, sugars, fat, saturated fat, fibre, salt)  per 100 g
# allergens: list of allergen keys
ING = {
  "Chicken kebab meat":      ((190, 24.0, 2.0, 1.0, 10.0, 2.8, 0.0, 1.2), []),
  "Lamb kebab meat":         ((240, 22.0, 1.0, 0.5, 16.5, 7.5, 0.0, 1.2), []),
  "Minced chicken kebab":    ((190, 23.0, 1.0, 0.5, 10.5, 3.0, 0.0, 0.9), []),
  "Minced lamb kebab":       ((280, 24.0, 1.0, 0.5, 20.0, 8.5, 0.0, 1.0), []),
  "Lamb cubes (kuşbaşı)":    ((215, 27.0, 0.0, 0.0, 11.5, 4.8, 0.0, 0.8), []),
  "Lamb köfte":              ((250, 19.0, 6.0, 1.5, 17.0, 7.0, 0.5, 1.1), ["gluten", "egg"]),
  "Falafel":                 ((333, 13.3, 31.8, 2.0, 17.8, 2.4, 4.9, 0.75), []),
  "Chicken nuggets":         ((296, 15.0, 16.0, 0.5, 19.0, 3.3, 1.0, 1.2), ["gluten"]),
  "Sucuk (beef sausage)":    ((450, 20.0, 2.0, 0.5, 40.0, 15.0, 0.0, 3.5), []),
  "Egg":                     ((143, 12.6, 0.7, 0.4, 9.5, 3.1, 0.0, 0.35), ["egg"]),
  "Lavash wrap":             ((300, 8.0, 50.0, 2.0, 7.0, 2.5, 2.5, 1.1), ["gluten"]),
  "Pita bread":              ((275, 9.1, 55.7, 1.3, 1.2, 0.2, 2.2, 1.3), ["gluten"]),
  "Tombik bread":            ((280, 9.0, 54.0, 2.0, 2.5, 0.4, 2.3, 1.2), ["gluten", "sesame"]),
  "Pide dough":              ((270, 8.5, 52.0, 2.0, 3.0, 0.5, 2.3, 1.2), ["gluten"]),
  "Rice pilaf":              ((150, 2.8, 27.0, 0.3, 3.3, 1.5, 0.4, 0.5), ["milk"]),
  "Biryani rice":            ((175, 3.2, 28.0, 1.0, 5.5, 2.8, 0.8, 0.7), ["milk"]),
  "Pasta (cooked)":          ((158, 5.8, 31.0, 0.6, 0.9, 0.2, 1.8, 0.3), ["gluten"]),
  "Fries":                   ((312, 3.4, 41.0, 0.3, 15.0, 2.3, 3.8, 0.5), []),
  "Potato":                  ((87, 1.9, 20.0, 0.9, 0.1, 0.0, 1.8, 0.0), []),
  "Lettuce":                 ((15, 1.4, 2.9, 0.8, 0.2, 0.0, 1.3, 0.0), []),
  "Tomato":                  ((18, 0.9, 3.9, 2.6, 0.2, 0.0, 1.2, 0.0), []),
  "Cucumber":                ((15, 0.7, 3.6, 1.7, 0.1, 0.0, 0.5, 0.0), []),
  "Red onion":               ((40, 1.1, 9.3, 4.2, 0.1, 0.0, 1.7, 0.0), []),
  "Red cabbage":             ((31, 1.4, 7.4, 3.8, 0.2, 0.0, 2.1, 0.0), []),
  "Green pepper":            ((20, 0.9, 4.6, 2.4, 0.2, 0.0, 1.7, 0.0), []),
  "Spinach":                 ((23, 2.9, 3.6, 0.4, 0.4, 0.1, 2.2, 0.2), []),
  "Eggplant":                ((35, 0.8, 8.7, 3.2, 0.2, 0.0, 2.5, 0.0), []),
  "Zucchini":                ((17, 1.2, 3.1, 2.5, 0.3, 0.1, 1.0, 0.0), []),
  "Mushrooms":               ((22, 3.1, 3.3, 2.0, 0.3, 0.0, 1.0, 0.0), []),
  "Fried onion":             ((300, 3.0, 35.0, 15.0, 16.0, 2.0, 3.5, 0.3), []),
  "Garlic yogurt sauce":     ((110, 3.0, 5.0, 4.0, 8.5, 2.5, 0.0, 0.6), ["milk", "egg"]),
  "Chilli sauce":            ((30, 1.0, 6.0, 4.0, 0.3, 0.0, 1.0, 1.0), []),
  "Tomato sauce":            ((50, 1.2, 7.0, 5.0, 2.0, 0.3, 1.2, 0.8), []),
  "Ketchup":                 ((101, 1.0, 27.0, 22.0, 0.1, 0.0, 0.3, 2.3), []),
  "Yogurt":                  ((61, 3.5, 4.7, 4.7, 3.3, 2.1, 0.0, 0.1), ["milk"]),
  "Strained yogurt":         ((97, 9.0, 3.9, 3.6, 5.0, 3.3, 0.0, 0.1), ["milk"]),
  "Butter":                  ((717, 0.9, 0.1, 0.1, 81.0, 51.0, 0.0, 0.6), ["milk"]),
  "Garlic butter":           ((650, 1.0, 3.0, 0.3, 72.0, 46.0, 0.2, 0.8), ["milk"]),
  "Olive oil":               ((884, 0.0, 0.0, 0.0, 100.0, 14.0, 0.0, 0.0), []),
  "Lemon juice":             ((22, 0.4, 6.9, 2.5, 0.2, 0.0, 0.3, 0.0), []),
  "Kaşar cheese":            ((350, 25.0, 1.5, 0.5, 27.0, 17.0, 0.0, 1.7), ["milk"]),
  "Cooking cream":           ((200, 2.7, 3.5, 3.5, 20.0, 12.5, 0.0, 0.1), ["milk"]),
  "Béchamel sauce":          ((130, 4.0, 9.0, 4.0, 9.0, 5.0, 0.2, 0.6), ["milk", "gluten"]),
  "Hummus":                  ((166, 7.9, 14.3, 0.3, 9.6, 1.4, 6.0, 0.95), ["sesame"]),
  "Tahini sauce":            ((250, 7.0, 8.0, 0.5, 22.0, 3.0, 3.0, 0.7), ["sesame"]),
  "Pesto":                   ((450, 5.0, 5.0, 1.0, 45.0, 7.0, 1.5, 2.0), ["nuts", "milk"]),
  "Baklava":                 ((430, 6.5, 45.0, 28.0, 25.0, 8.0, 2.0, 0.3), ["gluten", "nuts", "milk"]),
  "Kunafa":                  ((370, 7.0, 45.0, 25.0, 18.0, 10.0, 0.8, 0.5), ["gluten", "milk", "nuts"]),
  "Ayran":                   ((37, 1.7, 2.4, 2.4, 2.0, 1.3, 0.0, 0.5), ["milk"]),
  "Turkish tea (no sugar)":  ((1, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0), []),
}

C, L = "Chicken kebab meat", "Lamb kebab meat"

def meat(kind, g, chicken=C, lamb=L):
    if kind == "Chicken": return [(chicken, g)]
    if kind == "Lamb": return [(lamb, g)]
    return [(chicken, g // 2), (lamb, g - g // 2)]  # Mix

def by_meat(base, g, chicken=C, lamb=L, extra_first=None):
    return {k: meat(k, g, chicken, lamb) + base for k in ("Chicken", "Lamb", "Mix")}

WRAP_SALAD = [("Lettuce", 25), ("Tomato", 30), ("Red onion", 15), ("Red cabbage", 15)]
SAUCES = [("Garlic yogurt sauce", 30), ("Chilli sauce", 10)]

R = {}  # dish id -> {"desc", "opts": {option name: [(ingredient, grams)]}}
def dish(i, desc, opts): R[i] = {"desc": desc, "opts": opts}

dish("wrap", "Sliced kebab rolled in a soft lavash with fresh salad, garlic yogurt sauce and chilli sauce.",
     by_meat([("Lavash wrap", 90)] + WRAP_SALAD + SAUCES, 100))
dish("tombik", "A round, puffy Turkish bread stuffed with kebab, salad and sauces.",
     by_meat([("Tombik bread", 110)] + WRAP_SALAD + SAUCES, 110))
dish("falafel", "Crispy chickpea and herb falafel with hummus, salad and tahini sauce.", {
  "Wrap":  [("Falafel", 120), ("Lavash wrap", 90), ("Hummus", 30), ("Lettuce", 25), ("Tomato", 30), ("Cucumber", 20), ("Tahini sauce", 25)],
  "Pita":  [("Falafel", 120), ("Pita bread", 110), ("Hummus", 30), ("Lettuce", 25), ("Tomato", 30), ("Cucumber", 20), ("Tahini sauce", 25)],
  "Plate": [("Falafel", 150), ("Hummus", 80), ("Lettuce", 60), ("Tomato", 40), ("Cucumber", 40), ("Pita bread", 60), ("Tahini sauce", 30)],
})
chips = by_meat([("Fries", 150), ("Lettuce", 20), ("Tomato", 20)] + SAUCES, 120)
chips = {"Just fries": [("Fries", 180), ("Ketchup", 20)], **chips}
dish("chips", "Kebab served over crispy fries with salad, garlic yogurt sauce and chilli sauce.", chips)
dish("fries", "Golden fries, lightly salted.", {"Regular": [("Fries", 180), ("Ketchup", 20)]})
dish("iskender", "Kebab over toasted pita cubes, topped with tomato sauce and hot butter, with yogurt on the side.",
     by_meat([("Pita bread", 80), ("Tomato sauce", 60), ("Butter", 12), ("Yogurt", 100)], 150))
dish("ricekebab", "Kebab on buttery rice pilaf with fresh salad and sauces.",
     by_meat([("Rice pilaf", 200), ("Lettuce", 30), ("Tomato", 40), ("Cucumber", 30)] + SAUCES, 130))
dish("beyti", "Grilled minced kebab wrapped in lavash, sliced, with tomato sauce, butter and yogurt.",
     by_meat([("Lavash wrap", 70), ("Tomato sauce", 50), ("Butter", 10), ("Yogurt", 80)], 150, "Minced chicken kebab", "Minced lamb kebab"))
dish("alinazik", "Smoky eggplant mashed with garlic yogurt, topped with kebab and warm butter.",
     by_meat([("Eggplant", 150), ("Strained yogurt", 90), ("Butter", 10), ("Olive oil", 5)], 130))
dish("kofte", "Grilled lamb meatballs with rice pilaf, grilled tomato, pepper and onion.",
     {"Regular": [("Lamb köfte", 180), ("Rice pilaf", 180), ("Tomato", 60), ("Green pepper", 20), ("Red onion", 20), ("Lettuce", 20)]})
dish("biryani", "Spiced basmati rice cooked with meat, topped with fried onions, with yogurt on the side.", {
  "Chicken": [("Biryani rice", 250), (C, 130), ("Fried onion", 15), ("Yogurt", 50)],
  "Lamb":    [("Biryani rice", 250), (L, 130), ("Fried onion", 15), ("Yogurt", 50)],
})
PB = [("Pide dough", 220), ("Butter", 10)]
dish("pide", "Turkish flatbread boat baked in the oven with your choice of topping.", {
  "Cheese":             PB + [("Kaşar cheese", 110)],
  "Spinach":            PB + [("Spinach", 120), ("Red onion", 30), ("Kaşar cheese", 50), ("Olive oil", 8)],
  "Sucuk / pepperoni":  PB + [("Sucuk (beef sausage)", 80), ("Tomato", 30), ("Green pepper", 20)],
  "Chicken":            PB + [(C, 120), ("Tomato", 30), ("Green pepper", 20), ("Red onion", 20)],
  "Lamb":               PB + [("Lamb cubes (kuşbaşı)", 130), ("Tomato", 30), ("Green pepper", 20), ("Red onion", 20)],
  "Mix":                PB + [(C, 70), ("Lamb cubes (kuşbaşı)", 70), ("Tomato", 30), ("Green pepper", 20)],
  "Sucuk & cheese":     PB + [("Sucuk (beef sausage)", 60), ("Kaşar cheese", 80)],
  "Egg, sucuk & cheese": PB + [("Egg", 50), ("Sucuk (beef sausage)", 50), ("Kaşar cheese", 70)],
  "Egg, lamb & cheese": PB + [("Egg", 50), ("Lamb cubes (kuşbaşı)", 90), ("Kaşar cheese", 60)],
})
dish("bread", "Warm Turkish pita, plain, with garlic butter or with melted cheese.", {
  "Plain pita": [("Pita bread", 110)],
  "Garlic":     [("Pita bread", 110), ("Garlic butter", 15)],
  "Cheese":     [("Pita bread", 110), ("Kaşar cheese", 50)],
})
MB = [("Eggplant", 120), ("Tomato sauce", 60), ("Béchamel sauce", 80), ("Olive oil", 12), ("Kaşar cheese", 15)]
dish("moussaka", "Layers of eggplant and potato in tomato sauce, topped with béchamel and baked.", {
  "Veggie":  [("Eggplant", 120), ("Potato", 80), ("Zucchini", 50), ("Tomato sauce", 60), ("Béchamel sauce", 80), ("Olive oil", 15), ("Kaşar cheese", 15)],
  "Chicken": [("Minced chicken kebab", 100), ("Potato", 60)] + MB,
  "Lamb":    [("Minced lamb kebab", 100), ("Potato", 60)] + MB,
  "Mix":     [("Minced chicken kebab", 50), ("Minced lamb kebab", 50), ("Potato", 60)] + MB,
})
dish("bakedpasta", "Pasta baked with kebab, creamy tomato sauce and melted cheese.",
     by_meat([("Pasta (cooked)", 200), ("Cooking cream", 50), ("Tomato sauce", 40), ("Kaşar cheese", 40)], 100))
dish("bakedrice", "Rice pilaf baked with kebab, mushrooms, cream and melted cheese.",
     by_meat([("Rice pilaf", 220), ("Mushrooms", 30), ("Cooking cream", 40), ("Kaşar cheese", 40)], 110))
BC = [("Mushrooms", 180), ("Kaşar cheese", 70), ("Cooking cream", 60), ("Butter", 10), ("Pita bread", 50)]
bc = by_meat(BC, 90); bc = {"No meat": BC, **bc}
dish("bakedcheese", "Mushrooms baked in cream under melted cheese, served with bread.", bc)
SAL = [("Lettuce", 80), ("Tomato", 60), ("Cucumber", 60), ("Red onion", 20), ("Red cabbage", 30), ("Olive oil", 12), ("Lemon juice", 10)]
s = by_meat(SAL, 100); s = {"No meat": SAL, **s}
dish("salad", "Fresh mixed salad with olive oil and lemon dressing.", s)
HU = [("Hummus", 150), ("Olive oil", 8), ("Pita bread", 100)]
h = by_meat(HU, 100); h = {"Just hummus": HU, **h}
dish("hummus", "Creamy chickpea and tahini hummus with olive oil and warm bread.", h)
PE = [("Pasta (cooked)", 220), ("Pesto", 40), ("Kaşar cheese", 10)]
p = by_meat(PE, 100); p = {"Just pasta": PE, **p}
dish("pesto", "Pasta tossed in basil pesto with a little cheese.", p)
dish("nuggets", "Crispy chicken nuggets with fries and ketchup.", {"Regular": [("Chicken nuggets", 120), ("Fries", 130), ("Ketchup", 20)]})
dish("baklava", "Thin layers of pastry with chopped nuts, baked in butter and finished with syrup.", {"Regular": [("Baklava", 100)]})
dish("kunafa", "Shredded pastry with melted cheese inside, baked and soaked in syrup, topped with pistachio.", {"Regular": [("Kunafa", 150)]})
dish("drinks", "Drinks to go with your meal.", {
  "Ayran": [("Ayran", 250)],
  "Turkish tea": [("Turkish tea (no sugar)", 100)],
  "Soft drinks": [],
})

NOTE = {
  ("drinks", "Soft drinks"): "Nutrition depends on the brand and size. It is printed on the can or bottle.",
  ("drinks", "Turkish tea"): "Served without sugar. Each sugar cube adds about 10 kcal.",
}

def calc(items):
    tot = [0.0] * 8; al = set(); w = 0
    for name, g in items:
        vals, alg = ING[name]
        w += g
        for k in range(8): tot[k] += vals[k] * g / 100
        al.update(alg)
    return w, tot, al

def rnd(v):
    return [round(v[0])] + [round(x, 1) for x in v[1:]]

data = {}
for did, d in R.items():
    opts = {}
    for oname, items in d["opts"].items():
        w, tot, al = calc(items)
        e = {"w": w, "ing": [[n, g] for n, g in items]}
        if w:
            e["n"] = rnd(tot)
            e["h"] = rnd([x * 100 / w for x in tot])
            e["al"] = sorted(al)
        if (did, oname) in NOTE: e["note"] = NOTE[(did, oname)]
        opts[oname] = e
    data[did] = {"d": d["desc"], "o": opts}

JS = r"""/* Ingredients, estimated nutrition and allergens. Generated by tools/build_nutrition.py — do not edit by hand. */
(function(){
var D = __DATA__;
var AL = {gluten:"Gluten (wheat)", milk:"Milk", egg:"Egg", sesame:"Sesame", nuts:"Nuts"};
function norm(s){ return String(s).replace(/\s*\(.*?\)/g, "").trim(); }
function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); }
var css = ".nu-dlg{border:0;padding:0;border-radius:20px;width:min(560px,calc(100% - 24px));max-height:calc(100vh - 32px);background:#fff;color:#1F1B17;box-shadow:0 24px 60px rgba(0,0,0,.3)}"
 + ".nu-dlg::backdrop{background:rgba(28,26,24,.55)}"
 + ".nu-in{padding:22px 22px 20px;font:400 15px/1.5 Figtree,system-ui,sans-serif}"
 + ".nu-h{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}"
 + ".nu-h h3{font-family:Archivo,sans-serif;font-stretch:62%;font-weight:900;text-transform:uppercase;font-size:32px;line-height:.95}"
 + ".nu-x{width:38px;height:38px;border-radius:50%;border:1.5px solid #D8CDBE;font-size:20px;line-height:1;flex:none;background:none;cursor:pointer;color:inherit}"
 + ".nu-d{color:#655A50;margin:8px 0 14px}"
 + ".nu-tabs{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}"
 + ".nu-tabs button{border:1.5px solid #D8CDBE;border-radius:999px;padding:6px 12px;font:600 13.5px Figtree,sans-serif;background:none;cursor:pointer;color:inherit}"
 + ".nu-tabs button[aria-pressed=true]{background:#D9893A;border-color:#D9893A;color:#1F1B17}"
 + ".nu-k{font-weight:700;font-size:14px;margin:14px 0 6px;text-transform:uppercase;letter-spacing:.04em;color:#655A50}"
 + ".nu-t{width:100%;border-collapse:collapse;font-size:14.5px}"
 + ".nu-t th,.nu-t td{padding:6px 0;border-bottom:1px solid #EFE7DC;text-align:left}"
 + ".nu-t td:not(:first-child),.nu-t th:not(:first-child){text-align:right;font-variant-numeric:tabular-nums;padding-left:12px}"
 + ".nu-t th{font-size:12.5px;color:#655A50;font-weight:600}"
 + ".nu-t .sub td:first-child{padding-left:14px;color:#655A50}"
 + ".nu-t .kc td{font-weight:800;font-size:16px}"
 + ".nu-al{background:#FFF4E6;border:1px solid #F0D2AE;border-radius:10px;padding:8px 12px;font-size:14px}"
 + ".nu-f{font-size:12.5px;color:#655A50;margin-top:12px}"
 + ".nu-link{background:none;border:0;padding:0;font:600 13.5px Figtree,sans-serif;color:#A85A14;text-decoration:underline;text-underline-offset:2px;cursor:pointer}";
var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
var dlg = document.createElement("dialog"); dlg.className = "nu-dlg"; dlg.setAttribute("aria-labelledby", "nuTitle");
document.body.appendChild(dlg);
dlg.addEventListener("click", function(e){ if (e.target === dlg) dlg.close(); });
var curId, curName, curOpt;
function fmt(v, u){ return (u ? v.toFixed(1) : String(v)) + (u || ""); }
function body(){
  var d = D[curId], e = d.o[curOpt], names = Object.keys(d.o), h = "";
  h += '<div class="nu-in"><div class="nu-h"><h3 id="nuTitle">' + esc(curName) + '</h3><button type="button" class="nu-x" aria-label="Close" data-x>&times;</button></div>';
  h += '<p class="nu-d">' + esc(d.d) + '</p>';
  if (names.length > 1) h += '<div class="nu-tabs" role="group" aria-label="Option">' + names.map(function(n){ return '<button type="button" data-o="' + esc(n) + '" aria-pressed="' + (n === curOpt) + '">' + esc(n) + '</button>'; }).join("") + '</div>';
  if (e.ing.length){
    h += '<p class="nu-k">Ingredients</p><table class="nu-t"><tbody>' + e.ing.map(function(r){ return '<tr><td>' + esc(r[0]) + '</td><td>' + r[1] + ' g</td></tr>'; }).join("") + '<tr><td><b>Portion</b></td><td><b>about ' + e.w + ' g</b></td></tr></tbody></table>';
  }
  if (e.n){
    var n = e.n, p = e.h;
    h += '<p class="nu-k">Nutrition (estimated)</p><table class="nu-t"><thead><tr><th></th><th>Per portion</th><th>Per 100 g</th></tr></thead><tbody>'
      + '<tr class="kc"><td>Energy</td><td>' + n[0] + ' kcal</td><td>' + p[0] + ' kcal</td></tr>'
      + '<tr><td>Protein</td><td>' + fmt(n[1], " g") + '</td><td>' + fmt(p[1], " g") + '</td></tr>'
      + '<tr><td>Carbohydrate</td><td>' + fmt(n[2], " g") + '</td><td>' + fmt(p[2], " g") + '</td></tr>'
      + '<tr class="sub"><td>of which sugars</td><td>' + fmt(n[3], " g") + '</td><td>' + fmt(p[3], " g") + '</td></tr>'
      + '<tr><td>Fat</td><td>' + fmt(n[4], " g") + '</td><td>' + fmt(p[4], " g") + '</td></tr>'
      + '<tr class="sub"><td>of which saturated</td><td>' + fmt(n[5], " g") + '</td><td>' + fmt(p[5], " g") + '</td></tr>'
      + '<tr><td>Fibre</td><td>' + fmt(n[6], " g") + '</td><td>' + fmt(p[6], " g") + '</td></tr>'
      + '<tr><td>Salt</td><td>' + fmt(n[7], " g") + '</td><td>' + fmt(p[7], " g") + '</td></tr></tbody></table>';
    h += '<p class="nu-k">Allergens</p><p class="nu-al">' + (e.al.length ? "Contains: " + e.al.map(function(a){ return AL[a]; }).join(", ") + "." : "No major allergens in this recipe.") + '</p>';
  }
  if (e.note) h += '<p class="nu-f" style="font-size:14px;color:#1F1B17">' + esc(e.note) + '</p>';
  h += '<p class="nu-f">Values are estimates calculated from our typical recipe and portion weights, and can vary from portion to portion. Our kitchen also handles gluten, milk, egg, sesame, nuts and soy, so traces are possible. If you have an allergy, tell us before you order.</p></div>';
  dlg.innerHTML = h;
  dlg.querySelector("[data-x]").onclick = function(){ dlg.close(); };
  dlg.querySelectorAll("[data-o]").forEach(function(b){ b.onclick = function(){ curOpt = b.dataset.o; body(); }; });
}
window.SKNutri = {
  has: function(id){ return !!D[id]; },
  open: function(id, name, opt){
    if (!D[id]) return;
    curId = id; curName = name; var names = Object.keys(D[id].o);
    curOpt = names.indexOf(norm(opt || "")) > -1 ? norm(opt) : names[0];
    body();
    if (!dlg.open) dlg.showModal();
  }
};
})();
"""
OUT.write_text(JS.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":"))))
print("wrote", OUT, OUT.stat().st_size, "bytes")
for did in ("wrap", "iskender", "pide", "falafel", "baklava"):
    for o, e in list(data[did]["o"].items())[:3]:
        print(did, o, e.get("w"), e.get("n"), e.get("al"))
