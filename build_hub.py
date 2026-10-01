"""Build identity-hub.html: course + knowledge base as two tabs in one page.

Why a build script and not a hand-merged file: identity-learning.html (the
course) and identity.html (the knowledge base) stay the real source files --
same editing workflow as before (edit the course when expanding a topic,
edit the KB after every session). This script assembles them into one
page so there's a single URL to pin on mobile, the same pattern this
project already uses for the Train Deck (built from aigp.html/learning.html,
not hand-merged).

Run this, then republish identity-hub.html, whenever either source file
changes:

    python3 build_hub.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
COURSE_SRC = HERE / "identity-learning.html"
KB_SRC = HERE / "identity.html"
OUT = HERE / "identity-hub.html"

TABBAR_HEIGHT = 48  # px -- each tab's own sticky header is pushed down by this much


def extract(path):
    """Pull the <style> body and the full <body>...</body> content out of a page."""
    s = path.read_text()
    style = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    body = re.search(r"<body>(.*?)</body>", s, re.S).group(1)
    return style, body


def strip_shared_rules(style_text, tab_id):
    """Remove the global reset/root rules every page carries (defined once, shared,
    at the top of the merged file) -- except body{}, which each page sets a
    genuinely different font-size/line-height for, so that one gets rewritten to
    scope onto the tab's own container instead of discarded.
    """
    style_text = re.sub(r":root\{.*?\n\}\n", "", style_text, count=1, flags=re.S)
    style_text = style_text.replace("*{box-sizing:border-box}\n", "")
    style_text = re.sub(r"html\{[^}]*\}\n", "", style_text)
    style_text = re.sub(r"^a\{color:var\(--accent\)\}\n", "", style_text, flags=re.M)
    style_text = re.sub(r"h1,h2,h3,h4\{[^}]*\}\n", "", style_text)
    style_text = re.sub(r"^body\{", f"#{tab_id}{{", style_text, count=1, flags=re.M)
    return style_text


def push_down_header(style_text):
    """Each tab's own sticky header sits just below the shared tab bar, not at the very top."""
    return style_text.replace(
        "header.top{position:sticky;top:env(safe-area-inset-top,0px);",
        f"header.top{{position:sticky;top:calc(env(safe-area-inset-top,0px) + {TABBAR_HEIGHT}px);",
    )


def main():
    course_style, course_body = extract(COURSE_SRC)
    kb_style, kb_body = extract(KB_SRC)

    course_style = push_down_header(strip_shared_rules(course_style, "tab-course"))
    kb_style = push_down_header(strip_shared_rules(kb_style, "tab-kb"))

    # In the hub, cross-links between the two pages become same-page hash
    # links (#tab-course, #tab-kb, or #<module-id> for the KB's 36 "Module N"
    # links) -- a single click-interceptor in the script below switches tabs
    # and scrolls, instead of navigating out to the old standalone pages.
    kb_body = re.sub(
        r'href="https://claude\.ai/artifact/F9SKy7aoqre6AaReiMnivs#([^"]+)"',
        r'href="#\1"',
        kb_body,
    )
    kb_body = kb_body.replace(
        'href="https://claude.ai/artifact/F9SKy7aoqre6AaReiMnivs"', 'href="#tab-course"'
    )
    course_body = course_body.replace(
        'href="https://claude.ai/artifact/1qiEcgjDBvi95HRvZKhMrd"', 'href="#tab-kb"'
    )

    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Identity Security</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{{
  --bg:#FFFFFF; --surface:#FFFFFF; --surface-2:#F4F6FA; --text:#1B2437; --muted:#5B6576;
  --border:#E3E7EE; --accent:#1F6FB2; --accent-soft:#E7F1FA; --good:#16895B; --good-soft:#E3F3EA;
  --warn:#B7791F; --warn-soft:#FBF1DF; --bad:#D1394E; --bad-soft:#FBE6E8; --code:#F4F6FA;
  --govern:#5B47C9;
  --display:'Bricolage Grotesque','Avenir Next',system-ui,sans-serif; --body:'IBM Plex Sans','Helvetica Neue',Arial,sans-serif; --mono:'IBM Plex Mono',ui-monospace,Menlo,monospace;
  --radius:14px; --maxw:960px; color-scheme:light;
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth;background:var(--bg)}}
body{{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 var(--body);-webkit-text-size-adjust:100%;-webkit-font-smoothing:antialiased}}
a{{color:var(--accent)}}
h1,h2,h3,h4{{font-family:var(--display);text-wrap:balance}}

/* -- tab bar, shared -- */
.tabbar{{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;height:{TABBAR_HEIGHT}px;display:flex;background:#FFFFFF;border-bottom:1px solid var(--border);box-shadow:0 1px 2px rgba(20,30,50,.04)}}
.tabbtn{{flex:1;border:0;background:none;font:600 .86rem var(--display);color:var(--muted);cursor:pointer;border-bottom:3px solid transparent}}
.tabbtn.active{{color:var(--govern);border-bottom-color:var(--govern)}}
.tabpanel[hidden]{{display:none}}

/* -- course tab styles -- */
{course_style}

/* -- knowledge base tab styles -- */
{kb_style}
</style>
</head>
<body>

<div class="tabbar">
  <button class="tabbtn" id="btn-course" type="button">Course</button>
  <button class="tabbtn" id="btn-kb" type="button">Knowledge Base</button>
</div>

<div class="tabpanel" id="tab-course">
{course_body}
</div>

<div class="tabpanel" id="tab-kb" hidden>
{kb_body}
</div>

<script>
(() => {{
  const course = document.getElementById("tab-course");
  const kb = document.getElementById("tab-kb");
  const btnCourse = document.getElementById("btn-course");
  const btnKb = document.getElementById("btn-kb");
  const KEY = "identity-hub-tab";

  function show(which, scrollToHash) {{
    const toCourse = which === "course";
    course.hidden = !toCourse;
    kb.hidden = toCourse;
    btnCourse.classList.toggle("active", toCourse);
    btnKb.classList.toggle("active", !toCourse);
    try {{ localStorage.setItem(KEY, which); }} catch (e) {{}}
    if (scrollToHash && location.hash) {{
      const el = document.getElementById(location.hash.slice(1));
      if (el) el.scrollIntoView();
    }}
  }}

  btnCourse.addEventListener("click", () => show("course", false));
  btnKb.addEventListener("click", () => show("kb", false));

  // Every in-page cross-link (the KB's 36 "Module N" links, the KB<->course
  // links) is a same-page #hash now. Intercept clicks on those: switch to
  // whichever tab actually contains the target, then scroll to it -- instead
  // of the browser trying to scroll to an element that's still hidden.
  document.addEventListener("click", (e) => {{
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute("href").slice(1);
    const target = document.getElementById(id);
    if (!target) return;
    e.preventDefault();
    if (kb.contains(target)) show("kb", false);
    else if (course.contains(target)) show("course", false);
    target.scrollIntoView();
  }});

  // Deep link on load: if the hash points at an id that lives in the KB panel, open that tab.
  let initial = "course";
  try {{ initial = localStorage.getItem(KEY) || "course"; }} catch (e) {{}}
  if (location.hash) {{
    const target = document.getElementById(location.hash.slice(1));
    if (target && kb.contains(target)) initial = "kb";
    else if (target && course.contains(target)) initial = "course";
  }}
  show(initial, true);
}})();
</script>

</body>
</html>
"""
    OUT.write_text(page)
    print(f"Built {OUT} ({len(page)} chars)")


if __name__ == "__main__":
    main()
