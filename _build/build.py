"""Builds index.html (Greek, default) and en/index.html (English) from _build/source.html.
Edit design/English text in _build/source.html, Greek text in the EL list below, then run:
    python _build/build.py
"""
import os, sys, urllib.parse

# Set this once the domain is ready, e.g. "https://www.jordanangelov.com" (no trailing slash).
# Leave empty to build without domain-specific files and tags.
SITE_URL = "https://jordanangelov.com"

# GoatCounter analytics: your site code, e.g. "jordanangelov" for jordanangelov.goatcounter.com.
# Leave empty to build without analytics.
GOATCOUNTER_CODE = "jordana96"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "_build", "source.html"), encoding="utf-8").read()


def sub(text, pairs, label):
    for old, new in pairs:
        if old not in text:
            sys.exit(f"[{label}] text not found: {old[:70]!r}")
        text = text.replace(old, new)
    return text


LANG_CSS = (
    "    .lang { font-size: 12px; font-weight: 600; letter-spacing: .12em; color: #a39a8f; padding: 6px 2px; border-bottom: 1px solid transparent; }\n"
    "    .nav a.lang:hover { color: var(--gold); border-color: var(--gold); }\n"
)

# ---- shared changes: fonts with Greek support, language switch styling ----
COMMON = [
    ("family=Cormorant+Garamond:wght@400;500;600&family=Montserrat:wght@300;400;500;600;700",
     "family=EB+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Manrope:wght@300;400;500;600;700&family=Montserrat:wght@300;500"),
    ("font-family: Montserrat, system-ui, sans-serif;", "font-family: Manrope, system-ui, sans-serif;"),
    ("font-family: Montserrat, sans-serif;", "font-family: Manrope, sans-serif;"),
    (".wm { display: flex;", ".wm { font-family: Montserrat, sans-serif; display: flex;"),
    ("    .nav-cta {", LANG_CSS + "    .nav-cta {"),
    (".nav a:not(.nav-cta) { display: none; }", ".nav a:not(.nav-cta):not(.lang) { display: none; }\n      .nav { gap: 16px; }"),
]
base = sub(src, COMMON, "common").replace("'Cormorant Garamond'", "'EB Garamond'")

# ---- English: /en/ ----
EN = [
    ('<a href="#contact" class="nav-cta">',
     '<a href="../" class="lang" lang="el" hreflang="el" title="Ελληνικά">ΕΛ</a>\n        <a href="#contact" class="nav-cta">'),
    ('src="assets/', 'src="../assets/'),
]

