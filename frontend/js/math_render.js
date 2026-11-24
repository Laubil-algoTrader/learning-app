/**
 * Lightweight offline mathematical typography formatter.
 *
 * Turns math code spans like `(x² + 2x − 3)/(x² + 8x + 16)`, `2^(x+1)`, `√(b² − 4ac)` or
 * `v_0` into crisp typographic HTML (stacked fractions, superscripts, subscripts, radical
 * overbars) while leaving real programming code (`digitalWrite(13, HIGH)`, URLs, paths)
 * untouched in monospace.
 */

const CODE_HINT =
  /(digitalWrite|analogWrite|analogRead|pinMode|Serial\.|delay\(|void\s|int\s|float\s|const\s|return\s|if\s*\(|for\s*\(|while\s*\(|#include|http:|https:|\/\/|::|&&|\|\||==|!=|<=|>=|<-|;|{|}|"|'|\.py|\.js|\.db)/;

const MATH_SIGNAL =
  /[²³⁴⁵⁶⁷⁸⁹⁰¹⁻√∛π±×·÷≤≥≠∞⇒⇔∈∉⊂⊃∪∩∀∃αβγθλμΔΣ]|(\b(?:sen|sin|cos|tan|tg|cot|sec|csc|log|ln)\b)|(\^[0-9(a-zA-Z−-])|([a-zA-Z]_[0-9a-zA-Z])|(\([^()]+\)\s*\/\s*\([^()]+\))|(\b\d+\s*\/\s*\d+\b)/;

function escHtml(str) {
  return String(str ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function isMathExpr(raw) {
  const s = String(raw || "").trim();
  if (!s || s.length > 140) return false;
  if (CODE_HINT.test(s)) return false;
  // Avoid converting plain words/identifiers like `al-teoria-conjuntos` or `m/s`
  if (/^[a-z0-9-]+$/i.test(s) && s.includes("-")) return false;
  if (/^[a-zA-Z]{2,}\/[a-zA-Z]{1,3}$/.test(s)) return false;
  return MATH_SIGNAL.test(s) || (/^[0-9a-zA-Z\s+\-−*/=<>(),.·^_]+$/.test(s) && /[=+\-−*/^]/.test(s));
}

function formatInner(escaped) {
  let out = escaped;
  // Radicals with parenthesized radicands: √(expr) and ∛(expr)
  out = out.replace(/(√|∛)\(([^()]+)\)/g, (_, sym, body) => {
    const idx = sym === "∛" ? '<sup class="math-rad-idx">3</sup>' : "";
    return `<span class="math-rad-wrap">${idx}<span class="math-rad-sym">√</span><span class="math-rad">${body}</span></span>`;
  });
  // Explicit superscripts: ^(expr) or ^token
  out = out.replace(/\^\(([^()]+)\)/g, "<sup>$1</sup>");
  out = out.replace(/\^([−\-+]?[0-9a-zA-Zπ]+)/g, "<sup>$1</sup>");
  // Explicit subscripts: _(expr) or _0, _x
  out = out.replace(/_\(([^()]+)\)/g, "<sub>$1</sub>");
  out = out.replace(/([A-Za-zα-ωΑ-Ω])_([0-9a-zA-Z]+)/g, "$1<sub>$2</sub>");
  // Parenthesized fraction (A)/(B) or (A)/denom or num/(B)
  out = out.replace(
    /\(([^()]+)\)\s*\/\s*\(([^()]+)\)/g,
    '<span class="math-frac"><span>$1</span><span>$2</span></span>'
  );
  out = out.replace(
    /\(([^()]+)\)\s*\/\s*([0-9a-zA-Zπ√²³⁴⁵⁶⁷⁸⁹⁰¹⁻·]+(?:\s*<su[bp]>[^<]+<\/su[bp]>)?)/g,
    '<span class="math-frac"><span>$1</span><span>$2</span></span>'
  );
  out = out.replace(
    /(?<![A-Za-z0-9/])([0-9a-zA-Zπ√²³⁴⁵⁶⁷⁸⁹⁰¹⁻·]+)\s*\/\s*\(([^()]+)\)/g,
    '<span class="math-frac"><span>$1</span><span>$2</span></span>'
  );
  // Simple standalone numeric or short algebraic fraction (e.g. 1/4, x/2, 3x/2)
  out = out.replace(
    /(?<![A-Za-z0-9_/])(\d*[a-zA-Zπ]?|\d+)\/(\d+[a-zA-Z]?)(?![A-Za-z0-9_/])/g,
    (m, num, den) => {
      if (num.length > 4 || den.length > 4) return m;
      return `<span class="math-frac"><span>${num}</span><span>${den}</span></span>`;
    }
  );
  return out;
}

/** Format an inline backtick span as math typography if it is math, else standard code. */
export function formatInlineCode(raw) {
  const escaped = escHtml(raw);
  if (!isMathExpr(raw)) return `<code>${escaped}</code>`;
  return `<span class="math-inline">${formatInner(escaped)}</span>`;
}