# ---- Greek: / ----
EL = [
    ('<html lang="en">', '<html lang="el">'),
    ('content="Jordan Angelov, Insurance Advisor in Cyprus. Personal guidance on life, health, motor, home and business insurance."',
     'content="Jordan Angelov, Ασφαλιστικός Σύμβουλος στην Κύπρο. Προσωπική καθοδήγηση για ασφάλειες ζωής, υγείας, οχημάτων, κατοικίας και επιχειρήσεων."'),
    ("<title>Jordan Angelov | Insurance Advisor in Cyprus</title>", "<title>Jordan Angelov | Ασφαλιστικός Σύμβουλος στην Κύπρο</title>"),
    ('aria-label="Jordan Angelov, home"', 'aria-label="Jordan Angelov, αρχική σελίδα"'),
    ('aria-label="Main navigation"', 'aria-label="Κύρια πλοήγηση"'),
    ('<a href="#services">Services</a>', '<a href="#services">Υπηρεσίες</a>'),
    ('<a href="#process">How it works</a>', '<a href="#process">Πώς λειτουργεί</a>'),
    ('<a href="#about">About</a>', '<a href="#about">Σχετικά</a>'),
    ('<a href="#contact" class="nav-cta">Contact me</a>',
     '<a href="en/" class="lang" lang="en" hreflang="en" title="English">EN</a>\n        <a href="#contact" class="nav-cta">Επικοινωνία</a>'),
    ('<div class="eyebrow">Insurance Advisor &middot; Cyprus</div>', '<div class="eyebrow">Ασφαλιστικός Σύμβουλος &middot; Κύπρος</div>'),
    ("<h1>Protection that fits <em>your life</em>, explained clearly.</h1>",
     "<h1>Προστασία στα μέτρα <em>της ζωής σου</em>, με απλά λόγια.</h1>"),
    ("I help individuals, families and businesses in Cyprus understand their insurance options and choose cover with confidence. One conversation, no jargon, no pressure.",
     "Βοηθώ ιδιώτες, οικογένειες και επιχειρήσεις στην Κύπρο να κατανοήσουν τις ασφαλιστικές τους επιλογές και να επιλέξουν κάλυψη με σιγουριά. Μία συζήτηση, χωρίς δύσκολους όρους, χωρίς πίεση."),
    (">Book a free consultation</a>", ">Κλείσε δωρεάν συνάντηση</a>"),
    (">Explore services</a>", ">Δες τις υπηρεσίες</a>"),
    ('alt="Portrait of Jordan Angelov"', 'alt="Φωτογραφία του Jordan Angelov"'),
    ("Personal, one-to-one advice</li>", "Προσωπική εξυπηρέτηση, ένας προς έναν</li>"),
    ("Plain-language explanations</li>", "Εξηγήσεις σε απλή γλώσσα</li>"),
    ("Ongoing support, including claims</li>", "Συνεχής υποστήριξη, και στις αποζημιώσεις</li>"),
    ('<div class="eyebrow">What I can help with</div>', '<div class="eyebrow">Πώς μπορώ να βοηθήσω</div>'),
    ("Cover for every stage of life.</h2>", "Κάλυψη για κάθε στάδιο της ζωής.</h2>"),
    ("Whether you're starting a family, buying a home or running a business, I'll help you find protection that matches your priorities and budget.",
     "Είτε δημιουργείς οικογένεια, είτε αγοράζεις σπίτι, είτε έχεις επιχείρηση, θα σε βοηθήσω να βρεις την προστασία που ταιριάζει στις προτεραιότητες και στον προϋπολογισμό σου."),
    ("<h3>Life Insurance</h3><p>Financially protect the people you love.</p>",
     "<h3>Ασφάλεια Ζωής</h3><p>Προστάτευσε οικονομικά τους ανθρώπους που αγαπάς.</p>"),
    ("<h3>Health</h3><p>Quality medical care, when you need it most.</p>",
     "<h3>Υγεία</h3><p>Ποιοτική ιατρική φροντίδα, όταν τη χρειάζεσαι περισσότερο.</p>"),
    ("<h3>Motor</h3><p>Protection and peace of mind on every journey.</p>",
     "<h3>Οχήματα</h3><p>Προστασία και σιγουριά σε κάθε σου διαδρομή.</p>"),
    ("<h3>Home</h3><p>Insure your home and everything you have built.</p>",
     "<h3>Κατοικία</h3><p>Ασφάλισε το σπίτι σου και όσα έχεις δημιουργήσει.</p>"),
    ("<h3>Corporate Plans</h3><p>Comprehensive solutions for your business and your staff.</p>",
     "<h3>Εταιρικά Σχέδια</h3><p>Ολοκληρωμένες λύσεις για την επιχείρηση και το προσωπικό σου.</p>"),
    ("<h3>Savings &amp; Investment</h3><p>Start building your financial future today.</p>",
     "<h3>Αποταμίευση &amp; Επένδυση</h3><p>Ξεκίνα σήμερα να χτίζεις το οικονομικό σου μέλλον.</p>"),
    ('<div class="eyebrow">How it works</div>', '<div class="eyebrow">Πώς λειτουργεί</div>'),
    ("Simple, from first call to cover.</h2>", "Απλά, από το πρώτο τηλεφώνημα έως την κάλυψη.</h2>"),
    ("<h3>Let's talk</h3><p>We meet in person or online to understand your situation, your priorities and any cover you already have.</p>",
     "<h3>Γνωριμία</h3><p>Συναντιόμαστε δια ζώσης ή διαδικτυακά, για να κατανοήσω την κατάστασή σου, τις προτεραιότητές σου και τις καλύψεις που ήδη έχεις.</p>"),
    ("<h3>Clear options</h3><p>I explain suitable options side by side, in plain language, so you know exactly what you're paying for.</p>",
     "<h3>Ξεκάθαρες επιλογές</h3><p>Σου εξηγώ τις κατάλληλες επιλογές σε απλή γλώσσα, ώστε να ξέρεις ακριβώς για τι πληρώνεις.</p>"),
    ("<h3>Ongoing support</h3><p>Once you're covered, I stay your point of contact for renewals, changes and claims.</p>",
     "<h3>Συνεχής υποστήριξη</h3><p>Μετά την ασφάλιση, παραμένω ο σύνδεσμός σου για ανανεώσεις, αλλαγές και αποζημιώσεις.</p>"),
    ('<div class="eyebrow">About me</div>', '<div class="eyebrow">Σχετικά με εμένα</div>'),
    ("Someone on your side.</h2>", "Κάποιος στο πλευρό σου.</h2>"),
    ("<small>Insurance Advisor</small>", "<small>Ασφαλιστικός Σύμβουλος</small>"),
    ("I'm Jordan Angelov, an insurance advisor based in Cyprus. Insurance can feel complicated, and my job is to make it simple. I take the time to understand what matters to you, then help you choose cover that genuinely fits.",
     "Είμαι ο Jordan Angelov, ασφαλιστικός σύμβουλος στην Κύπρο. Η ασφάλιση μπορεί να φαίνεται περίπλοκη και η δουλειά μου είναι να την κάνω απλή. Αφιερώνω χρόνο για να καταλάβω τι είναι σημαντικό για σένα και σε βοηθώ να επιλέξεις την κάλυψη που πραγματικά σου ταιριάζει."),
    ("I work with individuals, families and business owners across Cyprus, and I believe good advice starts with listening.",
     "Συνεργάζομαι με ιδιώτες, οικογένειες και επιχειρηματίες σε όλη την Κύπρο και πιστεύω ότι η σωστή συμβουλή ξεκινά με το να ακούς."),
    ('<div class="eyebrow">Get in touch</div>', '<div class="eyebrow">Επικοινωνία</div>'),
    ("Let's find the right protection for you.</h2>", "Ας βρούμε μαζί την κατάλληλη προστασία για σένα.</h2>"),
    ("Reviewing your existing cover or starting fresh? Reach out and I'll get back to you within one working day.",
     "Θέλεις να επανεξετάσεις την υπάρχουσα κάλυψή σου ή ξεκινάς από την αρχή; Επικοινώνησε μαζί μου και θα σου απαντήσω εντός μίας εργάσιμης ημέρας."),
    ("<span>Call</span>", "<span>Τηλέφωνο</span>"),
    ("<b>Send a message</b>", "<b>Στείλε μήνυμα</b>"),
    ("?subject=Insurance%20consultation", "?subject=" + urllib.parse.quote("Ασφαλιστική συμβουλή")),
    ("Jordan Angelov &middot; Insurance Advisor, Cyprus</span>", "Jordan Angelov &middot; Ασφαλιστικός Σύμβουλος, Κύπρος</span>"),
]

en = sub(base, EN, "en")
el = sub(base, EL, "el")


def seo_tags(lang):
    if not SITE_URL:
        return ""
    url = SITE_URL + ("/" if lang == "el" else "/en/")
    title, desc = {
        "el": ("Jordan Angelov | Ασφαλιστικός Σύμβουλος στην Κύπρο",
               "Προσωπική καθοδήγηση για ασφάλειες ζωής, υγείας, οχημάτων, κατοικίας και επιχειρήσεων στην Κύπρο."),
        "en": ("Jordan Angelov | Insurance Advisor in Cyprus",
               "Personal guidance on life, health, motor, home and business insurance in Cyprus."),
    }[lang]
    return (
        f'  <link rel="canonical" href="{url}" />\n'
        f'  <link rel="alternate" hreflang="el" href="{SITE_URL}/" />\n'
        f'  <link rel="alternate" hreflang="en" href="{SITE_URL}/en/" />\n'
        f'  <link rel="alternate" hreflang="x-default" href="{SITE_URL}/" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:url" content="{url}" />\n'
        f'  <meta property="og:title" content="{title}" />\n'
        f'  <meta property="og:description" content="{desc}" />\n'
        f'  <meta property="og:image" content="{SITE_URL}/assets/profile.jpeg" />\n'
        f'  <meta property="og:locale" content="{"el_GR" if lang == "el" else "en_GB"}" />\n'
        f'  <meta name="twitter:card" content="summary" />\n'
    )

if GOATCOUNTER_CODE:
    gc = (f'  <script data-goatcounter="https://{GOATCOUNTER_CODE}.goatcounter.com/count"\n'
          '          async src="//gc.zgo.at/count.js"></script>\n</body>')
    el = el.replace("</body>", gc, 1)
    en = en.replace("</body>", gc, 1)
    print("GoatCounter enabled:", GOATCOUNTER_CODE)

TITLE_END = "</title>\n"
el = el.replace(TITLE_END, TITLE_END + seo_tags("el"), 1)
en = en.replace(TITLE_END, TITLE_END + seo_tags("en"), 1)

def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

if SITE_URL:
    host = SITE_URL.split("://", 1)[-1].strip("/")
    write("CNAME", host + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "".join(
              f'  <url>\n    <loc>{SITE_URL}{path}</loc>\n'
              f'    <xhtml:link rel="alternate" hreflang="el" href="{SITE_URL}/" />\n'
              f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/en/" />\n  </url>\n'
              for path in ("/", "/en/"))
          + "</urlset>\n")
    print("Domain files written for", host)

os.makedirs(os.path.join(ROOT, "en"), exist_ok=True)
with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(el)
with open(os.path.join(ROOT, "en", "index.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(en)
print("Built index.html (Greek) and en/index.html (English)")
